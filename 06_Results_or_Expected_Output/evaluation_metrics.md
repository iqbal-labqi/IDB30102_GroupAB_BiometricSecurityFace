# Evaluation Metrics

The proposed framework will be compared against a standard,
unhardened baseline model (e.g., standard FaceNet) using the same
OULU-NPU dataset protocols and experimental conditions, in line with
Section 3.9 of the proposal.

| Metric | Formula / Definition | Purpose |
|---|---|---|
| APCER (Attack Presentation Classification Error Rate) | Proportion of attack presentations incorrectly classified as genuine (bona fide) | Measures how often the system fails to catch a spoofing attempt |
| BPCER (Bona Fide Presentation Classification Error Rate) | Proportion of genuine presentations incorrectly classified as attacks | Measures how often the system wrongly rejects a real user |
| ACER (Average Classification Error Rate) | (APCER + BPCER) / 2 | Provides a single balanced error measure between the two error types |
| Execution Latency | Wall-clock processing time per authentication attempt (milliseconds) | Measures whether the framework is efficient enough for edge deployment |

## Testing Environments

Metrics will be recorded separately for:
- **Standard workstation environment** — to establish baseline
  algorithmic performance without hardware constraints.
- **Edge/resource-constrained environment** — to evaluate whether the
  added privacy-preserving mechanism keeps latency within practical
  limits for real deployment (per Section 1.6 scope).

## Evaluation Protocol

Consistent with OULU-NPU's four evaluation protocols, error rates
will be assessed across variations in illumination, capture device,
and presentation attack instrument, to directly test the framework's
cross-domain generalization claim (RO3).

## Comparison Basis

Lower APCER/BPCER/ACER values indicate stronger presentation attack
detection. Latency will be interpreted alongside these error rates,
since an improvement in detection accuracy that comes at the cost of
excessive processing time would not satisfy the research's
lightweight, edge-deployment goal.
