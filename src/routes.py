from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from inference import detect_objects

app = Flask(__name__)

# Create an uploads folder if it doesn't exist
UPLOAD_FOLDER = "static/uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "mp4"}

def allowed_file(filename):
    """Check if the file extension is allowed."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

# image detection
@app.route("/detect_image", methods=["POST"])
def detect_image():
    """
    API to detect objects in an uploaded image.
    Returns detected objects in JSON format.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    model_type = request.form.get("model_type", "traffic_violation")  # Default to traffic violation

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Run YOLO detection
        _, detections, output_path = detect_objects(file_path, model_type=model_type)

        return jsonify({
            "message": "Detection complete",
            "model_used": model_type,
            "detected_objects": detections,
            "processed_image": output_path
        })
    else:
        return jsonify({"error": "Invalid file format"}), 400

# video detection
@app.route("/detect_video", methods=["POST"])
def detect_video():
    """
    API to detect objects in an uploaded video.
    Returns the processed video path.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]
    model_type = request.form.get("model_type", "traffic_violation")  # Default to traffic violation

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        # Run YOLO detection on video
        output_video_path, _ = detect_objects(file_path, model_type=model_type, is_video=True)

        return jsonify({
            "message": "Video processing complete",
            "model_used": model_type,
            "processed_video": output_video_path
        })
    else:
        return jsonify({"error": "Invalid file format"}), 400

# home route
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AI Traffic Violation & Pothole Detection API is running!"})

if __name__ == "__main__":
    app.run(debug=True)
