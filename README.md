# Eye Motion Tracking 

## Overview 

### About Eye Motion Tracking
I used Dlib and OpenCV libraries to take the information from the webcam, then use the [Landmark Points](docs/landmark_points.jpg) from the Dlib to examine if the eye is closed or open (Eye-blinking) and whether the user is looking at the center, left or right.


## Process 
1. Use CV and Dlib to read the image from the camera
2. 

## Installation
1. Deactivate your current environment 
```
conda deactivate 
```
2. Create a new environment and download the prerequisite
```
conda env create -f environment.yml
```

3. Check the environment list: 
```
conda env list
```
4. Activate the environment (make sure the name of the environment is correct): 
```
conda activate eye-motion-tracking
```
5. Download Dlib library (Or you can copy the download link in [this website](https://pypi.org/simple/dlib/)):
```
python -m pip install https://files.pythonhosted.org/packages/0e/ce/f8a3cff33ac03a8219768f0694c5d703c8e037e6aba2e865f9bae22ed63c/dlib-19.8.1-cp36-cp36m-win_amd64.whl#sha256=794994fa2c54e7776659fddb148363a5556468a6d5d46be8dad311722d54bfcf
```
