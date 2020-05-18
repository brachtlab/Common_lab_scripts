#!/usr/bin/env python
import sys
from sys import argv

#./get_gene_from_gff.py <gene to find, be sure to include' -mRNA-1' at end > <gff to extract from>

gene_to_find=argv[1]
inHandle=open("%s"%argv[2],'r')
outHandle=open('%s_from_%s'%(argv[1],argv[2]),'w')
x=0
outHandle.write('##gff-version 3\n')
for line in inHandle:
	if line[:7]=='##FASTA':
		print 'triggered break'
		break
	elif line[:2]!='##':
		if gene_to_find in line:
			outHandle.write(line)
inHandle.close()
outHandle.close()
