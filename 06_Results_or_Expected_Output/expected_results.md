# Expected Results

The proposed framework will be evaluated against a standard,
unhardened baseline model (e.g., standard FaceNet) to determine
whether it provides better protection against facial presentation
attacks while remaining suitable for lightweight, edge-oriented
deployment.

## Evaluation Focus

- Presentation attack detection accuracy (APCER, BPCER, ACER)
- Processing efficiency (execution latency)
- Cross-domain generalization across OULU-NPU's evaluation protocols
  (varying illumination, capture devices, and attack instruments)
- Performance on both standard workstation and edge computing
  environments

## Expected Comparison

| Aspect | Baseline | Proposed Framework |
|---|---|---|
| APCER / BPCER / ACER | Reference error rates on unhardened model | Expected to be lower, reflecting improved cross-domain liveness detection |
| Execution Latency | Reference processing time | Expected to remain within a reasonable margin of the baseline, demonstrating that privacy protection does not introduce excessive overhead |

## Interpretation Criteria

- Lower error rates are expected to indicate better spoof detection
  performance than the baseline.
- Reasonable execution latency (comparable to or only marginally
  higher than the baseline) will indicate that the added
  privacy-preserving mechanism remains suitable for lightweight,
  edge-device deployment.

## Note

No final performance values are reported here, as the proposed
framework has not yet been implemented and tested. This document
describes the evaluation criteria and expected direction of results,
consistent with Sections 3.9 and 3.11 of the proposal report. Actual
experimental results will replace this content once testing is
complete.
