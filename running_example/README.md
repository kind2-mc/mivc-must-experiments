
# Running Example

This directory contains the three versions of the model used as the running example,
and four scripts to compute the results described in the paper.

- SystemModelV1.lus: Original system model
- SystemModelV2.lus: Enhanced system model with `LIMIT = THRESH - (DELTA + S_ERROR)`
- SystemModelV3.lus: Enhanced system model with `LIMIT = THRESH - (DELTA + 2.0*S_ERROR)`

Scripts:
- Example 1 (page 7)
  - run1.sh: Computes an approximate MIVC over assumptions and guarantees for SystemModelV1
  - run2.sh: Computes an (exact) MIVC over assumptions and guarantees for SystemModelV1
  - run3.sh: Computes all MIVCs over assumptions and guarantees for SystemModelV1
- Example 2 (page 8)
  - run4.sh: Computes all MIVCs and the MUST set over assumptions and guarantees for SystemModelV2
  - run5.sh: Computes all MIVCs and the MUST set over assumptions and guarantees for SystemModelV3
- Example 3 (page 11)
  - run6.sh: Computes all MCSs over assumptions and guarantees for SystemModelV3

Notice that the result computed with `run1.sh` may correspond to a MIVC or
any superset depending on the invariants found in a particular run.


