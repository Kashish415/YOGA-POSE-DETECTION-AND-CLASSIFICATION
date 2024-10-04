# Yoga Pose Detection and Classification

This project detects and classifies five custom-trained yoga poses using computer vision techniques. The system can identify the following poses:

- Cobbler's Pose (Baddha Konasana)
- Bridge Pose (Setu Bandhasana)
- Dandasana (Staff Pose)
- Vrikshasana (Tree Pose)
- Vibhadhrasana (Warrior Pose)
  
## Project Overview

The objective of this project is to build a real-time yoga pose detection system that helps users identify and correct their poses during practice. The system uses keypoint detection to extract body landmarks and classifies the yoga pose based on the trained model.

## Features:

- Real-time pose detection using a webcam.
- Provides feedback on which pose is detected.
- Trained on custom datasets for accurate classification of the yoga poses.
  
## Technologies Used:

- Python: Main programming language.
- OpenCV: For image and video processing.
- MediaPipe: To detect key body landmarks.
- TensorFlow/Keras: For training the pose classification model.
  
## Installation

1. Clone the repository:

   git clone https://github.com/Kashish415/YOGA-POSE-DETECTION-AND-CLASSIFICATION

2. Download or train the model and place it in an appropriate folder.


## Dataset

The project was trained on a custom dataset comprising images of the five yoga poses. If you'd like to train the model with your own data, you can use the provided data_collection.py and data_training.py scripts.

## Contributions

Feel free to fork this repository, submit pull requests, or open issues for any bugs or suggestions.
