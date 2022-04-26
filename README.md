# CoveragePlot
Generate coverage plots for genomes

# Dependencies
Python3 (tested with v3.8.1)  
	* pandas   
	* matplotlib  
	* numpy  
	* PIL (pillow)  
Samtools (tested with v1.9)
Bedtools (tested with v2.30.0)

# Running  
usage: plot_coverage.py [-h] [--maxNumSeqs MAXNUMSEQS | --seqs SEQS] [--bam BAM] [--winSize WINSIZE] [--img IMG] [--depth DEPTH] [--covLim COVLIM]

required arguments:
  --bam BAM                  BAM mapping file

optional arguments:
  --maxNumSeqs MAXNUMSEQS    Maximum number of sequences (returns MAXNUMSEQS largest sequences)
  --seqs SEQS                List of sequences to be used (cannot be run with the --maxNumSeqs option)
  --winSize WINSIZE          Windows size (default=10Kb)
  --img IMG                  List of images to concatenate
  --depth DEPTH              Depth file to use as input for generating plot
  --covLim COVLIM            Coverage limit to be displayed at the y axis (default=90% coverage quartile)
