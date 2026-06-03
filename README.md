# computer-vision-exercises
OpenCV exercises covering image processing, image tiling, video playback overlays, and side-by-side video composition using Python and OpenCV.

# Computer Vision Exercises

This repository contains OpenCV exercises completed using Python.

## Exercise 1: Basic Drawing & Processing

Features:

* Read image using `cv2.imread()`
* Draw line, rectangle, and circle
* Add text using `cv2.putText()`
* Resize image using `cv2.resize()`
* Crop image using NumPy slicing
* Save processed images

Output:

* Final processed image
* Resized image
* Cropped image

---

## Exercise 2: Image Tiling

Features:

* Read image
* Create a 2×2 tiled image
* Use `cv2.hconcat()` and `cv2.vconcat()`
* Save tiled image

Output:

* Tiled image

---

## Exercise 3: Video Playback Overlay

Features:

* Open video using `cv2.VideoCapture()`
* Read video frames
* Display elapsed and remaining time on each frame
* Print FPS and video information
* Save the first 10 seconds of the processed video

Output:

* Processed video with overlay information

---

## Exercise 4: Side-by-Side Video Player

Features:

* Read video frames
* Duplicate video stream
* Display two synchronized streams side by side
* Save combined video at 1920×1080 resolution

Output:

* Side-by-side combined video

---

## Requirements

* Python 3.x
* OpenCV

Install OpenCV:

```bash
pip install opencv-python
```

## Running the Scripts

Navigate to the appropriate exercise folder and run:

```bash
python exercise1.py
python exercise2.py
python exercise3.py
python exercise4.py
```
