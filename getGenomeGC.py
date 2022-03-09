#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv
genome_handle=open("%s"%argv[1],"r")
seqlength=0
numC=0
numG=0
for seq_record in SeqIO.parse(genome_handle,"fasta"):
	seqlength+=len(seq_record.seq)
	ident=seq_record.id
	seq='%s'%seq_record.seq
	numC+=seq.count('C')
	numG+=seq.count('G')
gcpercent=((float(numC)+float(numG))/float(seqlength))*100
print 'GC content is %s percent'%gcpercent
genome_handle.close()
