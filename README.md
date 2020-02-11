# Common_lab_scripts
Commonly used Bracht lab Python scripts


blast_analysis.py calculates how much of the query length (Alternative assembly) matched to the subject length (Reference assembly) at a defined percent identity threshold:
./blast_analysis.py <query fasta> <blast_to_reference_outfmt6.txt> <percent identity to consider, as integer (like '98' for 98 %)>
