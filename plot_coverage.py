import time
import argparse
import os
import pandas as pd
import matplotlib.pyplot as plt
import shutil
from windows_depth import get_windows_depths, windows_to_base, windows_to_base_df
from split_bam import split_bam
from get_depth import get_depth, get_windows_depth
from covered_seqs import get_covered_seqs
from make_genome import make_genome_file, make_genome_windows
from seq_parser import get_all_seqs
from sort_sequences import sort_sequences, retrieve_sequences
from merge_images import merge_images

def plot_coverage(depth_file, out_filename, seq_ID, winSize):

  df = pd.read_csv(depth_file, sep="\t", names=['sequence', 'start', 'end', 'depth'])  
  df1 = df.astype({'start': 'int', 'end': 'int', 'depth': 'float'})

  df1['position'] = df1['start'] + (df1['end'] - df1['start'])/2
  df2 = df1.astype({'position': 'object'})
    
  fig, ax = plt.subplots(1,1)
  ax.bar(x=df2['position'], height=df2['depth'], width=winSize)
  ax.set_title(seq_ID)

  plt.savefig(out_filename)

def main():

    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    mutually_exclusive_group = optional.add_mutually_exclusive_group(required=False)
    mutually_exclusive_group.add_argument('--maxNumSeqs', help='Maximum number of sequences')
    mutually_exclusive_group.add_argument('--seqs', help='List of sequences to be used')
    required.add_argument('--bam', help='BAM mapping file')
    optional.add_argument('--winSize', help='Windows size')
    optional.add_argument('--img', help='List of images to concatenate')
    optional.add_argument('--depth', help='Depth file to use as input for generating plot')
    args = parser.parse_args()
    
    if args.bam:
        in_bam = args.bam
        
        start = time.time()
        print("Getting length information from genome sequences", flush=True)
        seqs_info = get_all_seqs(in_bam)
        if args.maxNumSeqs:
            seqs_info_sliced = sort_sequences(seqs_info, args.maxNumSeqs)
        elif args.seqs:
            seqs_info_sliced = retrieve_sequences(seqs_info, args.seqs)
        else:
            seqs_info_sliced = sort_sequences(seqs_info, len(seqs_info))
        end = time.time()
        elapsed_time = end - start
        print(f"Elapsed time: {elapsed_time}", flush=True)
        
        seqs_plots = []
        for index, row in seqs_info_sliced.iterrows():
          seq_ID, seq_len = row['seq_ID'], str(row['seq_len'])
          # create genome file
          start = time.time()
          print(f"Creating genome file for {seq_ID}", flush=True)
          genome_filename = f"{seq_ID}.genome.txt"
          with open(genome_filename, "w") as f:
            f.write("\t".join([seq_ID, seq_len]))
          end = time.time()
          elapsed_time = end - start
          print(f"Elapsed time: {elapsed_time}", flush=True)
          
          # create windows file
          start = time.time()
          print(f"Creating genome windows file for {seq_ID}", flush=True)
          windows_filename = make_genome_windows(genome_filename, args.winSize)
          end = time.time()
          elapsed_time = end - start
          print(f"Elapsed time: {elapsed_time}", flush=True)
          
          # calculate mean depth per windows
          start = time.time()
          print(f"Calculating mean depth per windows for {seq_ID}", flush=True)
          depth_per_windows = get_windows_depth(windows_filename, in_bam, seq_ID)
          end = time.time()
          elapsed_time = end - start
          print(f"Elapsed time: {elapsed_time}", flush=True)
          
          # creating plot for sequence
          start = time.time()
          print(f"Creating coverage plot for {seq_ID}", flush=True)
          out_plot_filename = f"{seq_ID}.coverage.png"
          seqs_plots.append(out_plot_filename)
          plot_coverage(depth_per_windows, out_plot_filename, seq_ID, int(args.winSize))
          end = time.time()
          elapsed_time = end - start
          print(f"Elapsed time: {elapsed_time}", flush=True)
        
        print(f"seqs_plots: {seqs_plots}", flush=True)
        print("Concatenating sequences coverages plots into final.coverage.png", flush=True)
        merge_images(seqs_plots, "final.coverage.png")
    
    if args.depth:
        depth_filename = args.depth
        out_filename = f"{depth_filename}.png"
        plot_coverage(depth_filename, out_filename, "coverage plot", int(args.winSize))

    if args.img:
        images = args.img.split()
        print("Concatenating images into final.coverage.png", flush=True)
        merge_images(images, "final.coverage.png")
   
if __name__ == "__main__":
    main()    
