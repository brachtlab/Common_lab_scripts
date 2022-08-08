#!/usr/bin/python
from Bio import SeqIO
import sys
from sys import argv
inHandle=open("%s"%argv[1],"r")
outHandle=open("%s_coverageColumns.txt"%argv[1],'w')
outHandle.write("scaffold\tlength\tcoverage\tGCpercent\n")
for line in inHandle:
	combined=line.split()[0]
	print combined
	cov=combined.split('_')[2]
	length=int(line.split()[1])
	GC=float(line.split()[2])
	number=int(cov[3:])
	outHandle.write("%s\t%s\t%s\t%s\n"%(combined,length,number,GC))


inHandle.close()
outHandle.close()
