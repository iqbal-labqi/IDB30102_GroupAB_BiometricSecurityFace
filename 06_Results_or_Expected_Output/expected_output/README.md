# Expected Output

For each authentication attempt, the proposed system is expected to
produce:

1. **Genuine or spoof classification** — output of the presentation
   attack detection stage (Deep Learning-based PAD model).
2. **Authentication decision** — final Access Granted / Access Denied
   result following face matching.
3. **Presentation attack detection results** — per-sample APCER/BPCER
   contribution, used to compute aggregate error rates.
4. **Evaluation metric results** — APCER, BPCER, and ACER values
   computed across the OULU-NPU test protocols, compared against the
   baseline model.
5. **Execution latency measurements** — per-stage and total
   processing time (milliseconds), recorded on both standard
   workstation and edge computing environments.

## Output Format

Results will be logged per test run (e.g., CSV or JSON) capturing:
   dataset protocol used, sample ID, ground-truth label (genuine/attack),
   predicted label, and per-stage latency — to support the comparative
   analysis described in Section 3.1.5 (Statistical Analysis) of the
   proposal.

## Status

Actual experimental results will be added to this folder after the
implementation and testing stages are completed, replacing the
expected values described in `expected_results.md`.
