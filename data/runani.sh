#!/bin/bash

# Activate the conda environment
source /home/mayank/miniconda3/etc/profile.d/conda.sh
conda activate aai

# Change directory
cd /home/mayank/Videos/sample

# Run the skani command
fastANI -q  /home/mayank/Downloads/ncbi_dataset_1/ncbi_dataset/data/GCA_028736055.1/g2.fna -r /home/mayank/Downloads/ncbi_dataset/ncbi_dataset/data/GCA_030433645.1/g1.fna -o Output.out

cat Output.out >> fasta/Output_fastani.out
cat fasta/Output_fastani.out

