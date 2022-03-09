#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv
outHandle=open("%s_contiglengths.txt"%argv[1],'w')
genome_handle=open("%s"%argv[1],"r")
for seq_record in SeqIO.parse(genome_handle,"fasta"):
	seqlength=len(seq_record.seq)
	ident=seq_record.id
	seq="%s"%seq_record.seq
	numC=seq.count('C')
	numG=seq.count('G')
	gcpercent=((float(numC)+float(numG))/float(seqlength))*100
	outHandle.write("%s\t%s\t%s\n"%(ident,seqlength,gcpercent))
genome_handle.close()
outHandle.close()
