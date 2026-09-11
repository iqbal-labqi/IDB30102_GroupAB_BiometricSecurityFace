import cv2
import numpy as np


def presentation_attack_detection(processed_image):
    """
    Preliminary heuristic presentation attack detection (PAD).

    The final implementation will use a deep learning-based
    PAD model selected during the experimental stage.
    """

    if processed_image is None:
        raise ValueError("Processed image is required.")

    # Convert normalized image back to 8-bit format
    image = (processed_image * 255).astype("uint8")

    # Measure image texture
    texture_score = cv2.Laplacian(image, cv2.CV_64F).var()

    # Detect edges
    edges = cv2.Canny(image, 50, 150)

    # Calculate edge percentage
    edge_score = cv2.countNonZero(edges) / edges.size

    return {
        "texture_score": texture_score,
        "edge_score": edge_score
    }


if __name__ == "__main__":
    print("Preliminary PAD component initialized.")
