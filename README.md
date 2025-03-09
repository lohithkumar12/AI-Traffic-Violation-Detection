# 🚦 AI-Powered Traffic Violation & Pothole Detection System  

## 🔥 Project Overview  
This project is an **AI-powered system** that detects **traffic violations** (wrong-way driving, red-light running, etc.) and **road conditions** (potholes, cracks, lane damage) using **YOLOv8 object detection**.  

### **✨ Key Features**  
✅ **Traffic Violation Detection** – Identifies violations such as motorcycle on pedestrian road, jaywalking, and more.  
✅ **Pothole Detection** – Detects potholes and road damages for better infrastructure monitoring.  
✅ **Real-time Detection API** – Uses a Flask backend to process images & videos.  
✅ **Interactive Dashboard** – A **Streamlit-powered UI** for real-time monitoring & analysis.  
✅ **Live Detection Statistics** – Displays violation counts, trends, and a heatmap of detections.  

---

## **🛠️ Tech Stack**  
| Component  | Technology |
|------------|------------|
| **Object Detection** | YOLOv8 |
| **Backend API** | Flask |
| **Frontend Dashboard** | Streamlit |
| **Data Processing** | OpenCV, NumPy, Pandas |
| **Visualization** | Plotly, Folium (for live maps) |
| **Version Control** | Git & GitHub |

---

## **🚀 Installation & Setup**  

### **📌 Step 1: Clone the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/AI-Traffic-Violation-Detection.git
cd AI-Traffic-Violation-Detection
```

### **📌 Step 2: Create a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate     
```

### **📌 Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **📌 Step 4: Run the Flask API**  
```bash
python src/routes.py
```
- The API should now be running at **`http://127.0.0.1:5000/`**.  
- You can test it by opening the URL in your browser.  

### **📌 Step 5: Start the Streamlit Dashboard**  
In a new terminal, run:  
```bash
streamlit run src/dashboard.py
```
- The dashboard should open at **`http://localhost:8501/`**.  

---

## **📸 How to Use?**  
1️⃣ **Upload an Image or Video** via the Streamlit UI.  
2️⃣ **Select the Model Type** (`Traffic Violation` or `Pothole`).  
3️⃣ **View Results** with detections highlighted.  
4️⃣ **Check Analytics** – Live detection statistics & violation trends.  

---

## **📊 Live Dashboard Features**  
🔹 **Upload images & videos for detection**  
🔹 **Track detected violations & potholes over time**  
🔹 **View recent detections with confidence scores**  
🔹 **See detected locations on an interactive map**  
🔹 **Monitor real-time detection trends**  

---

## **🔗 API Endpoints**
| Method | Endpoint | Description |
|--------|------------|------------|
| **POST** | `/detect_image` | Upload an image for detection |
| **POST** | `/detect_video` | Upload a video for detection |
| **GET** | `/get_detection_stats` | Get total violation & pothole counts |
| **GET** | `/get_recent_detections` | Get last 5 detections |
| **GET** | `/get_detection_locations` | Get detected locations on the map |

---

## **📦 Project Structure**  
AI-Traffic-Violation-Detection/
│── models/                 # YOLOv8 trained models
│── src/
│   ├── inference.py        # YOLO detection functions
│   ├── routes.py           # Flask API
│   ├── dashboard.py        # Streamlit dashboard
│── static/
│   ├── uploads/            # Stores processed images & videos
│── requirements.txt        # Required dependencies
│── README.md               # Project documentation
│── .gitignore              # Ignore unnecessary files


🎯 **Star the repository if you like this project!**
📢 **Have suggestions? Feel free to open an issue!**  

