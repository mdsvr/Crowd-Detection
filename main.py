import cv2
import torch
import numpy as np
import pandas as pd
from collections import defaultdict
from datetime import datetime

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Function to calculate distance between two points
def calculate_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Function to detect crowds
def detect_crowd(persons, threshold_distance=100):
    crowds = []
    for i in range(len(persons)):
        group = [i]
        for j in range(i + 1, len(persons)):
            if calculate_distance(persons[i], persons[j]) < threshold_distance:
                group.append(j)
        if len(group) >= 3:
            crowds.append(group)
    return crowds

# Process video
def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_number = 0
    crowd_history = defaultdict(list)
    results_crowds = []
    results_individuals = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Detect persons using YOLOv5
        results_yolo = model(frame)
        detections = results_yolo.xyxy[0].cpu().numpy()
        persons = [((x1 + x2) / 2, (y1 + y2) / 2) for x1, y1, x2, y2, conf, cls in detections if int(cls) == 0]
        print(f"Frame {frame_number}: Detected {len(persons)} persons")

        # Save individual person data
        for idx, person in enumerate(persons):
            results_individuals.append({
                'Frame Number': frame_number,
                'Person ID': idx,
                'X Coordinate': person[0],
                'Y Coordinate': person[1]
            })

        # Detect crowds in the current frame
        crowds = detect_crowd(persons)
        print(f"Frame {frame_number}: Detected {len(crowds)} potential crowds")

        # Update crowd history
        for crowd in crowds:
            crowd_key = tuple(sorted(crowd))
            crowd_history[crowd_key].append(frame_number)
            print(f"Crowd {crowd_key} updated: {crowd_history[crowd_key]}")

        # Check for persistent crowds
        for crowd_key, frames in list(crowd_history.items()):
            if len(frames) >= 3: 
                results_crowds.append({
                    'Frame Number': frames[0],
                    'Person Count in Crowd': len(crowd_key),
                    'Person IDs in Crowd': crowd_key
                })
                print(f"Crowd {crowd_key} persisted for {len(frames)} frames. Saving to CSV.")
                del crowd_history[crowd_key]

        frame_number += 1

    cap.release()

    # Generate unique CSV file names with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_csv_crowds = f'crowd_detection_results_{timestamp}.csv'
    output_csv_individuals = f'individual_person_results_{timestamp}.csv'
    print(f"Saving crowd results to {output_csv_crowds}")
    print(f"Saving individual person results to {output_csv_individuals}")

    # Save results to CSV
    df_crowds = pd.DataFrame(results_crowds)
    df_individuals = pd.DataFrame(results_individuals)
    df_crowds.to_csv(output_csv_crowds, index=False)
    df_individuals.to_csv(output_csv_individuals, index=False)

# Example usage
video_path = 'F:/task3/dataset_video.mp4' 
process_video(video_path)