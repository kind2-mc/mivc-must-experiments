#!/bin/bash

python3 run_benchmarks.py --all benchmarks all_without
python3 collect.py all_without all_without.csv

python3 run_benchmarks.py --with_must_set --all benchmarks all_with
python3 collect.py all_with all_with.csv

python3 combine.py experiment2.csv all_without.csv all_with.csv
