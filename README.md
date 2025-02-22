# Crowd Detection Using YOLOv5

This project detects **individual people** and **crowds** in a video using the YOLOv5 object detection model. It processes video frames, identifies people, groups them into crowds based on proximity, and saves the results into two CSV files: one for individual person data and another for crowd data.

## Features
- **Person Detection**: Uses YOLOv5 to detect people in each frame of a video.
- **Crowd Detection**: Groups people into crowds if they are within a specified distance of each other.
- **Persistence Tracking**: Tracks crowds across consecutive frames and saves data if they persist for a minimum number of frames.
- **Data Export**: Saves results into two CSV files:
  - **Individual Person Data**: Contains frame number, person ID, and coordinates.
  - **Crowd Data**: Contains frame number, number of people in the crowd, and person IDs.

## Requirements
- Python 3.7+
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crowd-detection-project.git
   ```
2. Place your video file in the `data/` folder.
3. Run the script:
   ```bash
   python crowd_detection.py
   ```
4. Output files will be saved in the `outputs/` folder.

## Output
- **Individual Person Data (`individual_person_results_*.csv`)**:
  - `Frame Number`: The frame in which the person was detected.
  - `Person ID`: A unique identifier for the person in that frame.
  - `X Coordinate`: The x-coordinate of the person's center.
  - `Y Coordinate`: The y-coordinate of the person's center.

- **Crowd Data (`crowd_detection_results_*.csv`)**:
  - `Frame Number`: The frame in which the crowd was first detected.
  - `Person Count in Crowd`: The number of people in the crowd.
  - `Person IDs in Crowd`: The IDs of the people in the crowd.

## Project Structure
```
crowd-detection-project/
│
├── crowd_detection.py          # Main script for crowd detection
├── requirements.txt            # List of dependencies
├── README.md                   # Project description and instructions
├── LICENSE                     # License file (optional)
├── .gitignore                  # Files/folders to ignore in Git
├── data/                       # Folder for input data (e.g., videos)
│   └── dataset_video.mp4       # Example video file
└── outputs/                    # Folder for output files (e.g., CSV files)
```

## How to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## Acknowledgments
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5) for the object detection model.
- OpenCV, PyTorch, NumPy, and Pandas for enabling this project.

---

This description provides a clear and concise overview of your project, making it easy for others to understand and use. You can copy and paste this into your GitHub repository's `README.md` file. Let me know if you need further assistance! 🚀
