#!/Library/Frameworks/EPD64.framework/Versions/Current/bin/python
from Bio import SeqIO
from Bio import Seq
from Bio.Seq import Seq
import sys
from sys import argv
records=[]
found=0
x=0
contigDict={}
contighandle=open("%s"%argv[1],"r")
for line in contighandle:
	gcontig=line.split()[0]
	gpos=line.rfind('g')
	contig=gcontig[:gpos-1]
	print contig	
	contigDict[contig]=1
	x+=1
genomehandle=open("oxy_fin.split.6.plus170.asm","r")
out=open("%s.fasta"%argv[1],"w")
for seq_record in SeqIO.parse(genomehandle,"fasta"):
	if contigDict.has_key("%s"%seq_record.id):
		out.write(">%s\n%s\n"%(seq_record.id, seq_record.seq))
		found+=1
print "found %s records out of %s total"%(found, x)
genomehandle.close()
contighandle.close()
out.close()

