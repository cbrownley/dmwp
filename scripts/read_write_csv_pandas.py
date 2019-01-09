#!/usr/bin/env python3
import pandas as pd
import sys

# On Mac, while inside the scripts folder, run this script from the command line with the following command:
# python read_write_csv_pandas.py ../inFiles/randomuser5000.csv ../outFiles/output_from_script.csv

# input_file is the first command line argument after the script name
input_file = sys.argv[1]

# output_file is the second command line argument after the script name
output_file = sys.argv[2]

# read data from CSV file into a DataFrame named df
df = pd.read_csv(input_file)

# create a new DataFrame named males that contains the rows from the original
# DataFrame where gender equals female
females = df.loc[df.gender == 'female',:]

# write data to CSV file
females.to_csv(output_file, index=False)
print('Wrote file.')
