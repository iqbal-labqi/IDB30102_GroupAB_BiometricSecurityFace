# Research Gap Analysis

The reviewed literature shows strong progress in face anti-spoofing, cross-domain generalisation, deepfake detection, privacy-preserving facial recognition and practical deployment. The main gap is an **integration and evaluation gap** rather than a claim that the individual components have not been studied.

## Gap 1 – Cross-domain liveness detection remains challenging

Cai et al. (2022), Wang et al. (2022), Huang et al. (2023), Zhang and Nie (2023) and related studies improve robustness to unseen domains, but substantial domain changes can still reduce performance.

## Gap 2 – Liveness and biometric privacy are often separate

Anti-spoofing studies mainly focus on detecting whether the face presentation is genuine, while privacy studies focus on images, features or stored templates. Fewer studies evaluate both requirements together in one authentication pipeline.

## Gap 3 – Privacy mechanisms can add overhead

Encryption, secure computation, blockchain and federated approaches can introduce extra processing, storage or communication cost. This is especially important for edge and IoT environments.

## Gap 4 – Practical systems do not always evaluate complete biometric security

Several attendance and IoT systems demonstrate recognition functionality, but their security evaluation is less comprehensive than dedicated PAD or privacy studies.

## Proposed direction

The proposed research therefore focuses on an integrated lightweight privacy-preserving facial biometric authentication framework combining cross-domain liveness detection with protected facial biometric representations and explicit evaluation of computational cost.
