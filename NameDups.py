#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv
dupsHandle=open("dups.bed",'r')
genomeHandle=open('mephisto_alpha.fasta','r')
outHandle=open('mephisto_alpha_rename.fasta','w')
correlationsHandle=open('primary_contigs_correlation_with_original_names.txt','w')
dupsDict={}
matchingDict={}
junkDict={}
primaryDict={}
x=0
for line in dupsHandle:
	dup=line.split()[0]
	type=line.split()[3]
	if type=='HAPLOTIG' or type=='OVLP':
		matching=line.split()[4]
		x+=1
		dupsDict[dup]=matching
		matchingDict[matching]=1
		primaryDict[matching]='TEMPORARY'
	elif type=='JUNK':
		junkDict[dup]=1
	
j=0
for seq_record in SeqIO.parse(genomeHandle,'fasta'):
	j+=1
	id='%s'%seq_record.id
	if dupsDict.has_key(id):
		matching_name=dupsDict[id]
		if primaryDict.has_key(matching_name):
			masterName=primaryDict[matching_name]
			if masterName=='TEMPORARY':
				masterName='Contig%s'%j 
				primaryDict[matching_name]=masterName
		else:#add to dictionary
			masterName='Contig%s'%j
			primaryDict[matching_name]=masterName
		hapName=masterName+'.'+'%s'%matchingDict[matching_name]
		outHandle.write('>%s\n%s\n'%(hapName,seq_record.seq))
		matchingDict[matching_name]+=1#increment haplotig count
	elif primaryDict.has_key(id):
		updatedName=primaryDict[id]
		if updatedName=='TEMPORARY':
			updatedName='Contig%s'%j
			primaryDict[id]=updatedName
		outHandle.write('>%s\n%s\n'%(updatedName,seq_record.seq))
	else:
		if junkDict.has_key(id):
			pass #strip out the junk!
		else:
			newName='Contig%s'%j
			outHandle.write('>%s\n%s\n'%(newName,seq_record.seq))	
print primaryDict
print matchingDict
pkeys=primaryDict.keys()
for p in pkeys:
	correlationsHandle.write('%s\t%s\t%s\n'%(p,primaryDict[p],matchingDict[p]))
dupsHandle.close()	
genomeHandle.close()
outHandle.close()
correlationsHandle.close()
