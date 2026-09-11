# IDB30102_GroupAB_BiometricSecurityFace

<h2>Research Title</h2> 
<b>A Lightweight Privacy-Preserving Facial Biometric Authentication Framework with Cross-Domain Liveness Detection</b>
<br>
<br>
<h2>Group Number</h2>
Group AB
<br>
<br>
<h2>Group Member and Student IDs</h2>
1. MUHAMMAD IQBAL BIN RUSLAN - 52215125730<br>
2. MUHAMMAD HUSSAIN KOE BIN MUHAMMAD KHALID KOE - 52215125117<br>
3. IZZUL HARITH BIN IDHAM - 52215251635<br>
4. NUR LYANA YASMIN BINTI KHAMARUKHNIZAM - 52215125726<br>
<br>

<h2>Assigned Research Area</h2>
Biometric Security: Face
<br>
<br>
<h2>Problem Statement</h2>
Despite advancements in facial biometric security, current research exhibits two major operational weaknesses: <br>

- Poor Cross-Domain Liveness Detection Under Unseen Attacks: State-of-the-art liveness detection models perform exceptionally well on controlled benchmark datasets but suffer severe performance degradation (high False Acceptance Rates) when deployed across unseen camera sensors, varying lighting conditions, or against advanced adversarial presentation attacks.

- High Computational Latency from Privacy-Preserving Mechanisms: The implementation of robust privacy mechanisms, such as template encryption or blockchain storage, introduces high processing latency and communication overhead. This makes it extremely difficult to deploy secure biometric authentication on edge computing devices and IoT hardware where computational resources are highly constrained.

<br>
<h2>Research Aim</h2>
The aim of this research is to design, develop, and evaluate a lightweight, privacy-preserving facial biometric authentication framework that enhances cross-domain presentation attack detection while ensuring secure template storage without exceeding the latency constraints of edge devices.

<br>
<br>
<h2>Research Objectives</h2>
To achieve the aim of this study, the following three specific objectives are formulated: <br>

- RO1: To investigate existing facial biometric presentation attack detection methods and template privacy mechanisms to identify vulnerabilities in cross-domain environments and edge deployment.

- RO2: To design and implement a lightweight biometric framework combining deep learning-based cross-domain liveness detection with a low-latency feature encryption mechanism.

- RO3: To evaluate the proposed framework against standard baseline models using classification error metrics (APCER, BPCER, ACER) and execution latency thresholds on standard workstation and edge computing environments.

<br>
<br>
<h2>Scope of the Research</h2>
The scope of this research is defined by its target users and implementation environment: <br>

- Target User: The system is designed for organizations, educational institutions, or smart-campus administrators requiring secure, privacy-compliant facial biometric access control or attendance logging systems.

- Implementation: The research will employ an Experimental methodology and an Iterative and Incremental development model. The prototype will be implemented using Python, leveraging frameworks such as PyTorch or TensorFlow, and standard computer vision libraries (OpenCV). Evaluation will be conducted using benchmark facial anti-spoofing datasets (OULU-NPU) in a controlled laboratory environment. The evaluation will focus strictly on algorithmic error rates (ACER) and computational processing latency (milliseconds) compared against standard unhardened baseline models (e.g., standard FaceNet).


<h2>System Architecture</h2>
<img width="857" height="671" alt="Figure 1" src="https://github.com/user-attachments/assets/145b1822-150b-43c9-b829-07733bfa0b95" />

