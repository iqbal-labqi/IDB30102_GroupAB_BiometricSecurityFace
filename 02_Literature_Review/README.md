# 02 — Literature Review

## Purpose

This folder contains the supporting literature-review materials for Chapter 2. The materials are based on the group's existing literature review and are organised according to the latest lecturer requirement: a focused comparison of approximately 10 existing approaches and approximately 10 existing technologies/tools, together with the wider analysis used to develop the research gap.

## 1. Literature Review Analysis

The selected literature covers five main areas:

1. Facial recognition and face anti-spoofing
2. Cross-domain and unseen attack detection
3. Deepfakes and adversarial attacks
4. Privacy and protection of facial biometric data
5. Multimodal and practical facial biometric systems

The full paper-by-paper findings remain part of the group's existing literature-review evidence. The proposal table is intentionally condensed to the selected approaches and technologies requested by the lecturer.

## 2. Comparison of Existing Approaches

| No. | Existing Approach | Main Purpose | Main Finding / Limitation | Relevance |
|---|---|---|---|---|
| 1 | Person-specific Siamese Network | Identity-aware spoof detection | Improves detection but requires a genuine reference image. | Practical liveness detection. |
| 2 | Learnable Gradient Operator | Fine-grained PAD feature extraction | Improves PAD but remains affected by domain differences. | Visual PAD features. |
| 3 | Multi-Scale Colour Inversion Dual-Stream CNN | Colour and multi-scale spoof detection | Improves detection; unseen attacks remain challenging. | Complementary visual cues. |
| 4 | Image-Quality Features with Deep Learning | Uses image-quality information for PAD | Useful but affected by captured image quality. | Practical PAD evaluation. |
| 5 | Fine-Grained Patch Recognition | Local spoof-related feature detection | Improves unseen spoof detection; may miss global cues. | Cross-domain PAD. |
| 6 | Meta Pattern Learning | Learns transferable spoofing patterns | Improves generalisation; large domain shifts remain difficult. | Cross-domain liveness detection. |
| 7 | Shuffled Style Assembly Network | Separates style/content for domain generalisation | Improves generalisation but deployment distributions can differ. | Domain robustness. |
| 8 | Multi-Domain Feature Alignment | Reduces feature differences between domains | Improves generalisation; target-domain differences remain. | Domain adaptation/generalisation. |
| 9 | Test-Time Adaptation | Adapts a pretrained PAD model to target data | Can improve target performance but adds computation and latency. | Robustness-efficiency trade-off. |
| 10 | Multimodal Face Anti-Spoofing | Combines RGB, infrared and depth information | Improves robustness but needs specialised sensors and data. | Comparison with a simpler edge design. |

## 3. Comparison of Existing Technologies / Tools

| No. | Technology / Tool | Use in Previous Studies | Main Consideration |
|---|---|---|---|
| 1 | Convolutional Neural Network (CNN) | Face anti-spoofing, recognition and multimodal biometrics. | Effective feature learning; performance depends on data and conditions. |
| 2 | Siamese Network | Person-specific face spoofing detection. | Requires suitable reference information. |
| 3 | Vision Transformer (ViT) | Multimodal face anti-spoofing. | Strong representation learning but can require more resources. |
| 4 | Masked Autoencoder (MAE) | Representation learning in multimodal PAD. | Requires suitable multimodal data and computation. |
| 5 | Generative Adversarial Network (GAN) | Privacy-related transformation and adversarial attack generation. | Useful but may increase complexity. |
| 6 | Federated Learning | Local training without centralising raw facial data. | Reduces direct data exposure but adds communication overhead. |
| 7 | Blockchain | Decentralised facial data management/protection. | Adds storage and processing overhead. |
| 8 | Secure Multi-Party Computation | Privacy-preserving processing. | Strong privacy but higher processing/communication cost. |
| 9 | Frequency-Domain Processing | Privacy protection of facial representations. | Privacy can be balanced against recognition utility. |
| 10 | Raspberry Pi 5 / ESP32-S3 | Practical edge facial-recognition implementation. | Demonstrates deployment feasibility under resource constraints. |

## 4. Research Gap Analysis

### 4.1 Cross-domain presentation attack detection

Meta-learning, patch-level recognition, style assembly, feature alignment and test-time adaptation improve generalisation, but substantial differences between training and target conditions can still affect performance. This supports the proposed focus on cross-domain liveness detection.

### 4.2 PAD and biometric privacy are commonly studied separately

PAD research mainly addresses whether a presentation is genuine or an attack, while privacy research focuses on facial images, features or templates. The existing studies therefore provide useful individual solutions, but fewer studies address both concerns together in one practical authentication framework.

### 4.3 Privacy mechanisms can increase computational or communication requirements

Encryption, secure multi-party computation, blockchain and federated learning provide different forms of privacy protection, but their processing, storage or communication requirements can be important for edge deployment.

### 4.4 Practical recognition systems do not always evaluate complete biometric security

Application-oriented systems can report high recognition accuracy without fully evaluating cross-domain spoofing and privacy together. This creates a difference between recognition performance and the requirements of a secure, private and lightweight biometric authentication system.

### 4.5 Main research gap

The main gap is the limited integration of cross-domain presentation attack detection, biometric template privacy and computational efficiency within a single practical framework. This is an integration and evaluation gap rather than a claim that cross-domain PAD or privacy protection has not been studied.

## 5. Methods and Algorithms Identified

- CNN-based face anti-spoofing
- Person-specific Siamese Network
- Learnable Gradient Operator
- Meta Pattern Learning
- Fine-grained patch recognition
- Shuffled Style Assembly Network
- Multi-Domain Feature Alignment
- Test-Time Adaptation
- Spatial and temporal deep learning
- Multi-view and pose features
- Template protection / BioCrypto
- Frequency-domain privacy protection
- Extensible privacy-preserving feature extraction
- Federated learning
- Blockchain with GAN obfuscation
- Secure multi-party computation
- Multimodal feature learning

## 6. Relevant Datasets and Data Sources

The reviewed studies use benchmark, public and application-oriented datasets. Relevant datasets identified in the existing literature include CASIA-FASD, SiW, Replay-Attack, OULU-NPU, CASIA-MFSD, MSU-MFSD, LFW, MOBIO, FFIW-10K, FaceForensics++, OpenForensics, CVL, IITK, CASIA-Face-v5, FERET, CelebA, HDU, CFP-FP, AgeDB-30, IJB-C, WMCA, CASIA-SURF and CASIA-SURF CeFA.

For the proposed research, dataset selection should support a clear comparison between source and target conditions and provide suitable genuine and attack samples for presentation attack detection. The exact final dataset choice remains consistent with the scope and methodology stated in Chapter 1.

## 7. Evaluation Metrics Identified

| Metric | Use | Relevance |
|---|---|---|
| ACER | Overall PAD error. | Core PAD evaluation. |
| APCER | Error for presentation attacks. | Measures attack-detection performance. |
| BPCER | Error for bona fide presentations. | Measures false rejection of genuine presentations. |
| HTER | PAD error measure used in related studies. | Supporting comparison metric. |
| EER | False acceptance/rejection balance in biometric evaluation. | Supporting biometric comparison. |
| Accuracy / Precision / Recall / F1-score | General classification and recognition evaluation. | Supporting context where appropriate. |
| AUC / ROC-AUC | Discrimination performance. | Useful where ROC-based evaluation is used. |
| Recognition accuracy / TAR@FAR | Facial recognition utility. | Helps determine whether privacy protection affects recognition. |
| Execution latency / inference time | Computational efficiency. | Directly relevant to lightweight deployment. |

## 8. Link to Chapter 2 Written Report

The GitHub materials support the written Chapter 2 by providing the underlying comparison of existing approaches, technologies, methods, datasets and evaluation metrics. The written report remains the main academic discussion, while this folder provides the structured supporting evidence used to develop the synthesis and research gap.

## 9. References

The references used for this supporting material are the same verified references already used by the group in Chapter 2. No new research direction is introduced through this GitHub material.
