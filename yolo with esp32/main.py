from ultralytics import YOLO
import cv2

# Replace with your ESP32-CAM stream URL
ESP32_STREAM_URL = "http://192.168.197.187:81/stream"

def main():
    cap = cv2.VideoCapture(ESP32_STREAM_URL)  # Open MJPEG stream
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)  # Reduce buffering delay

    if not cap.isOpened():
        print("Error: Unable to open ESP32-CAM stream")
        return

    model = YOLO(r'C:\Users\desai\runs\detect\train9\weights\best.pt')  # Load trained YOLO model

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Warning: No frame received, reconnecting...")
            cap.release()
            cap = cv2.VideoCapture(ESP32_STREAM_URL)
            continue

        frame = cv2.resize(frame, (320, 240))  # Resize to QVGA

        # Perform YOLO object detection
        results = model(frame, agnostic_nms=True, show=True)

        # Process detected objects
        for result in results:
            if result.boxes is None:
                continue  # Skip if no detections

            detection_count = len(result.boxes)
            for i in range(detection_count):
                cls = int(result.boxes.cls[i].item())  # Get class ID
                name = model.names[cls]  # Get class name
                print(name)  # Print detected object name

        # Exit on 'ESC'
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
