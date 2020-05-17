import os
import sys
import csv
import argparse

parser = argparse.ArgumentParser(description='Combine several CSV produced by collect.py into one (for comparison).')
parser.add_argument('csv_output_file', help='The CSV file to create.')
parser.add_argument('csv_input_files', help='The CSV files to combine.', nargs='+')

args = parser.parse_args()

output_file = args.csv_output_file
files = args.csv_input_files

results = {}

n = len(files)
for i in range(n):
    file = files[i]
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        first = True
        for row in reader:
            if first:
                first = False
                continue
            if not (row[0] in results):
                results[row[0]] = [(None, None) for _ in range(n)]
            results[row[0]][i] = [row[1],row[2]]


with open(output_file, 'w', newline='') as csv_f:

    writer = csv.writer(csv_f, delimiter=',')
    columns = ["Model name"]
    for file in files:
        columns += [file + " AT", file + " TT"]
    writer.writerow(columns)

    for i, k in enumerate(results):
        v = results[k]
        row = [k] + [item for sublist in v for item in sublist]
        writer.writerow(row)

