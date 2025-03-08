import cv2
import torch
import os
import numpy as np
from model_loader import models

# Run inference on an image
def detect_objects(image_path, model_type="traffic_violation"):
    """
    Runs YOLOv8 detection on an image and returns the processed image with detections.
    
    Parameters:
    - image_path (str): Path to the input image.
    - model_type (str): 'traffic_violation' or 'pothole' to specify which model to use.
    
    Returns:
    - result_img (numpy array): Image with bounding boxes drawn.
    - detections (list): List of detected objects with class names, confidence scores, and coordinates.
    """

    # Ensure model_type is valid
    if model_type not in models:
        raise ValueError(f"Invalid model type. Choose from: {list(models.keys())}")

    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not load the image. Check the file path.")

    # Run YOLO model inference
    results = models[model_type](image)

    # Extract detections
    detections = []
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Bounding box coordinates
            confidence = float(box.conf[0])  # Confidence score
            class_id = int(box.cls[0])  # Class ID
            class_name = result.names[class_id]  # Get class name

            # Save the detection
            detections.append({
                "class": class_name,
                "confidence": confidence,
                "bbox": [x1, y1, x2, y2]
            })

            # Draw bounding box on the image
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f"{class_name} {confidence:.2f}",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return image, detections

# Example usage
if __name__ == "__main__":
    test_img = "static/test_image.jpg"  # Place a test image in the static folder
    output_img, detected_objects = detect_objects(test_img, model_type="traffic_violation")

    # Save output image for verification
    output_path = "static/output_image.jpg"
    cv2.imwrite(output_path, output_img)

    print("Detection complete! Check:", output_path)
    print("Detected Objects:", detected_objects)
