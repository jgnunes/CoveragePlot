import subprocess
import sys

def get_covered_seqs(in_bam, out_file):
    samtools_cmd = ['samtools', 'view', in_bam]
    seqs = set()
    proc = subprocess.Popen(samtools_cmd, stdout=subprocess.PIPE)
    for bytes_line in proc.stdout:
        line = bytes_line.decode('utf-8')
        seq_ID = line.split()[2]
        if seq_ID not in seqs:
            # with open(out_file, "a") as f:
            #     f.write(seq_ID + "\n")
            seqs.add(seq_ID)

    return seqs

def main():
    get_covered_seqs(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
