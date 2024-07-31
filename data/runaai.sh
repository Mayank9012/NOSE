#!/bin/bash

# Change directory
cd /home/mayank/Videos/sample

# Activate the conda environment
source /home/mayank/miniconda3/etc/profile.d/conda.sh
conda activate aai

# Run the ezaai command with the full path to the MMSeqs2 binary
/home/mayank/miniconda3/envs/aai/bin/ezaai calculate -i db/ -j db/ -o out/aai3.tsv

#output
cat out/aai3.tsv

