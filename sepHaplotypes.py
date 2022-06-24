#!/usr/bin/env python
from Bio import SeqIO
import sys
from sys import argv
genome_handle=open("%s"%argv[1],"r")
out1=open("%s_pri.fasta"%argv[1],"w")
out2=open("%s_alt.fasta"%argv[1],"w")
records1=[]
records2=[]
for seq_record in SeqIO.parse(genome_handle, "fasta"):
	ident='%s'%seq_record.id
	if '.' in ident: #is alt
		records2.append(seq_record)
	else: # is pri
		records1.append(seq_record)

SeqIO.write(records1,out1,"fasta")
SeqIO.write(records2,out2,"fasta")
genome_handle.close()
out1.close()
out2.close()
