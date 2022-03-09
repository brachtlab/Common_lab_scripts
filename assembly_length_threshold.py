#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv
outHandle=open("%s_over%sbp.fasta"%(argv[1],argv[2]),'w')
threshold=int(argv[2])
genome_handle=open("%s"%argv[1],"r")
for seq_record in SeqIO.parse(genome_handle,"fasta"):
	seqlength=len(seq_record.seq)
	if seqlength >=threshold:
		outHandle.write(">%s\n%s\n"%(seq_record.id,seq_record.seq))
genome_handle.close()
outHandle.close()
