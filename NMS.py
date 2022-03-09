#!/usr/bin/env python
import Bio
from Bio import SeqIO
from Bio import Seq
from Bio.Seq import Seq
import sys
from sys import argv

seqHandle=open("%s"%argv[1],"r")
blasthandle=open("%s"%argv[2],'r')
outHandle=open("%s_nonmatching.fasta"%argv[1],'w')
out2handle=open("%s_matching.fasta"%argv[1],'w')
Dict={}
for line in blasthandle:
	ident=line.split()[1]
	Dict[ident]=1	

for seq_record in SeqIO.parse(seqHandle, "fasta"):
	if Dict.has_key(seq_record.id):
		out2handle.write(">%s\n%s\n"%(seq_record.id,seq_record.seq))
	else:
		outHandle.write(">%s\n%s\n"%(seq_record.id,seq_record.seq))
seqHandle.close()
blasthandle.close()
outHandle.close()
out2handle.close()
