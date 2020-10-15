import os
import sys
import json
import csv
import argparse

parser = argparse.ArgumentParser(description='Collect the timing results from the outputs produced by run_benchmarks.py.')
parser.add_argument('kind2_results_dir', help='The directory created by run_benchmarks.py.')
parser.add_argument('csv_output_file', help='The CSV file to create.')

args = parser.parse_args()

input_dir = args.kind2_results_dir
output_file = args.csv_output_file

total_nb = 0
no_timeout_nb = 0
error_nb = 0

with open(output_file, 'w', newline='') as csv_f:

    writer = csv.writer(csv_f, delimiter=',')
    writer.writerow(["Model name", "Analysis time", "Total time"])

    for file in os.listdir(input_dir):
        if file.endswith(".log"):
            total_nb += 1
        if file.endswith(".txt"):
            no_timeout_nb += 1
            kind2_file = os.path.join(input_dir, file)
            log_file = os.path.join(input_dir, file[0:-4] + ".log")

            if not os.path.exists(log_file):
                total_nb += 1
                error_nb += 1
                print("Skipping {} because it has no associated log file.".format(file))
                continue

            with open(log_file, 'r') as log_f:
                logs = log_f.readlines()
                assert len(logs) >= 2
                status = logs[0].strip()
                assert status == "SUCCESS"
                total_time = int(logs[1].strip())

            success = False
            try:
                with open(kind2_file, 'r') as kind2_f:
                    output = json.loads(kind2_f.read())
                    
                for elt in output:
                    if "objectType" in elt and elt["objectType"] == "property":
                        if elt["answer"]["value"] == "valid":
                            success = True
                            analysis_time = int(elt["runtime"]["value"]*1000)
                        else:
                            success = False
                            break
            except:
                pass

            if not success:
                error_nb += 1
                print("Skipping {} because it has not been proved safe.".format(file))
                continue

            writer.writerow([file[0:-4], analysis_time/1000, total_time/1000])

print("Number of timeout: {}".format(total_nb - no_timeout_nb))
print("Number of errors: {}".format(error_nb))
print("Number of models kept: {}".format(no_timeout_nb - error_nb))
