# Face Recognition in Video Files

## Overview
This project demonstrates a face recognition system that processes video files to detect and recognize faces using pre-trained facial encodings. The system takes an input video, processes each frame to identify faces, and outputs a video with the recognized faces labeled.

## Features
- Detects faces in video frames using the `face_recognition` library.
- Recognizes and labels known faces using pre-trained facial encodings.
- Outputs a processed video with bounding boxes and names around recognized faces.
- Optionally displays the video frames in real-time during processing.

## Requirements
- Python 3.x
- OpenCV
- face_recognition
- imutils
- argparse
- pickle

## Usage
To run the face recognition system on a video file, use the following command:

```bash
python recognize_faces_video_file.py --encodings encodings.pickle --input {path to input video} --output {path to output video} --display 0
