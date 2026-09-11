import sys

from preprocessing import preprocess_face
from pad_detection import presentation_attack_detection
from feature_extraction import extract_features
from privacy_protection import protect_features


def run_pipeline(image_path):
    print("=== Facial Biometric Authentication Prototype ===")
    print()

    # Step 1: Preprocessing
    print("[1] Preprocessing facial input...")
    processed_image = preprocess_face(image_path)
    print("    ✓ Preprocessing completed.")
    print()

    # Step 2: Presentation Attack Detection
    print("[2] Presentation Attack Detection...")
    pad_result = presentation_attack_detection(processed_image)

    print("    ✓ PAD analysis completed.")
    print(f"    Texture score: {pad_result['texture_score']:.2f}")
    print(f"    Edge score: {pad_result['edge_score']:.4f}")
    print()

    # Step 3: Feature Extraction
    print("[3] Feature Extraction...")
    features = extract_features(processed_image)
    print(f"    ✓ Feature extraction completed.")
    print(f"    Feature length: {len(features)}")
    print()

    # Step 4: Privacy Protection
    print("[4] Privacy Protection...")
    protected_features = protect_features(features)
    print("    ✓ Privacy protection component completed.")
    print()

    # Final output
    print("[5] Authentication Pipeline...")
    print("    ✓ Preliminary pipeline execution completed.")
    print()
    print("=== End of Prototype ===")


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("python main.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]

    try:
        run_pipeline(image_path)
    except Exception as error:
        print(f"Error: {error}")
