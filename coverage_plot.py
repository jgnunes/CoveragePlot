"""
This script plots a coverage histogram over the length of the input sequences
"""

import argparse
import seaborn as sns
import pandas as pd

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', help='Input Coverage data per Window')
    args = parser.parse_args()

    in_f = args.i
    df = pd.read_csv(in_f, sep=" ", names=['sequence', 'start', 'end', 'depth'])
    print('first three lines of input file:')
    print(df.head(3))
     
    hist_plot = sns.histplot(data=df, x="start", y='depth') 
    fig = hist_plot.get_figure()
    fig.savefig('cov.png')

if __name__ == "__main__":
    main()
