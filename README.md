# MIVC-MUST Experiments

This repository serves as supporting material for the paper [1]. The new features described in the paper are available at https://github.com/kind2-mc/kind2/tree/mivc-must-mcs-20. You will need to compile the version of Kind 2 available there to run the scripts below. The scripts of this repository require Python >= 3.5, and assume that the `kind2` binary is located in the root of this repository.

The `running_example` directory contains the model used as running example, and the scripts necessary to compute the results described in the paper.

The set of bechmarks used in the experimental evaluation have been collected from [2].

Run `experiment1.sh` to get the results for the first experiment. This will create a CSV file (`experiment1.csv`) with the runtimes for the computation of a single MIVC (`one_without.csv`) and the computation of both a MIVC and its MUST elements (`one_with.csv`) over the set of bechmarks.

Run `experiment2.sh` to get the results for the second experiment. This will create a CSV file (`experiment2.csv`) with the runtimes for the computation of all the MIVCs using the MUST set optimization (`all_with.csv`), and without the MUST set optimization (`all_without.csv`) over the set of bechmarks.

A description of the options for the computation of MIVCs and the MUST set is available at:
https://github.com/kind2-mc/kind2/tree/mivc-must-mcs-20/doc/usr/source/9_other/10_inductive_validity_core.rst

A description of the options for the computation of MCSs is available at:
https://github.com/kind2-mc/kind2/tree/mivc-must-mcs-20/doc/usr/source/9_other/11_minimal_cut_set.rst

For information about other options in Kind 2, please see Kind 2 user documentation: https://kind.cs.uiowa.edu/kind2_user_doc/

[1] Merit and Blame Assignment with Kind 2. D. Larraz, M. Laurent, and C. Tinelli.

[2] Efficient generation of all minimal inductive validity cores. E. Ghassabani, M. W. Whalen, and A. Gacek. FMCAD 2017.
