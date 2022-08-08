#!/usr/bin/env python
import sys
from sys import argv
import Bio
from Bio import SeqIO

#calculating_contig_coverage.py <depth_file> <genome_fasta>

depth_handle=open("%s"%argv[1],"r")
out_handle=open("%s_depth.txt"%(argv[2]),"w")
genome_handle=open("%s"%argv[2],"r")
x=0
depthDict={}
lengthDict={}
GC_Dict={}
for seq_record in SeqIO.parse(genome_handle,"fasta"):
	sequence=seq_record.seq
	numG=sequence.count('G')
	numC=sequence.count('C')
	length=len(sequence)
	percent_GC=(float(numG)+float(numC))/(float(length))
	GC_Dict[seq_record.id]=percent_GC

old_contig="initial"
j=0
for line in depth_handle:
	j+=1
	if j%100000==0:
		print "processed %s million basepairs."%(float(j)/1000000)
	contig=line.split()[0]
	depth=int(line.split()[2])
	if contig==old_contig:
		sum=depthDict[contig]+depth
		depthDict[contig]=sum
		x=x+1
	else:
		depthDict[contig]=depth
		lengthDict[old_contig]=x
		x=1
	old_contig=contig
lengthDict[contig]=x
list_of_contigs=depthDict.keys()
genome_depth=0
genome_length=0
for c in list_of_contigs:
	length_of_contig=lengthDict[c]
	total_depth=depthDict[c]
	genome_depth+=total_depth
	genome_length+=length_of_contig
	average_depth=float(total_depth)/float(length_of_contig)
	print c
	print average_depth
	if GC_Dict.has_key(c):
		GC=GC_Dict[c]
	else:
		GC='unknown'
	out_handle.write("%s\t%s\t%s\t%s\n"%(c,average_depth,length_of_contig,GC))
print list_of_contigs
print 'genomic total depth is %s'%(float(genome_depth)/float(genome_length))
depth_handle.close()
out_handle.close()
genome_handle.close()
