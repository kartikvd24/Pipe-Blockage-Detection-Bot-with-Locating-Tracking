import cv2
import torch
from ultralytics import YOLO

# Load YOLO model (Replace with your trained model)
model_path = r"C:\Users\desai\runs\detect\train9\weights\best.pt" # Update this with your trained model path
model = YOLO(model_path)

# Open the laptop camera
cap = cv2.VideoCapture(0)  # 0 for default camera

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Perform inference using YOLO
    results = model(frame)

    # Draw bounding boxes and labels
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get bounding box coordinates
            label = f"{model.names[int(box.cls[0])]}: {box.conf[0]:.2f}"  # Class label with confidence
            
            # Draw rectangle and text
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Pipeline Blockage Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
