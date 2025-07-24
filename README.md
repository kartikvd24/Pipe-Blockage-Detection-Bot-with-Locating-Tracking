# Pipe Blockage Detection Bot with Locating & Tracking

This project is a real-time pipe blockage detection system using an ESP32-CAM module and YOLOv8 model with OpenCV. The bot can navigate inside pipelines, detect blockages using a trained object detection model, and send the live stream over Wi-Fi. The stream is processed on a local machine for real-time detection.
Thins project integrates the hardware with the ML model in which we have used Supervised learning as the datasets for yolov8 were used.its not a conventional Edge AI project but can be categorized as such due to the implementation.

## 📸 Project Media

- `real_time_trial.mp4`: Demonstrates the working of the detection bot in a pipeline environment.
- `bot_image.jpg`: Image showing the full hardware setup of the bot.

> 🛑 **Note:** These media files are for reference only. Please ensure you follow appropriate procedures for large media files in version control.

---

## ⚙️ Hardware Used

| Component             | Description                                      |
|-----------------------|--------------------------------------------------|
| ESP32-CAM             | For capturing real-time video stream             |
| ESP32                 | For location tracking and control of bot         |
| L298N Motor Driver    | For controlling the movement of the bot          |
| 2x DC Motors          | Bot locomotion                                   |
| Chassis               | Bot structural frame                             |
| Power Supply          | Rechargeable 7.4V battery                        |
| Jumper Wires          | For all interconnections                         |
| Arduino IDE           | To flash the ESP32-CAM                           |
| USB to TTL Converter  | To program the ESP32-CAM                         |
| GPS Module(Neo-6sm)   | For location tracking (if included)              |


---


## 🧠 AI Model Used

- **YOLOv8 (You Only Look Once version 8)**
  - Trained on a custom dataset containing images of clean and blocked pipelines.
  - Model detects blockage objects in real-time from the ESP32-CAM video feed.

---

## 🗂 Project Structure
Pipe-Blockage-Detection-Bot-with-Locating-Tracking/
|- bot_image.jpg |
|- real_time_trial.mp4 |
|- main.py |
|- yolov8_model/ | 
|- runs/ |
|- requirements.txt | 
|- README.md |
|- Datasets |
---

## 🚀 How to Run the Project

1. **Flash the ESP32-CAM**
   - Use Arduino IDE.
   - Select `AI Thinker ESP32-CAM` as the board.
   - Upload your ESP sketch (you can use a basic MJPEG stream sketch or a custom sketch that sends video stream over Wi-Fi).
   - also upload the arduino sketch for the location tracking in the ESP32 with the control via the blynk app through the smart phone.  

2. **Get ESP32-CAM Stream URL**
   - After uploading the code, open the **Serial Monitor**.
   - Copy the IP address shown (e.g., `http://192.168.1.104`).
     
3. **Training yolov8 model**
   -open cmd as admin as use the following command-
   ```cmd
   yolo detect train data=your_dataset.yaml model=yolov8n.pt epochs=50 imgsz=640
   ```
  > 🛑 **NOTE** - the .yaml can be creted by our own based on the parameters you are trying to add on the model. 
   
3. **Run Detection Script on Local PC**
   -  Install Python dependencies:

     ```bash
     pip install -r req.txt
     ```
     
   - Open `main.py` and replace the placeholder URL with the ESP32-CAM stream:

     ```python
     url = "http://192.168.x.x"  # Replace with your ESP32-CAM stream address
     ```

   - Run the script:

     ```bash
     python main.py
     ```

4. **Output**
   - The script will open the video stream and apply YOLOv8 detection on the frames in real-time.
   - Detected blockages will be highlighted.
   - The model Efficiceny and the Model training weights can be seen the folder called 'runs' the wreight can be used for dectection and also it contains the parameters that         are been inherited
---

## 🛠 Requirements

- Python 3.8+
- OpenCV
- Ultralytics (YOLOv8)
- NumPy
- ESP32 board package in Arduino IDE

---

## 📌 Notes

- Make sure both your ESP32-CAM and your computer are connected to the same Wi-Fi network.
- This system can be extended by integrating a GPS module and uploading location data to a web server or Firebase.
- The Model took approx.10hrs for traning 50 epochs as per my gpu specifications
- Gpu used for the traning - Nvidia GTX 1650 

---

## 👨‍🔧 Contributors

- **Kartik Desai**  
  Undergraduate Student, DSCE  
  Project on Smart Pipeline Monitoring with Edge AI

---

