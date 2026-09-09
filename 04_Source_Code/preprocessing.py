import cv2


def preprocess_face(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to load the input image.")

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize image for consistent processing
    resized = cv2.resize(gray, (224, 224))

    # Normalize pixel values
    normalized = resized / 255.0

    return normalized


if __name__ == "__main__":
    image_path = "sample_face.jpg"

    processed_image = preprocess_face(image_path)

    print("Preprocessing completed.")
    print("Processed image shape:", processed_image.shape)
