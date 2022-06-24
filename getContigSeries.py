#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv
#getContigs.py <assemblyfile> <pattern such as 'Contig8.' include the period!>
outHandle=open("%s_series.fasta"%argv[2],'w')
genome_handle=open("%s"%argv[1],"r")
pattern='%s'%argv[2]
x=0
y=0
records=[]
for seq_record in SeqIO.parse(genome_handle,"fasta"):
	i="%s"%seq_record.id
	if pattern in i:
		records.append(seq_record)
	if i==pattern.rstrip('.'):
		records.append(seq_record)
SeqIO.write(records,outHandle, 'fasta')		
genome_handle.close()
outHandle.close()
