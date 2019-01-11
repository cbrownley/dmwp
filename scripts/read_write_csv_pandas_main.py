#!/usr/bin/env python3
import pandas as pd
import sys

# On Mac, while inside the scripts folder, run this script from the command line with the following command:
# python read_write_csv_pandas_main.py ../inFiles/randomuser5000.csv ../outFiles/output_from_script_with_main.csv

def capture_command_line_arguments():
    # input_file is the first command line argument after the script name
    input_file = sys.argv[1]
    # output_file is the second command line argument after the script name
    output_file = sys.argv[2]
    return input_file, output_file


def read_infile(infilepath):
    # read data from CSV file into a DataFrame named df
    df = pd.read_csv(infilepath)
    return df


def process_file(df, row_condition):
    # create a new DataFrame named males that contains the rows from the original
    # DataFrame where gender equals female
    df = df.loc[row_condition,:]
    return df


def write_outfile(df, outfilepath):
    # write data to CSV file
    df.to_csv(outfilepath, index=False)




def main():
    # capture the input and output filenames from the command line
    input_file, output_file = capture_command_line_arguments()
    # read the input file into a DataFrame
    df = read_infile(input_file)
    # create a new DataFrame that contains data for females
    females = process_file(df, df.gender == 'female')
    # write the females DataFrame to the output file
    write_outfile(females, output_file)
    print('Finished writing file.')

main()
