# 01 — Research Papers

## Overview

This section compiles the **48 selected research papers** used in the group literature review. The papers cover facial recognition, face anti-spoofing, cross-domain and unseen attacks, deepfake and adversarial attacks, privacy protection, secure biometric processing, and practical or multimodal facial biometric systems. The publication years range from **2022 to 2026**.

## Compiled Research Papers

The same information fields are used for every paper to make the literature evidence easy to compare and review.

### 1. Test-time adaptation for robust face anti-spoofing

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Pei-Kai Huang; Chen-Yu Lu, Shu-Jung Chang; Jun-Xiong Chong; Chiou-Ting Hsu |
| **Objective / Problem** | Addresses Test-Time Adaptation (TTA) in Face Anti-Spoofing (FAS) to adapt an off-the-shelf model online to unseen target domains and novel attack types without accessing source domain data. |
| **Dataset / Data Source** | Benchmark dataset TTA-FAS |
| **Method / Approach** | Activation-based pseudo-labeling with Test-Time Adaptation (3A-TTA) |
| **Functionality / Process** | -Takes a pre-trained source FAS model and receives unlabelled streaming target face samples during testing.; Generates fine-grained pseudo-labels using activation maps to minimize label noise. |
| **Tools / Technologies** | PyTorch |
| **Evaluation Metrics** | Half Total Error Rate (HTER), Equal Error Rate (EER), Accuracy |
| **Key Findings / Results** | 3A-TTA significantly outperforms existing baseline TTA methods adapted from general image classification. |
| **Weaknesses / Limitations** | Incurring computational overhead and latency during inference due to continuous online gradient updates/back propagation. |
| **Research Gap / Relevance** | First study to evaluate a dedicated Test-Time Adaptation (TTA) setup for Face Anti-Spoofing, offering a practical solution where source data cannot be stored due to privacy (GDPR) or storage constraints. |
| **Official Source / DOI** | https://proceedings.bmvc2023.org/379/ |

### 2. Masked face detection and recognition system based on Deep Learning algorithms

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Hayat Al-Dmour; Afaf Tareef; Asma Musabah Alkalbani; Awni Hammouri; Ban Alrahmani |
| **Objective / Problem** | Addresses the degradation of traditional facial recognition and registration authentication systems caused by face masks, which obscure critical facial features such as the nose, mouth, and chin. |
| **Dataset / Data Source** | benchmark and synthetic face image datasets containing unmasked, correctly masked, and incorrectly masked face images. |
| **Method / Approach** | Convolutional Neural Network (CNN) with early stopping and cross-validation |
| **Functionality / Process** | -Detects face region; Performs binary classification (masked vs. unmasked) |
| **Tools / Technologies** | Convolutional Neural Networks (CNN), Deep Learning frameworks, Image Processing algorithms. |
| **Evaluation Metrics** | Classification Accuracy, Precision, Recall, F1-Score |
| **Key Findings / Results** | Achieved 99.77% binary detection accuracy and 97.98% identification accuracy on masked facial profiles |
| **Weaknesses / Limitations** | Identification accuracy drops under extreme side angles or severe facial occlusions like glasses or mask |
| **Research Gap / Relevance** | Further research is needed to reconstruct hidden lower-facial features using generative networks prior to matching |
| **Official Source / DOI** | https://doi.org/10.12720/jait.14.2.224-232 |

### 3. A hybrid deep learning framework for deepfake detection using temporal and spatial features

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | - Fazeel Zafar; Talha Ahmed Khan; Salas Akbar; Muhammad Talha Ubaid; Sameena Javaid; Kushsairy Abdul Kadir |
| **Objective / Problem** | Addresses the threat posed by increasingly realistic AI-generated deepfakes created using Generative Adversarial Networks (GANs). |
| **Dataset / Data Source** | FFIW-10K (Face Forensics in the Wild 10K dataset) |
| **Method / Approach** | Hybrid Enhanced EfficientNet-B0 and Temporal Convolutional Neural Network (TempCNN) |
| **Functionality / Process** | -Dissects input video streams into individual sequential frames.; Detects and aligns facial regions using Multi-Task Cascaded Convolutional Networks (MTCNN). |
| **Tools / Technologies** | -EfficientNet-B0; Temporal Convolutional Networks (TempCNNs) |
| **Evaluation Metrics** | -Training Accuracy; Testing Accuracy; Epochs |
| **Key Findings / Results** | Achieved 91.5% training accuracy and 92.45% testing accuracy after 40 epochs on the FFIW-10K dataset. |
| **Weaknesses / Limitations** | Performance may drop if faces are severely occluded, low-resolution, or heavily blurred. |
| **Research Gap / Relevance** | deepfake detection models often focus on either spatial or temporal features independently, or require heavy computational power that restricts real-world deployment. |
| **Official Source / DOI** | https://doi.org/10.1109/access.2025.3566008 |

### 4. Face liveness detection using artificial intelligence techniques: A systematic literature review and future directions

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | Smita Khairnar; Shilpa Gite; Ketan Kotecha; Sudeep D. Thepade |
| **Objective / Problem** | Review, categorize, and evaluate existing face liveness detection research published over the past decade to address physical presentation attacks targeting biometric authentication systems. |
| **Dataset / Data Source** | Systematic Literature Review analyzing studies retrieved from major academic databases synthesizes benchmark datasets reviewed in literature |
| **Method / Approach** | PRISMA framework-based Systematic Literature Review (SLR) utilizing preset inclusion/excl usion criteria, thematic synthesis, and taxonomy classification of feature extraction and AI strategies. |
| **Functionality / Process** | -Queries and screens peer-reviewed literature across academic repositories using PRISMA protocols.; Categorizes presentation attacks (static photo prints, dynamic video replays, 3D mask occlusions). |
| **Tools / Technologies** | -PRISMA Framework; Machine Learning / Deep Learning algorithms |
| **Evaluation Metrics** | Average Classification Error Rate (ACER), Equal Error Rate (EER), HTER |
| **Key Findings / Results** | Deep Learning models consistently outperform traditional hand-crafted texture approaches (e.g., LBP, HoG) across multi-attack scenarios |
| **Weaknesses / Limitations** | -As a literature review paper, it does not present new empirical experiments, a custom dataset, or a new model architecture.; Paper selection is limited to specific database indexing and predefined timeframes, potentially missing unindexed preprint literature |
| **Research Gap / Relevance** | Prior literature reviews lacked a comprehensive synthesis connecting traditional texture-based anti-spoofing with recent cutting-edge paradigms like XAI, Federated Learning, and Meta-Learning |
| **Official Source / DOI** | https://doi.org/10.3390/bdcc7010037 |

### 5. Unmasking facial deepfakes: A robust multiview detection framework for natural images

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | Sami Belguesmia; Mohand Said Allili; Assia Hamadene |
| **Objective / Problem** | challenge of detecting facial DeepFakes under unconstrained real-world conditions |
| **Dataset / Data Source** | - O; F penForensic s dataset aceForensic s++dataset. |
| **Method / Approach** | Propose a superb multi-view detection framework that combines three facial view encoders (Global, Middle, Local), a dedicated face orientation (pose) encoder, and a multi-layer perceptron (MLP) feature fusion module |
| **Functionality / Process** | Uses RetinaFace to locate faces and extract five key facial landmarks (eyes, nose, mouth corners) |
| **Tools / Technologies** | -PyTorch; RetinaFace; MobileNet |
| **Evaluation Metrics** | Precision, Recall, F1-score, Area Under the Curve (AUC) |
| **Key Findings / Results** | - I; Fusing multiple spatial views significantly outperforms single-view baselines across all evaluation metrics on both datasets ncorporating face orientation features noticeably improves performance (OpenForensi cs AUC: 98.49%; FaceForensic s++ AUC: 99.88% |
| **Weaknesses / Limitations** | Evaluated primarily on single-frame static natural images without incorporating temporal frame-to-frame sequence dynamics for video streams |
| **Research Gap / Relevance** | Standard DeepFake detectors assume un-oriented, frontal faces and rely on single-view global features, making them vulnerable to localized manipulation s and real-world head pose variations |
| **Official Source / DOI** | https://arxiv.org/abs/2510.15576 |

### 6. Privacy-preserving face recognition method based on randomization and local feature learning

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Yanhua Huang; Zhendong Wu; Juan Chen; Hui Xiang |
| **Objective / Problem** | Preserve privacy while keeping FR accuracy |
| **Dataset / Data Source** | LFW, CelebA, HDU (private) |
| **Method / Approach** | Random convolution with self-learning batch norm |
| **Functionality / Process** | Scrambles face images via random convolution prior to recognition; learns robust features via adaptive batch norm |
| **Tools / Technologies** | Python; deep learning framework |
| **Evaluation Metrics** | Recognition accuracy on scrambled images |
| **Key Findings / Results** | Scrambled images matched normal-image accuracy |
| **Weaknesses / Limitations** | Server-side trust assumption remains |
| **Research Gap / Relevance** | Extend to fully untrusted-server scenarios |
| **Official Source / DOI** | https://doi.org/10.3390/jimaging10030059 |

### 7. A review of Deepfake and its detection: From generative adversarial networks to Diffusion Models

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | Baoping Liu; Bo Liu; Tianqing Zhu; Ming Ding |
| **Objective / Problem** | Track how deepfake generation and detection have evolved from GANs to diffusion models. |
| **Dataset / Data Source** | Survey covering major public deepfake generation and detection datasets. |
| **Method / Approach** | Systematic literature review and categorization of generation and detection techniques. |
| **Functionality / Process** | Organizes methods by generation model type and matches them against correspondin g detection strategies. |
| **Tools / Technologies** | Reviews GAN based and diffusion based generative frameworks. |
| **Evaluation Metrics** | Comparative synthesis of detection accuracy trends across surveyed studies. |
| **Key Findings / Results** | Diffusion based deepfakes are harder to detect than earlier GAN based ones, driving a shift in detection research. |
| **Weaknesses / Limitations** | As a review, it reports no new experiments of its own. |
| **Research Gap / Relevance** | Highlights detection methods have not kept pace with newer diffusion-based generation techniques. |
| **Official Source / DOI** | https://doi.org/10.1155/int/9987535 |

### 8. Comprehensive vulnerability evaluation of face recognition systems to template inversion attacks via 3D face reconstruction

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Hatef Otroshi Shahrez; Sébastien Marcel |
| **Objective / Problem** | Test whether stored face templates can be reversed back into usable face images. |
| **Dataset / Data Source** | LFW and MOBIO datasets. |
| **Method / Approach** | GaFaR method using a geometry aware generative neural radiance field network. |
| **Functionality / Process** | Maps stolen templates to a 3D face generator to reconstruct the original face. |
| **Tools / Technologies** | Generative neural radiance fields with camera parameter optimization. |
| **Evaluation Metrics** | Attack success rate in whitebox and blackbox settings. |
| **Key Findings / Results** | Reconstructed faces successfully fooled state of the art face recognition systems, including through printed photo and screen replay attacks. |
| **Weaknesses / Limitations** | Requires access to the template embedding, which not all attack scenarios provide. |
| **Research Gap / Relevance** | Shows stored templates alone are not safe without additional protection like template encryption. |
| **Official Source / DOI** | https://doi.org/10.1109/tpami.2023.3312123 |

### 9. Adversarial patch attacks on deep-learning-based face recognition systems using generative adversarial networks

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Ren-Hung Hwang; Jia-You Lin; Sun-Ying Hsieh; Hsuan-Yu Lin; Chia-Liang Lin |
| **Objective / Problem** | Test black-box adversarial patch attacks on FR |
| **Dataset / Data Source** | Face recognition benchmark |
| **Method / Approach** | GAN-generated adversarial patches |
| **Functionality / Process** | Trains a GAN to generate patches and applies them to face images to fool black-box FR APIs |
| **Tools / Technologies** | Phython; GAN framework |
| **Evaluation Metrics** | Attack success rate (black-box) |
| **Key Findings / Results** | GAN patches fooled real-world black-box FR systems |
| **Weaknesses / Limitations** | Assumes attacker can place physical patch |
| **Research Gap / Relevance** | Study defences against GAAN-crafted physical patches |
| **Official Source / DOI** | https://doi.org/10.3390/s23020853 |

### 10. Toward robust and privacy-enhanced facial recognition: A decentralized blockchain-based approach with GANs and Deep Learning

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Muhammad Ahmad Nawaz Ul Ghani; Kun She; Muhammad Arslan Rauf; Shumaila Khan; Masoud Alajmi; Yazeed Yasin Ghadi; Hend Khalid Alkahtani |
| **Objective / Problem** | Protect facial data privacy while enabling authentication |
| **Dataset / Data Source** | Custom facial dataset |
| **Method / Approach** | Blockchain with GAN-based obfuscation and clustering |
| **Functionality / Process** | Cluster facial traits, obfuscates them via GAN and stores encoded data on blockchain nodes |
| **Tools / Technologies** | Python; blockchain platform; GAN framework |
| **Evaluation Metrics** | Recognition accuracy, privacy metrics |
| **Key Findings / Results** | Decentralized storage improved privacy without major accuracy loss |
| **Weaknesses / Limitations** | Blockchain adds latency/storage overhead |
| **Research Gap / Relevance** | Improve scalability of blockchain-based biometric storage |
| **Official Source / DOI** | https://doi.org/10.3934/mbe.2024184 |

### 11. An attack on facial soft-biometric privacy enhancement

| Field | Details |
|---|---|
| **Year** | 2022 |
| **Author(s)** | - Dailé Osorio-Roig; Christian Rathgeb; Pawel Drozdowski; Philipp Terhörst; Vitomir Štruc; Christoph Busch |
| **Objective / Problem** | Test privacy enhancement techniques for soft biometrics |
| **Dataset / Data Source** | Face benchmark datasets |
| **Method / Approach** | Attack modelling on privacy-enhanced FR |
| **Functionality / Process** | Attempts to reverse/recov er soft-biometric attributes from protected templates |
| **Tools / Technologies** | Phyton |
| **Evaluation Metrics** | Attack success rate |
| **Key Findings / Results** | Existing soft-biometric privacy methods can be reversed |
| **Weaknesses / Limitations** | Highlights weak privacy guarantees in current techniques |
| **Research Gap / Relevance** | Design privacy enhancement techniques resistant to attribute-inference attacks |
| **Official Source / DOI** | https://doi.org/10.1109/tbiom.2022.3172724 |

### 12. A secure face recognition for IOT-enabled healthcare system

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Alamgir Sardar; Saiyed Umer; Ranjeet Kr. Rout; Shui-Hua Wang; M. Tanveer |
| **Objective / Problem** | Protect face templates used in IoT healthcare surveillance from theft. |
| **Dataset / Data Source** | Four benchmark face databases: CVL, IITK, CASIA-Face-v5, and FERET. |
| **Method / Approach** | Three step protection combining cancelable biometrics and BioCrypto encryption. |
| **Functionality / Process** | Transforms each face template before storage so it cannot be reversed if leaked. |
| **Tools / Technologies** | Python based face recognition with cryptographic template protection. |
| **Evaluation Metrics** | Recognition accuracy, irreversibility , revocability, and unlinkability. |
| **Key Findings / Results** | Kept strong accuracy across all four datasets while meeting protection requirements. |
| **Weaknesses / Limitations** | Added encryption increases computation on constrained IoT hardware. |
| **Research Gap / Relevance** | Real world edge device efficiency still needs further testing. |
| **Official Source / DOI** | https://doi.org/10.1145/3534122 |

### 13. Robust face recognition under challenging conditions: A comprehensive review of Deep Learning methods and challenges

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | - Aidana Zhalgas; Beibut Amirgaliyev; Adil Sovet |
| **Objective / Problem** | Review how face recognition models perform under pose, occlusion, and low resolution. |
| **Dataset / Data Source** | Five benchmark datasets: LFW, CPLFW, CALFW, AgeDB-30, and QMUL-SurvFace. |
| **Method / Approach** | Comparative review of FaceNet, ArcFace, OpenFace, and SFace. |
| **Functionality / Process** | Each architecture is run against each benchmark dataset and scored, so that strengths/weaknesses under specific real-world degradations (e.g., surveillance-grade low resolution) can be directly compared rather than |
| **Tools / Technologies** | Python; FaceNet, ArcFace, OpenFace, and SFace reference implementati ons. |
| **Evaluation Metrics** | Area under the ROC curve (ROC-AUC); accuracy; precision; F1-score. |
| **Key Findings / Results** | FaceNet and ArcFace led in constrained settings, SFace led in surveillance conditions. |
| **Weaknesses / Limitations** | Review is limited to four architectures and five datasets; does not include the newest transformer-based face recognition models or adversarially-robust variants. |
| **Research Gap / Relevance** | Shows model choice should match deployment context. |
| **Official Source / DOI** | https://doi.org/10.3390/app15179390 |

### 14. Maintaining privacy in face recognition using Federated Learning Method

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | Abraham Woubie, Enoch Solomon, Joseph Attieh |
| **Objective / Problem** | Avoid exposing sensitive face data during centralized model training. |
| **Dataset / Data Source** | Public face datasets partitioned across simulated federated clients. |
| **Method / Approach** | Federated learning applied both with and without secure aggregators, to supervised and unsupervised face recognition model training. |
| **Functionality / Process** | Clients train locally and share only model updates, not raw images. |
| **Tools / Technologies** | Federated learning framework, secure aggregation protocol, and supervised as well as unsupervised face recognition training pipelines. |
| **Evaluation Metrics** | Face recognition accuracy under federated learning, in both supervised and unsupervised settings, compared against centralized, non-federated training baselines. |
| **Key Findings / Results** | Matched centralized accuracy while keeping raw data on device. |
| **Weaknesses / Limitations** | Adds communication overhead and struggles with uneven client data. |
| **Research Gap / Relevance** | Scalability to very large, diverse client populations remain untested. |
| **Official Source / DOI** | https://doi.org/10.1109/access.2024.3373691 |

### 15. Trustworthy face recognition as a service: A multi-layered approach for mitigating spoofing and ensuring system integrity

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | - Mostafa Kira; Zeyad Alajamy; Ahmed Soliman; Yusuf Mesbah; Manuel Mazzara |
| **Objective / Problem** | Defend a cloud face recognition service against spoofing and deepfakes. |
| **Dataset / Data Source** | Platform level testing rather than a fixed benchmark dataset. |
| **Method / Approach** | Multi layered FRaaS combining passive liveness detection and active challenge response. |
| **Functionality / Process** | Escalates ambiguous cases from passive checks to active user challenges. |
| **Tools / Technologies** | Cloud FRaaS platform, open source SDK, and Lighthouse auditing. |
| **Evaluation Metrics** | Lighthouse audit scores and SDK code coverage. |
| **Key Findings / Results** | Scored above ninety six percent on audits and over ninety one percent code coverage. |
| **Weaknesses / Limitations** | Lacks standard spoof detection accuracy metrics like EER or HTER. |
| **Research Gap / Relevance** | Frames security as whole service trustworthiness, not just model accuracy. |
| **Official Source / DOI** | https://doi.org/10.3390/fi17100450 |

### 16. Learning Meta Pattern for face anti-spoofing

| Field | Details |
|---|---|
| **Year** | 2022 |
| **Author(s)** | - Rizhao Cai; Zhi Li; Renjie Wan, Haoliang Li; Yongjian Hu; Alex Chichung Kot |
| **Objective / Problem** | Improve face anti-spoofing performance on unseen domains. |
| **Dataset / Data Source** | Public FAS datasets. |
| **Method / Approach** | Learning-to-learn Meta Pattern with a two-stream network. |
| **Functionality / Process** | Learns spoofing patterns from different facial regions to improve generalisation. |
| **Tools / Technologies** | CNN, Meta Pattern, HFM. |
| **Evaluation Metrics** | HTER, ACER and cross-domain performance. |
| **Key Findings / Results** | The proposed method improved generalisation compared with existing methods. |
| **Weaknesses / Limitations** | Performance can still drop when the testing domain is very different. |
| **Research Gap / Relevance** | Useful for improving face liveness detection against unseen attacks. |
| **Official Source / DOI** | https://doi.org/10.1109/tifs.2022.3158551 |

### 17. PatchNet: A simple face anti-spoofing framework via fine-grained patch recognition

| Field | Details |
|---|---|
| **Year** | 2022 |
| **Author(s)** | - Chien-Yi Wang; Yu-Ding Lu; Shang-Ta Yang; Shang-Hong Lai |
| **Objective / Problem** | Detect unseen face spoofing attacks using local facial information. |
| **Dataset / Data Source** | Public face anti-spoofing datasets. |
| **Method / Approach** | PatchNet with fine-grained patch recognition. |
| **Functionality / Process** | Divides the face into small patches and learns local spoofing features. |
| **Tools / Technologies** | CNN, patch recognition and self-supervised learning. |
| **Evaluation Metrics** | Intra-dataset and cross-dataset performance. |
| **Key Findings / Results** | The method improved detection of unseen spoofing attacks. |
| **Weaknesses / Limitations** | Local features may not capture all information from the whole face. |
| **Research Gap / Relevance** | Relevant to robust presentation attack detection. |
| **Official Source / DOI** | https://doi.org/10.1109/cvpr52688.2022.01964 |

### 18. Domain generalization via shuffled style assembly for face anti-spoofing

| Field | Details |
|---|---|
| **Year** | 2022 |
| **Author(s)** | - Zhuo Wang; Zezheng Wang; Zitong Yu; Weihong Deng; Jiahong Li; Tingting Gao; Zhongyuan Wang |
| **Objective / Problem** | Improve face anti-spoofing across different domains. |
| **Dataset / Data Source** | Existing FAS datasets and a new benchmark. |
| **Method / Approach** | Shuffled Style Assembly Network, SSAN. |
| **Functionality / Process** | Separates content and style features and combines different styles during training. |
| **Tools / Technologies** | CNN, contrastive learning and SSAN. |
| **Evaluation Metrics** | FAS benchmark performance. |
| **Key Findings / Results** | SSAN achieved better generalisation on different datasets. |
| **Weaknesses / Limitations** | Dataset differences can still affect performance in real environments . |
| **Research Gap / Relevance** | Relevant to domain generalisation in face biometric security. |
| **Official Source / DOI** | https://doi.org/10.1109/cvpr52688.2022.00409 |

### 19. Privacy-preserving face recognition in the frequency domain

| Field | Details |
|---|---|
| **Year** | 2022 |
| **Author(s)** | - Yinggui Wang; Jian Liu, Man Luo; Le Yang; Li Wang |
| **Objective / Problem** | Protect facial images from privacy leakage during cloud based recognition. |
| **Dataset / Data Source** | Evaluated across benchmark datasets (e.g., LFW, CFP-FP, AgeDB-30, IJB-C) |
| **Method / Approach** | Frequency-domain channel selection and fast masking |
| **Functionality / Process** | Converts faces to frequency channels via BDCT, drops >94% of visual energy, and applies fast masking |
| **Tools / Technologies** | Block Discrete Cosine Transform (BDCT), Analysis Network, Fast Masking, ArcFace |
| **Evaluation Metrics** | Recognition Recognition accuracy (TAR@FAR) , image energy loss, and inference speed |
| **Key Findings / Results** | The method provided privacy protection with a limited decrease in recognition accuracy. |
| **Weaknesses / Limitations** | More privacy protection can also reduce recognition performance. |
| **Research Gap / Relevance** | Relevant to privacy protection of facial biometric data. |
| **Official Source / DOI** | https://doi.org/10.1609/aaai.v36i3.20157 |

### 20. Person-specific face spoofing detection based on a Siamese network

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Mingtao Pei; Bin Yan; Huiling Hao; Meng Zhao |
| **Objective / Problem** | Improve face spoofing detection using the identity of the user. |
| **Dataset / Data Source** | SiW, CASIA-FASD and Replay-Attack. |
| **Method / Approach** | Person-specific Siamese Network. |
| **Functionality / Process** | Compares the test face with a genuine reference image of the user. |
| **Tools / Technologies** | Siamese Network, face recognition and Joint Bayesian Loss. |
| **Evaluation Metrics** | Spoof detection and cross-dataset performance. |
| **Key Findings / Results** | Using user identity information improved spoofing detection. |
| **Weaknesses / Limitations** | Requires a genuine reference image for each user. |
| **Research Gap / Relevance** | Relevant to identity based face liveness detection. |
| **Official Source / DOI** | https://doi.org/10.1016/j.patcog.2022.109148 |

### 21. A learnable gradient operator for face presentation attack detection

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Caixun Wang; Bingyao Yu; Jiwen Lu; Jie Zhou |
| **Objective / Problem** | Improve face presentation attack detection using fine-grained features. |
| **Dataset / Data Source** | Replay-Attack, CASIA-FASD, OULU-NPU and SiW. |
| **Method / Approach** | Learnable Gradient Operator Network. |
| **Functionality / Process** | Learns gradient information directly from facial images to identify spoofing features. |
| **Tools / Technologies** | CNN, learnable gradient operator and adaptive gradient loss. |
| **Evaluation Metrics** | HTER and PAD performance. |
| **Key Findings / Results** | The method showed better PAD performance on several benchmark datasets. |
| **Weaknesses / Limitations** | Cross-domain differences can still affect the results. |
| **Research Gap / Relevance** | Relevant to fine-grained face spoofing detection. |
| **Official Source / DOI** | https://doi.org/10.1016/j.patcog.2022.109146 |

### 22. Face spoofing detection based on multi-scale color inversion dual-stream convolutional neural network

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | -Xin Shu; Xi Li; Xi Zuo; Dong Xu; Jiachen Shi |
| **Objective / Problem** | Improve face spoof detection under different lighting conditions. |
| **Dataset / Data Source** | Public face anti-spoofing datasets. |
| **Method / Approach** | Multi-scale Color Inversion Dual-Stream CNN. |
| **Functionality / Process** | Uses original and colour inverted images to obtain more spoofing information. |
| **Tools / Technologies** | CNN, dual-stream network and multi-scale features. |
| **Evaluation Metrics** | Accuracy and ACER. |
| **Key Findings / Results** | The method improved detection compared with single stream approaches. |
| **Weaknesses / Limitations** | Unseen attacks and difficult lighting conditions are still challenging. |
| **Research Gap / Relevance** | Relevant to face liveness detection. |
| **Official Source / DOI** | https://doi.org/10.1016/j.eswa.2023.119988 |

### 23. FASS: Face anti-spoofing system using image quality features and deep learning

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Enoch Solomon; Krzysztof J. Cios |
| **Objective / Problem** | Detect face spoofing using image quality features and deep learning. |
| **Dataset / Data Source** | Replay-Attack, CASIA-MFSD, MSU-MFSD, OULU-NPU and SiW. |
| **Method / Approach** | FASS ensemble system. |
| **Functionality / Process** | Combines image quality features with deep learning models to detect spoofing. |
| **Tools / Technologies** | Random Forest, ResNet50, SVM and image quality features. |
| **Evaluation Metrics** | Accuracy, HTER and cross dataset performance. |
| **Key Findings / Results** | FASS performed better than several existing face anti-spoofing methods. |
| **Weaknesses / Limitations** | Results depend on the quality of the captured face images. |
| **Research Gap / Relevance** | Strongly related to practical face anti-spoofing. |
| **Official Source / DOI** | https://doi.org/10.3390/electronics12102199 |

### 24. Fusion-based 2.5D Face Recognition System

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Min-Er Teo; Lee-Ying Chong; Siew-Chin Chong |
| **Objective / Problem** | Improve 2D face recognition under lighting and pose changes. |
| **Dataset / Data Source** | FRGC v2.0 database. |
| **Method / Approach** | Fusion-based 2.5D face recognition. |
| **Functionality / Process** | Extract depth/texture features, followed by GRCM feature fusion and face matching |
| **Tools / Technologies** | 2.5D depth images; Gabor-based Region Covariance Matrices. |
| **Evaluation Metrics** | Recognition accuracy; fusion comparison. |
| **Key Findings / Results** | Best max-min fusion reached 93.66% accuracy. |
| **Weaknesses / Limitations** | Uses a benchmark dataset; real-world deployment not tested. |
| **Research Gap / Relevance** | Test 2.5D recognition in uncontrolled environments and security systems. |
| **Official Source / DOI** | https://doi.org/10.18080/jtde.v12n1.770 |

### 25. Development of automated attendance system using pretrained deep learning models

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Muhammad Shahrul Zaim Ahmad; Nor Azlina Ab. Aziz; Anith Khairunnisa Ghazali |
| **Objective / Problem** | Automate student attendance with face recognition. |
| **Dataset / Data Source** | Student classroom images/data. |
| **Method / Approach** | Six pretrained face-recognition models; FaceNet selected. |
| **Functionality / Process** | Capture face, identify student, confirm attendance, and store the record |
| **Tools / Technologies** | FaceNet; IoT; pretrained deep-learning models. |
| **Evaluation Metrics** | Recognition accuracy. |
| **Key Findings / Results** | FaceNet achieved more than 95% accuracy. |
| **Weaknesses / Limitations** | Attendance-focused; limited spoofing/security testing. |
| **Research Gap / Relevance** | Add liveness detection and presentation-attack testing. |
| **Official Source / DOI** | https://doi.org/10.33093/ijoras.2024.6.1.2 |

### 26. An automated face detection and recognition for class attendance

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Chang-Horn Boe; Kok-Why Ng; Su-Cheng Haw; Palanichamy Naveen; Elham Abdulwahab Anaam |
| **Objective / Problem** | Automate class attendance using face recognition. |
| **Dataset / Data Source** | Classroom/st udent face images. |
| **Method / Approach** | Face detection + face recognition. |
| **Functionality / Process** | Capture image, detect face, recognise student, and record attendance |
| **Tools / Technologies** | Face recognition; computer vision; web/system components. |
| **Evaluation Metrics** | Recognition accuracy; system performance. |
| **Key Findings / Results** | Developed an automated face-detection and recognition attendance system. |
| **Weaknesses / Limitations** | Mainly classroom-focused; security attacks not deeply evaluated. |
| **Research Gap / Relevance** | Test spoofing, lighting, pose and larger student populations. |
| **Official Source / DOI** | https://doi.org/10.62527/joiv.8.3.2967 |

### 27. A new Asian version of the CFMT: The Cambridge Face Memory Test – Chinese Malaysian (CFMT-My)

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Siew Kei Kho; Bryan Q. Z. Leong; David R. T. Keeble; Huck-Koo Wong; Alejandro J. Estudillo |
| **Objective / Problem** | Create a face-memory benchmark for Chinese Malaysians. |
| **Dataset / Data Source** | 134 Chinese Malaysian participants; CFMT-MY. |
| **Method / Approach** | Adapted Cambridge Face Memory Test. |
| **Functionality / Process** | Learn unfamiliar faces, recognise target faces, and compare performance |
| **Tools / Technologies** | CFMT-MY; face-memory testing. |
| **Evaluation Metrics** | Recognition accuracy; group comparisons. |
| **Key Findings / Results** | Introduced a Chinese Malaysian face-memory benchmark. |
| **Weaknesses / Limitations** | Face memory rather than direct authentication. |
| **Research Gap / Relevance** | Use Malaysian face data for biometric recognition and fairness testing. |
| **Official Source / DOI** | https://doi.org/10.3758/s13428-023-02085-6 |

### 28. IOT smart door system with motion sensing and facial recognition

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Muhammad Kamil Hamzah; Norakmar Arbain Sulaiman; Murizah Kassim; Shuria Saaidin; Suhaili Beeran Kutty |
| **Objective / Problem** | Improve smart-door security with facial recognition. |
| **Dataset / Data Source** | Door-user facial images; smart-door test environment. |
| **Method / Approach** | IoT smart-door system with facial recognition. |
| **Functionality / Process** | Detect person, recognise face, and trigger door access |
| **Tools / Technologies** | IoT; camera; facial recognition; smart door. |
| **Evaluation Metrics** | Recognition/a ccess performance. |
| **Key Findings / Results** | Combines facial recognition with an IoT smart-door system. |
| **Weaknesses / Limitations** | Controlled access environment; limited anti-spoofing evaluation. |
| **Research Gap / Relevance** | Add liveness detection and test photo/video attacks. |
| **Official Source / DOI** | https://doi.org/10.1109/cspa60979.2024.10525522 |

### 29. Smart attendance in classroom (Cobot): IOT and facial recognition for educational and entrepreneurial impact

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Ahmad Anwar Zainuddin; Rizal Mohd Nor; Dini Handayani; Mohd. Izzuddin Mohd. Tamrin; Krishnan Subramaniam; Siti Fairuz Nurr Sadikan |
| **Objective / Problem** | Reduce attendance fraud and manual attendance work. |
| **Dataset / Data Source** | Facial images of 60 students. |
| **Method / Approach** | Mobile classroom robot (CObot) with IoT and face recognition. |
| **Functionality / Process** | Detect person, recognise face, and log attendance to Google Sheets. |
| **Tools / Technologies** | Raspberry Pi 5; ESP32-S3; camera; OpenCV; Google Sheets API. |
| **Evaluation Metrics** | Recognition accuracy (%); processing speed (RPi5 vs. ESP32). |
| **Key Findings / Results** | Raspberry Pi 5 achieved 99% accuracy (vs. 90% ESP32) and automated real-time logging. |
| **Weaknesses / Limitations** | Attendance-focused; limited biometric security testing. |
| **Research Gap / Relevance** | Evaluate spoofing, privacy and real-world classroom conditions. |
| **Official Source / DOI** | https://doi.org/10.34306/att.v6i3.497 |

### 30. Acceptance of or resistance to facial recognition payment: A systematic review

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Teng Yu; Chengliang Wang; Qing Bian; Ai Ping Teoh |
| **Objective / Problem** | Synthesize global factors influencing consumer acceptance of or resistance to facial recognition payment (FRP) systems. |
| **Dataset / Data Source** | Empirical literature corpus on facial recognition payment adoption (SLR dataset). |
| **Method / Approach** | Systematic review of facial-recognition payment acceptance. |
| **Functionality / Process** | Review factors affecting acceptance and resistance, then compare privacy, security, and trust issues |
| **Tools / Technologies** | SLR methodology; PRISMA framework; TAM / UTAUT theoretical models. |
| **Evaluation Metrics** | Literature comparison; acceptance factors. |
| **Key Findings / Results** | Identifies privacy, security, trust and usefulness as important factors. |
| **Weaknesses / Limitations** | Review-based; not a technical recognition experiment. |
| **Research Gap / Relevance** | Combine user acceptance with technical biometric-security testing. |
| **Official Source / DOI** | https://doi.org/10.1002/cb.2385 |

### 31. Impact of perceived privacy and security in the TAM model: The Perceived Trust as the mediated factors

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Yan Zhang |
| **Objective / Problem** | Examine privacy and security effects on face-recognition adoption. |
| **Dataset / Data Source** | User survey data. |
| **Method / Approach** | Trust-TAM model. |
| **Functionality / Process** | Measure perceived privacy and security, followed by trust and intention to use face recognition |
| **Tools / Technologies** | TAM framework; Structural Equation Modeling (SEM); survey questionnaire s. |
| **Evaluation Metrics** | Model relationships; behavioural intention. |
| **Key Findings / Results** | Perceived security and usefulness drive adoption; all hypotheses supported except privacy's direct impact on trust. |
| **Weaknesses / Limitations** | User-perception study; no algorithm testing. |
| **Research Gap / Relevance** | Study privacy/secur ity perceptions alongside actual biometric risks. |
| **Official Source / DOI** | https://doi.org/10.1016/j.jjimei.2024.100270 |

### 32. 2.5D face recognition system using EfficientNet with various optimizers

| Field | Details |
|---|---|
| **Year** | 2 025 |
| **Author(s)** | - Min-Er Teo; Lee-Ying Chong; Siew-Chin Chong; Pey-Yun Goh |
| **Objective / Problem** | Improve 2.5D face recognition with EfficientNet. |
| **Dataset / Data Source** | FRGC v2.0. |
| **Method / Approach** | EfficientNetB 1/B4 with different optimizers. |
| **Functionality / Process** | Use depth/2.5D face input for CNN feature extraction and identity classification |
| **Tools / Technologies** | EfficientNet; Adam; Nadam; Adamax; RMSProp. |
| **Evaluation Metrics** | Recognition accuracy. |
| **Key Findings / Results** | EfficientNetB 4 with Adam achieved 97.93% accuracy. |
| **Weaknesses / Limitations** | Benchmark-focused; limited real-world attack testing. |
| **Research Gap / Relevance** | Test depth-based recognition on mobile and uncontrolled environments . |
| **Official Source / DOI** | https://doi.org/10.62527/joiv.8.4.3030 |

### 33. Enhancing biometric authentication through multimodal approach combining face and fingerprint recognition using convolutional neural networks (CNN)

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | - Zulaiha Gimba; Ahmad Nurzid Rosli Ariffin; Nur Izura Udzir; Sufian Sani |
| **Objective / Problem** | Strengthen authentication using face and fingerprint together. |
| **Dataset / Data Source** | Georgia Tech; Essex; FVC2000; SOCOFing. |
| **Method / Approach** | CNN-based multimodal biometric fusion. |
| **Functionality / Process** | Extract face and fingerprint features, fuse the features, and authenticate the user |
| **Tools / Technologies** | CNN; face recognition; fingerprint recognition. |
| **Evaluation Metrics** | Accuracy; FAR; FRR. |
| **Key Findings / Results** | Multimodal system reduced FAR/FRR compared with relying on one biometric, although accuracy was slightly lower. |
| **Weaknesses / Limitations** | Needs two biometric sources and extra hardware/dat a. |
| **Research Gap / Relevance** | Test lightweight multimodal authentication on mobile devices. |
| **Official Source / DOI** | https://doi.org/10.1007/s10791-025-09775-z |

### 34. Face anti-spoofing based on Deep Learning: A comprehensive survey

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | - Yan Xing; Xiaohui Tan; Uzair Qamar; Licheng Jiao |
| **Objective / Problem** | Review deep-learning methods for face anti-spoofing. |
| **Dataset / Data Source** | OULU-NPU; CASIA-FASD; Replay-Attack; SiW and others. |
| **Method / Approach** | Comprehensi ve anti-spoofing survey. |
| **Functionality / Process** | Compare print, replay, 3D-mask and AI-generated attacks |
| **Tools / Technologies** | Deep Learning (CNNs, Vision Transformers ); RGB; Depth; IR; rPPG signals. |
| **Evaluation Metrics** | ACER; EER; HTER. |
| **Key Findings / Results** | Highlights deep learning and multimodal methods for stronger spoof detection. |
| **Weaknesses / Limitations** | Review paper; no new experiment. |
| **Research Gap / Relevance** | Improve unseen-attack, cross-domain and real-time liveness detection. |
| **Official Source / DOI** | https://doi.org/10.3390/app15126891 |

### 35. Face recognition using deep learning for real-time intruder detection

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | - Devandran Periasamy Pillai; Kalaivani Chellappan |
| **Objective / Problem** | Detect intruders in real time with low-cost face recognition. |
| **Dataset / Data Source** | Five known subjects; collected face images under varied conditions. |
| **Method / Approach** | Dlib pretrained ResNet-based face recognition. |
| **Functionality / Process** | Capture image, compare it with known faces, and trigger a buzzer/Whats App alert for unknown faces |
| **Tools / Technologies** | Raspberry Pi; Dlib; ResNet; Twilio. |
| **Evaluation Metrics** | Accuracy; precision; recall. |
| **Key Findings / Results** | Reported 96% accuracy and precision with 100% recall. |
| **Weaknesses / Limitations** | Small dataset; five known subjects. |
| **Research Gap / Relevance** | Test larger populations, spoofing and unseen environments . |
| **Official Source / DOI** | https://doi.org/10.17576/jkukm-2025-37(4)-40 |

### 36. Face recognition system at the airport based on internet of things and Cloud Technologies

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | - Muhammad Norhashim; Ahmad Shah; Mohd Kamal; Sahwee; Azizan; Ab Norizan |
| **Objective / Problem** | Improve airport identity checking using face recognition. |
| **Dataset / Data Source** | Airport passenger/fac e data; proposed system. |
| **Method / Approach** | IoT and cloud-based face recognition. |
| **Functionality / Process** | Capture passenger face, compare it with cloud identity data, and verify the passenger at the boarding gate |
| **Tools / Technologies** | Raspberry Pi; cameras; cloud technologies. |
| **Evaluation Metrics** | System/recog nition performance. |
| **Key Findings / Results** | Proposes contactless passenger verification and cloud monitoring. |
| **Weaknesses / Limitations** | Prototype/pro posal; limited quantitative biometric evaluation. |
| **Research Gap / Relevance** | Test accuracy, privacy, liveness and airport-scale deployment. |
| **Official Source / DOI** | https://doi.org/10.37934/kjaas.1.1.3140 |

### 37. Hoge: Integrating feature descriptor and transfer learning for masked face recognition

| Field | Details |
|---|---|
| **Year** | 2026 |
| **Author(s)** | - Chun-Xian Yo; Siew-Chin Chong; Lee-Ying Chong |
| **Objective / Problem** | Improve masked-face recognition. |
| **Dataset / Data Source** | Masked-face image datasets. |
| **Method / Approach** | HOGE: HOG + modified EfficientNet V2-S transfer learning. |
| **Functionality / Process** | Generate HOG image, perform EfficientNet V2-S feature extraction, and recognise the masked face |
| **Tools / Technologies** | HOG; EfficientNet V2-S; transfer learning. |
| **Evaluation Metrics** | Recognition accuracy; model performance. |
| **Key Findings / Results** | Introduces a lightweight HOGE model for masked-face recognition. |
| **Weaknesses / Limitations** | Focused on masked faces; broader spoofing not evaluated. |
| **Research Gap / Relevance** | Test against print/replay attacks and mobile deployment. |
| **Official Source / DOI** | https://doi.org/10.1007/s44163-025-00819-3 |

### 38. AI-powered file security system with facial biometrics, QR code, and OTP verification

| Field | Details |
|---|---|
| **Year** | 2026 |
| **Author(s)** | - Xian Loi; Yee Chan; Zhen Chan |
| **Objective / Problem** | Secure file sharing against impersonatio n and credential theft. |
| **Dataset / Data Source** | System-generated facial/user data; secure file-sharing environment. |
| **Method / Approach** | Facial biometrics + QR authentication + OTP. |
| **Functionality / Process** | Apply AES encryption, perform QR verification, use live facial recognition, and confirm with OTP |
| **Tools / Technologies** | AES-128; facial recognition; QR; OTP. |
| **Evaluation Metrics** | Authenticatio n/security performance. |
| **Key Findings / Results** | Combines facial recognition with two additional authentication layers. |
| **Weaknesses / Limitations** | System-specific; broader biometric attack testing is needed. |
| **Research Gap / Relevance** | Evaluate spoofing, privacy, usability and scalability. |
| **Official Source / DOI** | https://doi.org/10.33093/jiwe.2026.5.2.2 |

### 39. Multi-domain feature alignment for face anti-spoofing

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | -Shizhe Zhang; Wenhui Nie |
| **Objective / Problem** | Improve face anti-spoofing generalisation to unseen domains. |
| **Dataset / Data Source** | CASIA-MFSD, Replay-Attack, MSU-MFSD, and OULU-NPU datasets. |
| **Method / Approach** | Multi-Domain Feature Alignment Domain Generalisatio n, MADG. |
| **Functionality / Process** | Aligns features from different domains to learn more general spoofing features. |
| **Tools / Technologies** | Adversarial learning; domain feature alignment; triplet loss; CNN backbones; PyTorch. |
| **Evaluation Metrics** | Half Total Error Rate (HTER); Area Under Curve (AUC); cross-domain accuracy. |
| **Key Findings / Results** | MADG achieved superior cross-domain generalizatio n (lower HTER, higher AUC) compared to state-of-the-art baselines. |
| **Weaknesses / Limitations** | The method mainly focuses on feature alignment between domains. |
| **Research Gap / Relevance** | Relevant to robust face biometric security. |
| **Official Source / DOI** | https://doi.org/10.3390/s23084077 |

### 40. Privacy-preserving deepfake face image detection

| Field | Details |
|---|---|
| **Year** | 2023 |
| **Author(s)** | - Beijing Chen; Xin Liu; Zhihua Xia; Guoying Zhao |
| **Objective / Problem** | Detect DeepFake faces while protecting private input data. |
| **Dataset / Data Source** | FaceForensic s++, Celeb-DF, and DFDNet benchmark datasets. |
| **Method / Approach** | Secure DeepFake Detection Network, SecDFDNet. |
| **Functionality / Process** | Detects DeepFake faces without directly exposing the input face. |
| **Tools / Technologies** | Additive Secret Sharing (ASS); Secure Multi-Party Computation (SMPC); CNN feature extractors; PyTorch. |
| **Evaluation Metrics** | Detection accuracy (%); Area Under Curve (AUC); computational execution time; communication overhead (MB). |
| **Key Findings / Results** | Achieved high detection accuracy/AU C comparable to plaintext models while ensuring cryptographic privacy. |
| **Weaknesses / Limitations** | Secure computation increases processing and communication cost. |
| **Research Gap / Relevance** | Relevant to privacy-preserving facial biometric security. |
| **Official Source / DOI** | https://doi.org/10.1016/j.dsp.2023.104233 |

### 41. UCDCN: A nested architecture based on central difference convolution for face anti-spoofing

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Jing Zhang; Quanhao Guo; Xiangzhou Wang; Ruqian Hao; Xiaohui Du; Siying Tao; Juanxiu Liu; Lin Liu |
| **Objective / Problem** | Develop an efficient face anti-spoofing model with good generalisation. |
| **Dataset / Data Source** | Replay-Attack, OULU-NPU and SiW. |
| **Method / Approach** | UCDCN based on central difference convolution. |
| **Functionality / Process** | Extracts detailed spoofing features and combines features from different levels. |
| **Tools / Technologies** | CNN, CDC, UNet++, depth supervision. |
| **Evaluation Metrics** | ACER, HTER and cross-dataset performance. |
| **Key Findings / Results** | Achieved strong performance with relatively low model complexity. |
| **Weaknesses / Limitations** | New attack types may still reduce performance. |
| **Research Gap / Relevance** | Relevant to efficient face liveness detection. |
| **Official Source / DOI** | https://doi.org/10.1007/s40747-024-01397-0 |

### 42. Rethinking vision transformer and masked Autoencoder in multimodal face anti-spoofing

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Zitong Yu; Rizhao Cai; Yawen Cui; Xin Liu; Yongjian Hu; Alex C. Kot |
| **Objective / Problem** | Improve multimodal face anti-spoofing using efficient training. |
| **Dataset / Data Source** | WMCA, CASIA-SURF and CASIA-SURF CeFA. |
| **Method / Approach** | Vision Transformer, Masked Autoencoder and Adaptive Multimodal Adapter. |
| **Functionality / Process** | Combines RGB, infrared and depth information for spoof detection. |
| **Tools / Technologies** | ViT, MAE, multimodal adapter. |
| **Evaluation Metrics** | ACER, HTER and cross-domain performance. |
| **Key Findings / Results** | Multimodal learning improved robustness and reduced training cost. |
| **Weaknesses / Limitations** | Requires multimodal datasets and specialised sensors. |
| **Research Gap / Relevance** | Relevant to advanced face presentation attack detection. |
| **Official Source / DOI** | https://doi.org/10.1007/s11263-024-02055-1 |

### 43. Domain generalization via ensemble stacking for face presentation attack detection

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Usman Muhammad; Jorma Tapio Laaksonen; Djamila Romaissa Beddiar; Mourad Oussalah |
| **Objective / Problem** | Improve PAD performance on unseen target domains. |
| **Dataset / Data Source** | WMCA, CASIA-SURF, OULU-NPU, CASIA-MFSD, Replay-Attack, MSU-MFSD and SiW-Mv2. |
| **Method / Approach** | Synthetic data generation with ensemble stacking. |
| **Functionality / Process** | Generates synthetic training data and combines several models. |
| **Tools / Technologies** | Deep Learning, synthetic data, ensemble learning. |
| **Evaluation Metrics** | HTER, EER, APCER, BPCER, ACER and AUC. |
| **Key Findings / Results** | Reported HTER of 8.92% on CASIA-MFSD, 4.81% on MSU-MFSD and 6.70% on OULU-NPU. |
| **Weaknesses / Limitations** | Synthetic data may not fully represent real spoofing attacks. |
| **Research Gap / Relevance** | Relevant to unseen presentation attacks and model generalisation. |
| **Official Source / DOI** | https://doi.org/10.1007/s11263-024-02152-1 |

### 44. Privacy-preserving face recognition method based on extensible feature extraction

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Weitong Hu; Di Zhou; Zhenxin Zhu; Tong Qiao; Ye Yao; Mahmoud Hassaballah |
| **Objective / Problem** | Protect facial data while maintaining recognition efficiency. |
| **Dataset / Data Source** | Face recognition benchmark datasets. |
| **Method / Approach** | Privacy-preserving face recognition with extensible feature extraction. |
| **Functionality / Process** | Extracts face features and compare them in an encrypted environment. |
| **Tools / Technologies** | MobileFaceN et, ResNet-18, ResNet-50 and encryption. |
| **Evaluation Metrics** | Recognition accuracy, data transmission and computational efficiency. |
| **Key Findings / Results** | Maintained high recognition accuracy and improved efficiency compared with baseline methods. |
| **Weaknesses / Limitations** | Encryption still adds computational cost. |
| **Research Gap / Relevance** | Relevant to secure facial biometric data processing. |
| **Official Source / DOI** | https://doi.org/10.1016/j.jvcir.2024.104140 |

### 45. Generating bimodal privacy-preserving data for face recognition

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Darian Tomašević; Fadi Boutros; Naser Damer; Peter Peer; Vitomir Štruc |
| **Objective / Problem** | Generate privacy-preserving facial data for recognition training. |
| **Dataset / Data Source** | Six public face datasets. |
| **Method / Approach** | Identity-conditioned dual-branch GAN. |
| **Functionality / Process** | Generates synthetic visible and near-infrared face images for training. |
| **Tools / Technologies** | GAN, synthetic data, visible and NIR generation. |
| **Evaluation Metrics** | Image quality, recognition accuracy and privacy evaluation. |
| **Key Findings / Results** | Synthetic data supported face recognition training while reducing the use of real identities. |
| **Weaknesses / Limitations** | Synthetic faces may not fully represent real biometric data. |
| **Research Gap / Relevance** | Relevant to privacy-preserving biometric datasets. |
| **Official Source / DOI** | https://doi.org/10.1016/j.engappai.2024.108495 |

### 46. Securing Synthetic Faces: A gan-blockchain approach to privacy-enhanced facial recognition

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | Muhammad Ahmad Nawaz Ul Ghani, Kun She, Muhammad Arslan Rauf, Masoud Alajmi, Yazeed Yasin Ghadi, Abdulmohsen Algarni |
| **Objective / Problem** | Improve privacy and secure management of facial recognition data. |
| **Dataset / Data Source** | CelebA. |
| **Method / Approach** | Privacy-preserving self-attention GAN with clustering and blockchain. |
| **Functionality / Process** | Generates synthetic faces and uses clustering and blockchain for data management. |
| **Tools / Technologies** | GAN, K-means and blockchain. |
| **Evaluation Metrics** | Accuracy, precision, recall, F1, Inception Score and FID. |
| **Key Findings / Results** | Improved privacy protection while maintaining good recognition and image quality results. |
| **Weaknesses / Limitations** | The system has higher complexity due to several technologies. |
| **Research Gap / Relevance** | Relevant to privacy and secure management of facial biometric data. |
| **Official Source / DOI** | https://doi.org/10.1016/j.jksuci.2024.102036 |

### 47. Ethics-aware face recognition aided by synthetic face images

| Field | Details |
|---|---|
| **Year** | 2024 |
| **Author(s)** | - Xiaobiao Du; Xin Yu; Jinhui Liu; Beifen Dai; Feng Xu |
| **Objective / Problem** | Reduce privacy and demographic imbalance issues in face recognition training. |
| **Dataset / Data Source** | Synthetic facial data |
| **Method / Approach** | Race-controllable face synthesis |
| **Functionality / Process** | Generates synthetic faces with controlled demographic characteristics for training. |
| **Tools / Technologies** | Face synthesis and deep learning |
| **Evaluation Metrics** | Recognition accuracy and demographic performance. |
| **Key Findings / Results** | Synthetic data improved recognition accuracy and reduced performance differences between groups. |
| **Weaknesses / Limitations** | Synthetic images may not fully represent real people. |
| **Research Gap / Relevance** | Relevant to privacy, fairness and secure face recognition. |
| **Official Source / DOI** | https://doi.org/10.1016/j.neucom.2024.128129 |

### 48. Face anti-spoofing detection based on novel encoder convolutional neural network and texture’s grayscale structural information

| Field | Details |
|---|---|
| **Year** | 2025 |
| **Author(s)** | Marwa Radad; Amira E. Enab; Salah S. Elagooz; Nawal A. El-Fishawy; Mohamed A. El-Rashidy |
| **Objective / Problem** | Detect face spoofing attacks using facial texture information. |
| **Dataset / Data Source** | NUAA, Replay-Attack and MSU-MFSD |
| **Method / Approach** | Encoder CNN with RGB, grayscale and texture information |
| **Functionality / Process** | Combines colour and texture features to distinguish real and spoof faces. |
| **Tools / Technologies** | CNN, LBP, LTP and SVM |
| **Evaluation Metrics** | HTER, accuracy and computational performance |
| **Key Findings / Results** | Achieved 0.38% HTER on Replay-Attack and showed better results than several comparison methods. |
| **Weaknesses / Limitations** | Performance may change with different cameras and environments |
| **Research Gap / Relevance** | Relevant to practical face anti-spoofing systems |
| **Official Source / DOI** | https://doi.org/10.1007/s44196-025-00757-z |

## Coverage of the Selected Literature

The selected studies collectively provide evidence for the major issues considered in the research topic: robust face presentation attack detection across different domains, threats from deepfakes and adversarial attacks, protection of facial biometric representations, privacy-preserving learning and storage, and practical deployment considerations.
