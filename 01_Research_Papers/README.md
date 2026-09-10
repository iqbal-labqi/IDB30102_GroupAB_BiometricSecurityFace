# 01 — Research Papers

This folder contains the key research papers used to support Chapter 2 of the research proposal.

The research-paper PDFs are not uploaded to this repository. The information below is a structured summary of the selected literature used by the group.

## Required Paper Information

For each selected study, the following information is recorded:

- Paper Title
- Author(s)
- Year
- Research Problem
- Method / Technique
- Dataset / Tools
- Main Findings
- Limitation
- Relevance to the Proposed Research
- DOI / Official Link

## Key Papers Used in Chapter 2

## 1. Learning Meta Pattern for Face Anti-Spoofing

**Authors / Year:** Cai et al. (2022)

**Research Problem:** Cross-domain face anti-spoofing under changing domains.

**Method / Technique:** Meta Pattern Learning.

**Dataset / Tools:** Public FAS datasets.

**Main Findings:** Improved generalisation compared with existing methods.

**Limitation:** Performance can still drop when the testing domain is very different.

**Relevance to Proposed Research:** Supports cross-domain liveness detection.

**DOI / Official Link:** https://doi.org/10.1109/TIFS.2022.3158551

---

## 2. PatchNet: A Simple Face Anti-Spoofing Framework via Fine-Grained Patch Recognition

**Authors / Year:** Wang et al. (2022)

**Research Problem:** Unseen spoofing and domain-generalisation problems.

**Method / Technique:** Fine-grained patch recognition.

**Dataset / Tools:** Public face anti-spoofing datasets.

**Main Findings:** Improved detection of unseen spoofing attacks.

**Limitation:** Local features may not capture all information from the whole face.

**Relevance to Proposed Research:** Supports robust presentation attack detection.

**DOI / Official Link:** https://doi.org/10.1109/CVPR52688.2022.01964

---

## 3. Domain Generalization via Shuffled Style Assembly for Face Anti-Spoofing

**Authors / Year:** Wang et al. (2022)

**Research Problem:** Domain shift in face anti-spoofing.

**Method / Technique:** Shuffled Style Assembly Network (SSAN).

**Dataset / Tools:** Existing FAS datasets and benchmark data.

**Main Findings:** Improved generalisation across datasets.

**Limitation:** Dataset differences can still affect performance in real environments.

**Relevance to Proposed Research:** Supports domain generalisation.

**DOI / Official Link:** https://doi.org/10.1109/CVPR52688.2022.00409

---

## 4. Privacy-Preserving Face Recognition in the Frequency Domain

**Authors / Year:** Wang et al. (2022)

**Research Problem:** Protection of facial information during recognition.

**Method / Technique:** Frequency-domain channel selection and fast masking.

**Dataset / Tools:** Benchmark face datasets.

**Main Findings:** Provided privacy protection with a limited decrease in recognition accuracy.

**Limitation:** More privacy protection can reduce recognition performance.

**Relevance to Proposed Research:** Supports lightweight privacy protection.

**DOI / Official Link:** https://doi.org/10.1609/aaai.v36i3.20157

---

## 5. Person-Specific Face Spoofing Detection Based on a Siamese Network

**Authors / Year:** Pei et al. (2023)

**Research Problem:** Face spoofing detection using identity-specific information.

**Method / Technique:** Person-specific Siamese Network.

**Dataset / Tools:** SiW, CASIA-FASD and Replay-Attack.

**Main Findings:** Using user identity information improved spoofing detection.

**Limitation:** Requires a genuine reference image for each user.

**Relevance to Proposed Research:** Supports identity-aware liveness detection while showing an enrolment dependency.

**DOI / Official Link:** https://doi.org/10.1016/j.patcog.2022.109148

---

## 6. A Learnable Gradient Operator for Face Presentation Attack Detection

**Authors / Year:** Wang et al. (2023)

**Research Problem:** Fine-grained feature extraction for PAD.

**Method / Technique:** Learnable Gradient Operator Network.

**Dataset / Tools:** Replay-Attack, CASIA-FASD, OULU-NPU and SiW.

**Main Findings:** Improved PAD performance on benchmark datasets.

**Limitation:** Cross-domain differences can still affect results.

**Relevance to Proposed Research:** Supports gradient-based PAD features.

**DOI / Official Link:** https://doi.org/10.1016/j.patcog.2022.109146

---

## 7. Face Spoofing Detection Based on Multi-Scale Color Inversion Dual-Stream Convolutional Neural Network

**Authors / Year:** Shu et al. (2023)

**Research Problem:** Spoof detection under varying visual conditions.

**Method / Technique:** Multi-scale colour inversion dual-stream CNN.

**Dataset / Tools:** Public face anti-spoofing datasets.

**Main Findings:** Improved detection compared with single-stream approaches.

**Limitation:** Unseen attacks and difficult lighting conditions remain challenging.

**Relevance to Proposed Research:** Supports complementary visual features for liveness detection.

**DOI / Official Link:** https://doi.org/10.1016/j.eswa.2023.119988

---

## 8. FASS: Face Anti-Spoofing System Using Image Quality Features and Deep Learning

**Authors / Year:** Solomon and Cios (2023)

**Research Problem:** Face anti-spoofing using image-quality information.

**Method / Technique:** FASS ensemble system.

**Dataset / Tools:** Replay-Attack, CASIA-MFSD, MSU-MFSD, OULU-NPU and SiW.

**Main Findings:** Performed better than several existing PAD methods.

**Limitation:** Results depend on captured image quality.

**Relevance to Proposed Research:** Supports practical PAD using image-quality features.

**DOI / Official Link:** https://doi.org/10.3390/electronics12102199

---

## 9. Test-Time Adaptation for Robust Face Anti-Spoofing

**Authors / Year:** Huang et al. (2023)

**Research Problem:** Performance degradation in unseen target domains.

**Method / Technique:** Activation-based test-time adaptation.

**Dataset / Tools:** Benchmark TTA-FAS data.

**Main Findings:** Improved performance over baseline TTA methods.

**Limitation:** Online updates add computational overhead and latency.

**Relevance to Proposed Research:** Supports cross-domain adaptation while highlighting efficiency concerns.

**DOI / Official Link:** https://proceedings.bmvc2023.org/379/

---

## 10. Multi-Domain Feature Alignment for Face Anti-Spoofing

**Authors / Year:** Zhang and Nie (2023)

**Research Problem:** Feature distribution differences across domains.

**Method / Technique:** Multi-Domain Feature Alignment (MADG).

**Dataset / Tools:** CASIA-MFSD, Replay-Attack, MSU-MFSD and OULU-NPU.

**Main Findings:** Improved cross-domain generalisation.

**Limitation:** Mainly focuses on feature alignment between domains.

**Relevance to Proposed Research:** Supports cross-domain PAD.

**DOI / Official Link:** https://doi.org/10.3390/s23084077

---

## 11. Comprehensive Vulnerability Evaluation of Face Recognition Systems to Template Inversion Attacks via 3D Face Reconstruction

**Authors / Year:** Shahreza and Marcel (2023)

**Research Problem:** Security risk of stored face templates.

**Method / Technique:** GaFaR / geometry-aware reconstruction approach.

**Dataset / Tools:** LFW and MOBIO.

**Main Findings:** Reconstructed faces could be used to attack recognition systems.

**Limitation:** Requires access to the template embedding.

**Relevance to Proposed Research:** Supports the need to protect stored biometric representations.

**DOI / Official Link:** https://doi.org/10.1109/TPAMI.2023.3312123

---

## 12. An Attack on Facial Soft-Biometric Privacy Enhancement

**Authors / Year:** Osorio-Roig et al. (2022)

**Research Problem:** Attacks against privacy-enhanced facial representations.

**Method / Technique:** Attack modelling on privacy-enhanced face recognition.

**Dataset / Tools:** Face benchmark datasets.

**Main Findings:** Showed that some privacy-enhanced representations can reveal sensitive attributes.

**Limitation:** Privacy protection may not prevent attribute inference.

**Relevance to Proposed Research:** Supports stronger protection of facial representations.

**DOI / Official Link:** https://doi.org/10.1109/TBIOM.2022.3172724

---

## 13. A Secure Face Recognition for IoT-Enabled Healthcare System

**Authors / Year:** Sardar et al. (2023)

**Research Problem:** Secure biometric recognition for constrained IoT environments.

**Method / Technique:** Cancelable biometrics and BioCrypto-based template protection.

**Dataset / Tools:** CVL, IITK, CASIA-Face-v5 and FERET.

**Main Findings:** Maintained strong accuracy while meeting protection requirements.

**Limitation:** Encryption increases computation on constrained hardware.

**Relevance to Proposed Research:** Supports secure biometric deployment on constrained devices.

**DOI / Official Link:** https://doi.org/10.1145/3534122

---

## 14. Privacy-Preserving Face Recognition Method Based on Extensible Feature Extraction

**Authors / Year:** Hu et al. (2024)

**Research Problem:** Privacy-preserving recognition with attention to feature extraction and efficiency.

**Method / Technique:** Extensible feature extraction for privacy-preserving recognition.

**Dataset / Tools:** Face recognition benchmark datasets.

**Main Findings:** Maintained high recognition accuracy and improved efficiency compared with baseline methods.

**Limitation:** Encryption still adds computational cost.

**Relevance to Proposed Research:** Supports integrating privacy with computational efficiency.

**DOI / Official Link:** https://doi.org/10.1016/j.jvcir.2024.104140

---

## 15. Privacy-Preserving Face Recognition Method Based on Randomization and Local Feature Learning

**Authors / Year:** Huang et al. (2024)

**Research Problem:** Protection of facial information through randomisation and local feature learning.

**Method / Technique:** Random convolution with self-learning batch normalisation.

**Dataset / Tools:** LFW, CelebA and HDU.

**Main Findings:** Scrambled images achieved recognition results close to normal images.

**Limitation:** Server-side trust assumption remains.

**Relevance to Proposed Research:** Supports privacy protection through feature transformation.

**DOI / Official Link:** https://doi.org/10.3390/jimaging10030059

---

## 16. Maintaining Privacy in Face Recognition Using Federated Learning Method

**Authors / Year:** Woubie et al. (2024)

**Research Problem:** Privacy risks from centralised facial data training.

**Method / Technique:** Federated learning with and without secure aggregation.

**Dataset / Tools:** Public face datasets partitioned across simulated clients.

**Main Findings:** Matched centralised accuracy while keeping raw data on device.

**Limitation:** Communication overhead and uneven client data remain concerns.

**Relevance to Proposed Research:** Supports privacy-aware training while showing efficiency trade-offs.

**DOI / Official Link:** https://doi.org/10.1109/ACCESS.2024.3373691

---

## 17. Toward Robust and Privacy-Enhanced Facial Recognition: A Decentralized Blockchain-Based Approach with GANs and Deep Learning

**Authors / Year:** Ghani et al. (2024)

**Research Problem:** Privacy protection and decentralised facial data management.

**Method / Technique:** Blockchain with GAN-based obfuscation and clustering.

**Dataset / Tools:** Custom facial dataset.

**Main Findings:** Improved privacy without major accuracy loss.

**Limitation:** Blockchain adds latency and storage overhead.

**Relevance to Proposed Research:** Shows the privacy benefit and complexity cost of decentralised protection.

**DOI / Official Link:** https://doi.org/10.3934/mbe.2024184

---

## 18. Privacy-Preserving Deepfake Face Image Detection

**Authors / Year:** Chen et al. (2023)

**Research Problem:** Private deepfake detection without exposing input information.

**Method / Technique:** Secure DeepFake Detection Network using secret sharing and secure multi-party computation.

**Dataset / Tools:** FaceForensics++, Celeb-DF and DFDNet.

**Main Findings:** High detection performance while preserving cryptographic privacy.

**Limitation:** Secure computation increases processing and communication cost.

**Relevance to Proposed Research:** Supports privacy-preserving processing while highlighting latency concerns.

**DOI / Official Link:** https://doi.org/10.1016/j.dsp.2023.104233

---

## 19. Rethinking Vision Transformer and Masked Autoencoder in Multimodal Face Anti-Spoofing

**Authors / Year:** Yu et al. (2024)

**Research Problem:** Robust multimodal face anti-spoofing.

**Method / Technique:** Vision Transformer, Masked Autoencoder and adaptive multimodal processing.

**Dataset / Tools:** WMCA, CASIA-SURF and CASIA-SURF CeFA.

**Main Findings:** Improved robustness and reduced training cost.

**Limitation:** Requires multimodal datasets and specialised sensors.

**Relevance to Proposed Research:** Shows robustness benefits of multimodal information but added hardware complexity.

**DOI / Official Link:** https://doi.org/10.1007/s11263-024-02055-1

---

## 20. Enhancing Biometric Authentication Through Multimodal Approach Combining Face and Fingerprint Recognition Using CNN

**Authors / Year:** Gimba et al. (2025)

**Research Problem:** Improving authentication using multiple biometric sources.

**Method / Technique:** CNN-based multimodal fusion.

**Dataset / Tools:** Georgia Tech, Essex, FVC2000 and SOCOFing.

**Main Findings:** Reduced FAR/FRR compared with single-biometric approaches, although accuracy was slightly lower.

**Limitation:** Requires two biometric sources and additional hardware/data.

**Relevance to Proposed Research:** Supports multimodal security while highlighting resource requirements.

**DOI / Official Link:** https://doi.org/10.1007/s10791-025-09775-z

---

## 21. A Hybrid Deep Learning Framework for Deepfake Detection Using Temporal and Spatial Features

**Authors / Year:** Zafar et al. (2025)

**Research Problem:** Deepfake detection under spatial and temporal manipulation.

**Method / Technique:** Enhanced EfficientNet-B0 with Temporal CNN.

**Dataset / Tools:** FFIW-10K.

**Main Findings:** Reported strong training and testing accuracy.

**Limitation:** Performance may drop for occluded, low-resolution or blurred faces.

**Relevance to Proposed Research:** Supports consideration of diverse manipulated inputs.

**DOI / Official Link:** https://doi.org/10.1109/ACCESS.2025.3566008

---

## 22. Unmasking Facial Deepfakes: A Robust Multiview Detection Framework for Natural Images

**Authors / Year:** Belguesmia et al. (2025)

**Research Problem:** Deepfake detection under pose and local manipulation variation.

**Method / Technique:** Global, middle and local view encoders with pose features and MLP fusion.

**Dataset / Tools:** OpenForensics and FaceForensics++.

**Main Findings:** Multi-view and pose information improved detection.

**Limitation:** Focused mainly on static natural images rather than temporal video streams.

**Relevance to Proposed Research:** Supports consideration of multiple facial views and attack diversity.

**DOI / Official Link:** https://arxiv.org/abs/2510.15576

---

## 23. Adversarial Patch Attacks on Deep-Learning-Based Face Recognition Systems Using Generative Adversarial Networks

**Authors / Year:** Hwang et al. (2023)

**Research Problem:** Physical adversarial manipulation of face recognition systems.

**Method / Technique:** GAN-generated adversarial patches.

**Dataset / Tools:** Face recognition benchmark setting.

**Main Findings:** GAN-generated patches could fool black-box recognition systems.

**Limitation:** Assumes an attacker can place a physical patch.

**Relevance to Proposed Research:** Highlights the need to consider adversarial attack diversity.

**DOI / Official Link:** https://doi.org/10.3390/s23020853

---

## 24. A Review of Deepfake and Its Detection: From Generative Adversarial Networks to Diffusion Models

**Authors / Year:** Liu et al. (2025)

**Research Problem:** Changing deepfake generation and detection methods.

**Method / Technique:** Systematic review and categorisation.

**Dataset / Tools:** Public deepfake datasets reviewed in the literature.

**Main Findings:** Diffusion-based deepfakes are harder to detect than earlier GAN-based methods.

**Limitation:** Review does not provide new experiments.

**Relevance to Proposed Research:** Supports treating attack diversity as an ongoing robustness issue.

**DOI / Official Link:** https://doi.org/10.1155/int/9987535

---

