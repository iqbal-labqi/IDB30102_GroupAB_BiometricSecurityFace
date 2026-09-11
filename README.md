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

- <b>Poor Cross-Domain Liveness Detection Under Unseen Attacks</b>: State-of-the-art liveness detection models perform exceptionally well on controlled benchmark datasets but suffer severe performance degradation (high False Acceptance Rates) when deployed across unseen camera sensors, varying lighting conditions, or against advanced adversarial presentation attacks.

- <b>High Computational Latency from Privacy-Preserving Mechanisms</b>: The implementation of robust privacy mechanisms, such as template encryption or blockchain storage, introduces high processing latency and communication overhead. This makes it extremely difficult to deploy secure biometric authentication on edge computing devices and IoT hardware where computational resources are highly constrained.

<br>
<h2>Research Aim</h2>
The aim of this research is to design, develop, and evaluate a lightweight, privacy-preserving facial biometric authentication framework that enhances cross-domain presentation attack detection while ensuring secure template storage without exceeding the latency constraints of edge devices.

<br>
<br>
<h2>Research Objectives</h2>
To achieve the aim of this study, the following three specific objectives are formulated: <br>

- <b>RO1</b>: To investigate existing facial biometric presentation attack detection methods and template privacy mechanisms to identify vulnerabilities in cross-domain environments and edge deployment.

- <b>RO2</b>: To design and implement a lightweight biometric framework combining deep learning-based cross-domain liveness detection with a low-latency feature encryption mechanism.

- <b>RO3</b>: To evaluate the proposed framework against standard baseline models using classification error metrics (APCER, BPCER, ACER) and execution latency thresholds on standard workstation and edge computing environments.

<br>
<br>
<h2>Brief Description of the Proposed Solution</h2>
This research proposes a lightweight, privacy-preserving facial biometric authentication framework that integrates cross-domain liveness detection with low-latency feature encryption. The system is designed to significantly reduce spoofing vulnerabilities against unseen attacks while maintaining high processing efficiency suitable for edge computing environments. It uses an Iterative and Incremental development model to build and test preprocessing, liveness detection, feature extraction, and privacy protection modules before final identity matching.
<br>
<br>

<h2>Methodology and Evaluation Plan</h2>
<ul>
  <li><b>Methodology & Development Model:</b> The research employs an <i>Experimental</i> methodology combined with an <i>Iterative and Incremental</i> development model.</li>
  <li><b>Evaluation Plan:</b> The framework will be evaluated using the benchmark <b>OULU-NPU</b> facial anti-spoofing dataset in a controlled laboratory environment. The performance will be compared against a standard unhardened baseline model (e.g., standard FaceNet).</li>
  <li><b>Evaluation Metrics:</b> Algorithmic error rates (APCER, BPCER, ACER) and computational processing latency (in milliseconds).</li>
</ul>

<br>

<h2>System Architecture</h2>
<img width="857" height="671" alt="Figure 1" src="https://github.com/user-attachments/assets/145b1822-150b-43c9-b829-07733bfa0b95" />

<h2>Description of Technical Components Included</h2>
This repository includes preliminary source code components in the <b>04_Source_Code</b> folder to demonstrate the technical direction and feasibility of the proposed framework. The included files are:  <br>

- <b>main.py</b>: Connects the preliminary components into a single processing pipeline. <br> 

- <b>preprocessing.py</b>: Handles initial image preprocessing, including image loading, grayscale conversion, resizing, and pixel normalization. <br>

- <b>pad_detection.py</b>: Provides a preliminary presentation attack detection (PAD) structure. <br>
  
- <b>feature_extraction.py</b>: Converts the processed facial image into a numerical feature representation. <br>
  
- <b>privacy_protection.py</b>: Provides the initial structure for the low-latency feature protection and encryption mechanism.


<br>
<br>

<h2>Programming Languages, Software, and Tools</h2>
The following technologies are designated for the development and evaluation of this research: <br>

- <b>Programming Language</b>: Python
  
- <b>Computer Vision Library</b>: OpenCV (for image preprocessing and face alignment)
  
- <b>Deep Learning Frameworks</b>: PyTorch or TensorFlow (for the PAD model and feature extraction)
  
- <b>Data Processing</b>: NumPy
  
- <b>Benchmark Dataset</b>: OULU-NPU (for cross-domain presentation attack testing and evaluation)
  
<br>
<br>
<h2>Running the Prototype</h2>
Install the required Python packages:

```bash
pip install opencv-python numpy

```
Run the preliminary pipeline using a test facial image:
```
python main.py test_face.jpg
```

