import argparse
import pandas as pd
import matplotlib.pyplot as plt
from windows_depth import get_windows_depth

def plot_coverage(depth_file):

  df = pd.read_csv("window_depths.out.tsv", sep="\t", names=['sequence', 'position', 'depth'])
  df1 = df.astype({'position': 'object'})

  # split original dataframe based on the sequence ID
  dfs = list(df1.groupby('sequence'))
  dfs = [g[1] for g in list(dfs)]

  #print(dfs)

  if len(dfs) == 1:
    fig, ax = plt.subplots(1, 1)
    ax.bar(x=dfs[0]['position'], height=dfs[0]['depth'])
  else:
    # create subplots where each subplot is a barplot from a different sequence
    fig, axes = plt.subplots(len(dfs), 1)
    for idx, ax in enumerate(axes):
      #print(f"index: {idx} | ax: {ax}")
      ax.bar(x=dfs[idx]['position'], height=dfs[idx]['depth'])

  # set the spacing between subplots
  fig.tight_layout()
  # plt.show()
  plt.savefig('coverage.png')

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--bed', help='Bed file containing depth per base')
    args = parser.parse_args()
    
    if args.bed:
        get_windows_depth(args.bed)
    

    in_f = args.i
    df = pd.read_csv(in_f, sep=" ", names=['sequence', 'start', 'end', 'depth'])
    print('first three lines of input file:')
    print(df.head(3))

    hist_plot = sns.histplot(data=df, x="start", y='depth')
    fig = hist_plot.get_figure()

if __name__ == "__main__":
    main()    
