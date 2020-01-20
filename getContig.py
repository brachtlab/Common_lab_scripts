#!/usr/bin/env python2.6
from Bio import SeqIO
import sys
from sys import argv
genome_handle=open("/Users/jbracht/meCyt_IP/oxy_fin.split.6.plus170.plusMito.asm","r")
contigname="%s"%argv[1] #getContig.py ContigXXXX.X
#print contigname
out=open(("%s.fasta"%contigname),"w")
records=[]
found=0
x=0
j=0
for seq_record in SeqIO.parse(genome_handle, "fasta"):
	x+=1
	if seq_record.id==contigname:
		records.append(seq_record)
		found=1
		j=x
if found==0:
	print "not found."
else:
	SeqIO.write(records,out,"fasta")
if found==1:
	print "found contig, it was # %s of %s total contigs"%(j,x)
genome_handle.close()
out.close()
