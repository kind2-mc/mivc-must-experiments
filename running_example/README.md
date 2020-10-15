
# Running Example

This directory contains the three versions of the model used as running example,
and four scripts to compute the results described in the paper.

SystemModelV1.lus: Original system model
SystemModelV2.lus: Enhanced system model with `LIMIT = THRESH - (DELTA + S_ERROR)`
SystemModelV3.lus: Enhanced system model with `LIMIT = THRESH - (DELTA + 2.0*S_ERROR)`

Scripts:
run1.sh: Computes all MIVCs and the MUST set over assumptions and guarantees for SystemModelV1
run2.sh: Computes all MIVCs and the MUST set over assumptions and guarantees for SystemModelV2
run3.sh: Computes all MIVCs and the MUST set over assumptions and guarantees for SystemModelV3
run4.sh: Computes all MCSs over assumptions and guarantees for SystemModelV3

