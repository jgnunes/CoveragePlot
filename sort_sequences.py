import pandas as pd 
import sys 

def sort_sequences(in_df, upp_lim):
    #df = pd.read_csv(in_file, sep="\t", names=['seq_ID', 'length'])
    df1 = in_df.astype({'seq_len': 'int'})
    df1_sorted = df1.sort_values('seq_len', ascending=False)
    df1_sorted_sliced = df1_sorted.head(int(upp_lim)) # get first `upp lim` rows

    return df1_sorted_sliced

def retrieve_sequences(in_df, target_seqs_file):
    target_seqs_IDs = set()
    with open(target_seqs_file, "r") as f:
        for line in f:
            target_seq_ID = line.strip()
            target_seqs_IDs.add(target_seq_ID)

    df1 = in_df.loc[in_df['seq_ID'].isin(target_seqs_IDs)]
    
    return df1

if __name__ == "__main__":
    sort_sequences(sys.argv[1], sys.argv[2])
