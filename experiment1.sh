#!/bin/bash

python3 run_benchmarks.py benchmarks one_without
python3 collect.py one_without one_without.csv

python3 run_benchmarks.py --with_must_set benchmarks one_with
python3 collect.py one_with one_with.csv

python3 combine.py experiment1.csv one_without.csv one_with.csv
