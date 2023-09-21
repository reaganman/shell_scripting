'''takes a fasta filepath and output filepath. counts the total number of seqs and bp and writes to outfile'''
import sys
import os

def count_fasta(in_file, out_file):
    seqs=0
    bp=0
    for line in infile.readlines(): 
        if line[0] == '>':
            seqs+=1
        else: 
            bp+=len(line)
    total_seqs = ('total seqs: ' + str(seqs))
    total_bp = ('total bp: ' + str(bp))
    print('total seqs: ', str(seqs))
    print('total bp: ', str(bp))
    out_file.write(in_file.name + '\n')
    out_file.write(total_seqs + '\n')
    out_file.write(total_bp + '\n')



if __name__ == '__main__':
    in_file = sys.argv[1]
    out_file = sys.argv[2]
    with open(in_file, 'r') as infile:
        with open(out_file, 'a') as outfile:
            count_fasta(infile, outfile)
