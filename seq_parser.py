import subprocess
import pandas as pd
import sys

def get_all_seqs(in_bam, out_file="seqs.txt"):
    
    seqs_info_df = pd.DataFrame(columns=['seq_ID', 'seq_len'])
    samtools_cmd = ['samtools', 'view', '-h', in_bam]
    
    proc = subprocess.Popen(samtools_cmd, stdout=subprocess.PIPE)
    for bytes_line in proc.stdout:
        line = bytes_line.decode("utf-8")
        if line.split()[0] == "@HD":
            pass
        elif line.split()[0] == "@SQ":
            seq_ID = line.split()[1].replace("SN:","")
            seq_len = int(line.split()[2].replace("LN:", ""))
            seqs_info_dict = {'seq_ID': seq_ID, 'seq_len': seq_len}
            seqs_info_df = seqs_info_df.append(seqs_info_dict, ignore_index=True)
            #with open(out_file, "a") as f:
                #f.write("\t".join([seq_ID, seq_len]) + "\n")
        else:
            break

    #print(seqs_info_df.head())
    return seqs_info_df


if __name__ == "__main__":
    get_all_seqs(sys.argv[1])