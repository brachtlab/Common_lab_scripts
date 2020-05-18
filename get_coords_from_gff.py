#!/usr/bin/env python
import sys
from sys import argv

inHandle=open("%s"%argv[1],'r')
outHandle=open('%s_gene_coordinates.txt'%argv[1],'w')
x=0
for line in inHandle:
	if line[:7]=='##FASTA':
		print 'triggered break'
		break
	elif line[:2]!='##':
		if line.split()[2]=='gene':
			scaffold=line.split()[0]
			start=int(line.split()[3])
			stop=int(line.split()[4])
			stuff=line.split()[8]
			items= stuff.split(';')
			for i in items:
				if i.split('=')[0]=='Name':
					n=i.split('=')[1]
			#print stop-start
			if stop<start:
				print 'reversed'
				print line
			outHandle.write('%s\t%s\t%s\t%s\n'%(scaffold,start,stop,n))
			x+=1
print 'processed %s genes'%x
inHandle.close()
outHandle.close()
