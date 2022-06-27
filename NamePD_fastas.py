#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv
dupsHandle=open("dups.bed",'r')
purgePriHandle=open('mephisto_alpha.purged.fa','r')
purgeHapHandle=open('mephisto_alpha.hap.fa','r')
renamedPrimaryHandle=open('mephisto_alpha_primary.fasta','w')
renamedAltHandle=open('mephisto_alpha_alternate.fasta','w')
correlationsHandle=open('primary_contigs_correlation_with_original_names.txt','w')
dupsDict={}
matchingDict={}
junkDict={}
primaryDict={}
nmDict={}
x=0
for line in dupsHandle:
	dup=line.split()[0]
	type=line.split()[3]
	if type=='HAPLOTIG' or type=='OVLP':
		matching=line.split()[4]
		x+=1
		dupsDict[dup]=matching
		matchingDict[matching]=1#temporary number will increment below
		primaryDict[matching]='TEMPORARY'
	elif type=='JUNK':
		junkDict[dup]=1
	
j=0
primary_counter=1
for seq_record in SeqIO.parse(purgePriHandle,'fasta'):
	j+=1
	id='%s'%seq_record.id
	if dupsDict.has_key(id):
		matching_name=dupsDict[id]
		if primaryDict.has_key(matching_name):
			masterName=primaryDict[matching_name]
			if masterName=='TEMPORARY':
				masterName='Contig%s'%primary_counter
				primary_counter+=1 
				primaryDict[matching_name]=masterName
		else:#add to dictionary
			masterName='Contig%s'%primary_counter
			primary_counter+=1
			primaryDict[matching_name]=masterName
		hapName=masterName+'.'+'%s'%matchingDict[matching_name]
		renamedPrimaryHandle.write('>%s\n%s\n'%(hapName,seq_record.seq))
		matchingDict[matching_name]+=1#increment haplotig count
	elif primaryDict.has_key(id):
		updatedName=primaryDict[id]
		if updatedName=='TEMPORARY':
			updatedName='Contig%s'%primary_counter
			primary_counter+=1
			primaryDict[id]=updatedName
		renamedPrimaryHandle.write('>%s\n%s\n'%(updatedName,seq_record.seq))
	else:
		if junkDict.has_key(id):
			pass #strip out the junk!
		else:
			newName='Contig%s'%primary_counter
			primary_counter+=1
			renamedPrimaryHandle.write('>%s\n%s\n'%(newName,seq_record.seq))
			nmDict[id]=newName

for seq_record in SeqIO.parse(purgeHapHandle,'fasta'):
        j+=1
        ide='%s'%seq_record.id.split('ap_')[1]
	id=ide.split('|arrow')[0]+'|arrow'
	print id
        if dupsDict.has_key(id):
                matching_name=dupsDict[id]
                if primaryDict.has_key(matching_name):
                        masterName=primaryDict[matching_name]
                        if masterName=='TEMPORARY':
                                masterName='Contig%s'%primary_counter
                                primary_counter+=1
                                primaryDict[matching_name]=masterName
                else:#add to dictionary
                        masterName='Contig%s'%primary_counter
                        primary_counter+=1
                        primaryDict[matching_name]=masterName
                hapName=masterName+'.'+'%s'%matchingDict[matching_name]
                renamedAltHandle.write('>%s\n%s\n'%(hapName,seq_record.seq))
                matchingDict[matching_name]+=1#increment haplotig count
        elif primaryDict.has_key(id):
                updatedName=primaryDict[id]
                if updatedName=='TEMPORARY':
                        updatedName='Contig%s'%primary_counter
                        primary_counter+=1
                        primaryDict[id]=updatedName
                renamedAltHandle.write('>%s\n%s\n'%(updatedName,seq_record.seq))
        else:
                if junkDict.has_key(id):
                        pass #strip out the junk!
                else:
                        newName='Contig%s'%primary_counter
                        primary_counter+=1
                        renamedAltHandle.write('>%s\n%s\n'%(newName,seq_record.seq))
                        nmDict[id]=newName


	
print primaryDict
print matchingDict
print 'found %s primary contigs'%(primary_counter-1)
pkeys=primaryDict.keys()
for p in pkeys:
	correlationsHandle.write('%s\t%s\t%s\n'%(p,primaryDict[p],matchingDict[p]))
nmkeys=nmDict.keys()
for nm in nmkeys:
	correlationsHandle.write('%s\t%s\tno matching contig, retained as primary\n'%(nm,nmDict[nm]))
dupsHandle.close()	
purgePriHandle.close()
purgeHapHandle.close()
renamedPrimaryHandle.close()
correlationsHandle.close()
renamedAltHandle.close()
