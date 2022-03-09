# Common_lab_scripts
Commonly used Bracht lab Python scripts

Require Python2.7 and Biopython

NMS.py (Non Matching Sequences) is for subtractive blast. Run blast, output in outfmt6 and then NMS.py will separate an initial fasta into those sequences matching and those not matching. You can swtich whether the query or subject is read in the NMS.py script. 

Usage: ./NMS.py [fasta sequence file] [blast output, outfmt 6 file]

blast_analysis.py calculates how much of the query length (Alternative assembly) matched to the subject length (Reference assembly) at a defined percent identity threshold:
./blast_analysis.py <query fasta> <blast_to_reference_outfmt6.txt> <percent identity to consider, as integer (like '98' for 98 %)>
  
