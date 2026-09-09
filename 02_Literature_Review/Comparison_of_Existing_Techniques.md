# Comparison of Existing Techniques

## Face Anti-Spoofing and Liveness Detection

The reviewed studies use person-specific learning, gradient-based features, colour inversion, image-quality features and fine-grained patch recognition. These methods improve presentation-attack detection from different visual cues, but performance can still depend on image quality and capture conditions.

## Cross-Domain and Unseen-Attack Detection

Meta-learning, shuffled style assembly, test-time adaptation, feature alignment and ensemble stacking are used to reduce degradation when the testing domain differs from the training domain. These methods improve generalisation, but large domain shifts remain difficult. Test-time adaptation can also add inference overhead and latency.

## Deepfake and Adversarial Threats

Recent studies address spatial-temporal deepfakes, multiview manipulation and GAN-generated adversarial patches. These studies show that biometric systems must consider evolving synthetic-media and adversarial threats, not only traditional replay attacks.

## Privacy Protection

Privacy-focused studies use randomisation, frequency-domain protection, cancelable biometrics, encryption, template protection and secure computation. The main trade-off is that stronger protection can increase computational cost or reduce recognition performance.

## Practical Deployment

IoT, edge and multimodal systems demonstrate practical feasibility. However, added sensors, encryption, federated communication or blockchain can increase system complexity. This supports evaluating security, robustness and computational cost together.
