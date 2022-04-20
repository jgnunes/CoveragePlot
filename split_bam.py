import sys
import subprocess

def split_bam(in_bam):
    bamtools_cmd = ["bamtools", "split", "-in", in_bam, "-reference"]
    subprocess.run(bamtools_cmd)
    
if __name__ == '__main__':
    split_bam(sys.argv[1])