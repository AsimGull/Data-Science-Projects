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

Arguments
--encodings: Path to the serialized database of facial encodings.
--input: Path to the input video file.
--output: Path to the output video file.
--display: Whether or not to display the output frame to the screen (1 to display, 0 to not display).
--detection-method: Face detection model to use: either hog or cnn (default: cnn).
Project Structure
recognize_faces_video_file.py: The main script to run the face recognition system.
encodings.pickle: A serialized file containing pre-trained facial encodings.
Example
To run the face recognition on a sample video, you might use:

python recognize_faces_video_file.py --encodings encodings.pickle --input sample_video.avi --output output_video.avi --display 1

How It Works
Loading Encodings: The script loads the known facial encodings from a pickle file.
Processing Video: It processes the input video frame by frame.
Face Detection and Recognition: For each frame, it detects faces and compares them against the known encodings.
Annotating Frames: Recognized faces are labeled, and bounding boxes are drawn around them.
Output: The processed video is written to the specified output file, and optionally displayed in real-time.
Contributing
Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.


This format should make it easy for users to understand the purpose and functionality of your project, as well as how to set it up and run it.

