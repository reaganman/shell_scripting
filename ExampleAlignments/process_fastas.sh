#processes fasta files in the current directory by calling count_fasta and split_fasta.py
#creates log file w/ number of seqs and number of bp from original fastas and creates an individal_fastas directory with#seperate fastas for each seq

for i in *.fasta; do python3 count_fasta.py $i log.txt; python3 split_fasta.py $i individual_fastas; done
