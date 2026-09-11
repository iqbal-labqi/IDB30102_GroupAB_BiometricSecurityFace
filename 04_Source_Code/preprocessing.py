import cv2

def preprocess_face(image_path):
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Unable to load the input image.")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (224, 224))
    normalized = resized / 255.0

    return normalized
