#!/usr/bin/env python3
# To run, type the following on the command line: python eligible_for_medicare.py inFiles outFiles/all_medicare_eligibles.csv
from datetime import date
import pandas as pd
import glob
import os
import sys

# First command line argument after the script, namely, inFiles
input_path = sys.argv[1]
# Second command line argument after the script, namely, outFiles/all_medicare_eligibles.csv
output_file = sys.argv[2]

def calculate_age(born):
    """This function calculates a person's age (in years) based on
    today's date and his or her date of birth"""
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


# Collect paths to all 100 input files into a list
all_input_files = glob.glob(os.path.join(input_path,'*.csv'))
print('Number of input files: {}'.format(len(all_input_files)))

# Create an empty list, into which we'll append DataFrames
all_output_data_frames = []

# Loop / iterate over all 100 input files
# Read each 10-row file into a DataFrame
# Append DataFrames of Medicare-eligible people into our list of DataFrames
for a_file in sorted(all_input_files):
    print(os.path.basename(a_file))
    data_frame = pd.read_csv(a_file)

    # convert date of birth (dob) column to datetime
    data_frame.dob = pd.to_datetime(data_frame.dob)
    # calculate the person's age in years and add the value as a column
    data_frame['age'] = data_frame.dob.apply(lambda x: calculate_age(x))

    # extract rows where age >= 65 into a new DataFrame
    eligibles = data_frame.loc[data_frame.age >= 65,:]

    # if the DataFrame isn't empty; that is, if it does have data
    if not eligibles.empty:
        # then append the DataFrame into the list of output DataFrames
        all_output_data_frames.append(eligibles)

# Combine / concatenate all of the output DataFrames into one DataFrame
output_data_frame = pd.concat(all_output_data_frames)

# Print the number of rows and columns of the final DataFrame to the screen
nrows, ncols = output_data_frame.shape
print('Output DataFrame has {} rows and {} columns.'.format(nrows, ncols))

# Write the DataFrame of Medicare-eligible people to a new CSV file
# index=False means don't write the index column to the output file
output_data_frame.to_csv(output_file, index=False)
