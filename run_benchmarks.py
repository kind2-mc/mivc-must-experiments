import os
import sys
import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description='Run some benchmarks for IVC computation.')
parser.add_argument('models_dir', help='The directory containing the models.')
parser.add_argument('output_dir', help='The directory that will receive the Kind2 outputs.')
parser.add_argument('--kind2_path', default="./kind2")
parser.add_argument('--approximate', action="store_true")
parser.add_argument('--all', action="store_true")
parser.add_argument('--with_must_set', action="store_true")
parser.add_argument('--timeout', type=int, default=1600)
parser.add_argument('--solver', choices=["Z3", "CVC4", "Yices", "Yices2"], default='Z3')
parser.add_argument('--minimize', action="store_true")

args = parser.parse_args()

KIND2 = args.kind2_path
COMPUTE_APPROXIMATE_CORE = args.approximate
COMPUTE_ALL_CORES = args.all
MUST_SET_OPTIMISATION = args.with_must_set
SMT_SOLVER = args.solver
TIMEOUT = args.timeout
MINIMIZE = args.minimize

input_dir = args.models_dir
output_dir = args.output_dir

def current_ms_time():
    return int(round(time.time() * 1000))

def b2str(b):
    return "true" if b else "false"

args = ["--ivc", "true",
        "--ivc_approximate", b2str(COMPUTE_APPROXIMATE_CORE),
        "--ivc_all", b2str(COMPUTE_ALL_CORES),
        "--compositional", "true",
        "--smt_solver", SMT_SOLVER,
        "--ivc_uc_timeout", "30",
        "--timeout", str(TIMEOUT),
        "--minimize_program", "valid_lustre" if MINIMIZE else "no",
        "-json"
    ]

if MUST_SET_OPTIMISATION:
    args += ["--ivc_must_set", "true"]
else:
    args += ["--ivc_disable_must_opt", "true"]

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for file in os.listdir(input_dir):
    if file.endswith(".lus"):
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_dir, file + ".txt")
        log_file = os.path.join(output_dir, file + ".log")
        minimized_dir = os.path.join(output_dir, file[0:-4])
        t = current_ms_time()
        print("Running on {}...".format(file))
        try:
            with open(output_file, 'w') as output_f:
                subprocess.run([KIND2] + args + ["--ivc_output_dir", minimized_dir] + [input_file],
                    stdout=output_f,
                    stderr=output_f)
                    #,timeout=TIMEOUT)
            t = current_ms_time() - t
            if t >= TIMEOUT*1000:
                raise RuntimeError()
            print("Finished in {}ms.".format(str(t)))
            with open(log_file, 'w') as log_f:
                log_f.write("SUCCESS\n{}\n".format(str(t)))
        except (subprocess.TimeoutExpired, RuntimeError) as e:
            print("Timeout.")
            if os.path.exists(output_file):
                os.remove(output_file)
            with open(log_file, 'w') as log_f:
                log_f.write("TIMEOUT\n")
