#!/usr/bin/env python

from sys import argv
import re
from Bio import SeqIO

seq_d = SeqIO.parse(open(argv[1]), "fasta")

len_thresh = 100

genetic_code=1

for rec in seq_d:
  f1_bits = [bit for bit in str(rec.seq.translate(table=genetic_code)).split("*") if len(bit) >= len_thresh]
  f2_bits = [bit for bit in str(rec.seq[1:].translate(table=genetic_code)).split("*") if len(bit) >= len_thresh]
  f3_bits = [bit for bit in str(rec.seq[2:].translate(table=genetic_code)).split("*") if len(bit) >= len_thresh]

  rc_seq = rec.seq.reverse_complement()

  r1_bits = [bit for bit in str(rc_seq.translate(table=genetic_code)).split("*") if len(bit) >= len_thresh]
  r2_bits = [bit for bit in str(rc_seq[1:].translate(table=genetic_code)).split("*") if len(bit) >= len_thresh]
  r3_bits = [bit for bit in str(rc_seq[2:].translate(table=genetic_code)).split("*") if len(bit) >= len_thresh]


  j = 0
  for f1_bit in f1_bits:
    j += 1
    print ">%s_f1_%s\n%s" % (rec.name, j, f1_bit)
  j = 0
  for f2_bit in f2_bits:
    j += 1
    print ">%s_f2_%s\n%s" % (rec.name, j, f2_bit)
  j = 0
  for f3_bit in f3_bits:
    j += 1
    print ">%s_f3_%s\n%s" % (rec.name, j, f3_bit)

  j = 0
  for r1_bit in r1_bits:
    j += 1
    print ">%s_r1_%s\n%s" % (rec.name, j, r1_bit)
  j = 0
  for r2_bit in r2_bits:
    j += 1
    print ">%s_r2_%s\n%s" % (rec.name, j, r2_bit)
  j = 0
  for r3_bit in r3_bits:
    j += 1
    print ">%s_r3_%s\n%s" % (rec.name, j, r3_bit)







# vim: set sts=2 ts=2 sw=2:
