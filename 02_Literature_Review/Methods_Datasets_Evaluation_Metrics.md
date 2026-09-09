# Methods, Algorithms, Datasets and Evaluation Metrics

## 1. Methods and Algorithms Identified

| Area | Methods / Algorithms identified from the reviewed studies |
|---|---|
| Face anti-spoofing / liveness detection | CNN-based approaches, person-specific Siamese networks, learnable gradient operators, colour-inversion dual-stream CNNs, image-quality features, fine-grained patch recognition |
| Cross-domain / unseen attacks | Meta Pattern Learning, Shuffled Style Assembly Network (SSAN), Multi-Domain Feature Alignment (MADG), Test-Time Adaptation (TTA), ensemble stacking |
| Deepfake / adversarial detection | Spatial-temporal deep learning, multiview detection, GAN-generated adversarial patches, review of GAN-based and diffusion-based threats |
| Privacy protection | Randomisation, frequency-domain protection, cancelable biometrics, BioCrypto encryption, template protection, encrypted feature extraction |
| Distributed / secure privacy approaches | Federated learning, blockchain with GAN-based obfuscation, secure multi-party computation |
| Multimodal / practical systems | RGB + infrared + depth processing, face + fingerprint recognition, pretrained deep learning models, IoT-based facial recognition |

## 2. Relevant Datasets and Data Sources

The reviewed studies use public benchmark datasets, private/custom datasets, and practical deployment data. Examples appearing in the group's literature review include CASIA-FASD, SiW, Replay-Attack, OULU-NPU, CASIA-MFSD, MSU-MFSD, WMCA, CASIA-SURF / CASIA-SURF CeFA, LFW, MOBIO, CFP-FP, AgeDB-30, IJB-C, CelebA, FERET, CVL, IITK, CASIA-Face-v5, FFIW-10K, FaceForensics++, OpenForensics and classroom/custom facial datasets.

## 3. Evaluation Metrics

| Metric | Use identified in the reviewed literature |
|---|---|
| ACER | Face anti-spoofing error evaluation |
| HTER | Face anti-spoofing / verification error evaluation |
| EER | Error-rate evaluation in recognition / anti-spoofing studies |
| Accuracy | Classification or recognition performance |
| Precision | Positive-prediction performance |
| Recall | Detection of positive samples |
| F1-score | Combined precision and recall measure |
| AUC / ROC-AUC | Overall discrimination performance |
| TAR@FAR | Recognition performance at a selected false-acceptance rate |
| Attack Success Rate | Effectiveness of attack methods |
| Recognition Accuracy | Correct identity-recognition performance |
| Inference Speed / Latency | Computational and deployment efficiency |
