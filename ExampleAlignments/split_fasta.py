import sys
import os

def split_fasta(in_file, out_dir):
    current_sequence = None
    for line in in_file:
        if line.startswith('>'):
            # Found a new sequence header
            if current_sequence is not None:
                # Close the previous sequence file
                current_sequence.close()
            
            # Create a new sequence file
            seq_id = line.strip().split()[0][1:]
            source_fp = in_file.name.replace(".fasta", "_")
            seq_file_path = os.path.join(out_dir, f"{source_fp}{seq_id}.fasta")
            current_sequence = open(seq_file_path, 'w')
        elif current_sequence is not None:
            # Write sequence lines to the current sequence file
            current_sequence.write(line)

    if current_sequence is not None:
        # Close the last sequence file
        current_sequence.close()
            
    


if __name__ == '__main__':
    infile = sys.argv[1]
    outdir = sys.argv[2]
    try:
        os.mkdir(outdir)
    except:
        print('output diretory already exists')
    with open(infile, 'r') as in_file:
        split_fasta(in_file, outdir)
