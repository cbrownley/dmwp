#!/usr/bin/env python3
# To run, type the following on the command line: python parse_with_base_into_dict.py inFiles/data1.csv
import sys

# First command line argument after the script, namely, inFiles/data1.csv
input_path = sys.argv[1]

# Create an empty dictionary
my_data = {}

# Create a file_handle for reading lines from the file
with open(input_path, 'r', newline='') as file_handle:
    # Read the first line of the file, the header row
    header_row = file_handle.readline()
    # Strip whitespaces and newlines from the end of the line
    header_row = header_row.strip()
    # Split the line, a string, on commas to convert the line into a list
    header_row_list = header_row.split(',')
    # Loop / iterate over the values in the header row
    for index, column_heading in enumerate(header_row_list):
        # For each column heading, if it isn't already a key in the dictionary
        # then add it as a key and set the value as an empty list
        if header_row_list[index] not in my_data:
            my_data[header_row_list[index]] = []

    # Loop / iterate over the remaining rows in the file, the data rows
    for row in file_handle:
        # Strip whitespaces and newlines from the end of the line
        row = row.strip()
        # Split the line, a string, on commas to convert the line into a list
        row_list = row.split(',')
        # Loop / iterate over the values in the row
        for index, column_value in enumerate(row_list):
            # Append the value in row to the list associated with the key
            # that has the same index value, that is, use the index position
            # to ensure the values in a specific column are associated with
            # the correct column heading
            my_data[header_row_list[index]].append(row_list[index])

# Loop / iterate over the key-value pairs, that is, column headings and lists of
# column values, and print them to the screen
for column_heading, column_values in my_data.items():
    print('{}: {}'.format(column_heading,column_values))
