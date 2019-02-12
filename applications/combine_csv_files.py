#!/usr/bin/env python3
# To run, type the following on the command line: python combine_csv_files.py inFiles outFiles/all_files_combined.csv
import pandas as pd
import glob
import os
import sys

# First command line argument after the script, namely, inFiles
input_path = sys.argv[1]
# Second command line argument after the script, namely, outFiles/all_files_combine.csv
output_file = sys.argv[2]

# Collect paths to all 100 input files into a list
all_input_files = glob.glob(os.path.join(input_path,'*.csv'))
print('Number of input files: {}'.format(len(all_input_files)))

# Create an empty list, into which we'll append 100 DataFrames
all_output_data_frames = []

# Loop / iterate over all 100 input files
# Read each 10-row file into a DataFrame
# Append the DataFrame into our list of DataFrames
for a_file in sorted(all_input_files):
    print(os.path.basename(a_file))
    data_frame = pd.read_csv(a_file)
    all_output_data_frames.append(data_frame)

# Combine / concatenate all of the 10-row DataFrames into one 1,000-row DataFrame
output_data_frame = pd.concat(all_output_data_frames)

# Print the number of rows and columns of the final DataFrame to the screen
nrows, ncols = output_data_frame.shape
print('Output DataFrame has {} rows and {} columns.'.format(nrows, ncols))

# Write the 1,000-row DataFrame to a new CSV file
# index=False means don't write the index column to the output file
output_data_frame.to_csv(output_file, index=False)
