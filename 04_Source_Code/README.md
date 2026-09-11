# Source Code

This folder contains the preliminary source code components for the proposed lightweight, privacy-preserving facial biometric authentication framework.

The code is provided as a preliminary proof-of-concept to demonstrate the technical direction of the proposed system at the research proposal stage.

## Components

### `main.py`
Connects the preliminary components into a single processing pipeline.

### `preprocessing.py`
Handles the initial image preprocessing, including:
- Image loading
- Grayscale conversion
- Image resizing
- Pixel normalization

### `pad_detection.py`
Provides a preliminary presentation attack detection (PAD) component using basic image texture and edge analysis.

The final implementation is expected to use a deep learning-based PAD model selected during the experimental stage.

### `feature_extraction.py`
Provides a preliminary feature extraction component by converting the processed facial image into a numerical feature representation.

### `privacy_protection.py`
Provides the initial structure for the privacy protection stage.

The final implementation will use a suitable low-latency feature protection or encryption mechanism selected during the development and experimental stages.

## Running the Prototype

Install the required Python packages:

```bash
pip install opencv-python numpy

```
Run the preliminary pipeline using a test facial image:
```
python main.py test_face.jpg
```
