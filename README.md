# Proctoring Base

## Overview

This is the repository solutions for challenge from George Washington Institute for Data Science & AI.

The challenge requires me to prove skills in creating functions/models for AI Proctoring systems. 

AI Proctoring, in simple understanding, is a system using AI techniques to support managing the online examination to ensure that participants do the examination with permitted behaviors. 


## Analysis
From the challenge, I created different functions corresponding with detailed documents containing the problem and solutions for each of them: 

1. [Eye Blinking](docs/eyeBlinking/eyeBlinking.md)
2. [Eye Gazing](docs/eyeGazing/eyeGazing.md)
3. [Mouth Opening](docs/mouthOpening/mouthOpening.md)
4. [Head Pose](docs/headPoseEstimation/headPoseEstimation.md)
5. [Optical Character Recognition](docs/opticalCharacterRecognition/opticalCharacterRecognition.md)
6. [Spoofing Detection](docs/spoofingDetection/spoofingDetection.md)
7. [Voice Recorder](docs/voiceRecorder/voiceRecorder.md)
8. [Keypress Detection](docs/keypressDetection/keypressDetection.md)

## Files structure 

```
├── protoringBase
│   ├── data - keep the facial landmarks
│   │   ├── faceLandmarks.dat
│   ├── desmontration - a video introduction all the functions (Updating)
│   ├── docs - document of every functions
│   │   ├── eyeBlinking
│   │   ├── eyeGazing 
│   │   ├── headPoseEstimation
│   │   ├── keypressDetection
│   │   ├── mouthOpening
│   │   ├── opticalCharacterRecognition
│   │   ├── spoofingDetection
│   │   ├── voiceRecorder
================ FUNCTION ================
│   ├── eyeBlinking
│   ├── eyeGazing
│   ├── headPoseEstimation
│   ├── keypressDetection
│   ├── mouthOpening
│   ├── opticalCharacterRecognition
│   ├── spoofingDetection
│   ├── voiceRecorder
│   ├── .gitignore
│   ├── LICENSE
│   ├── README.md
│   ├── requirements.txt
```

## Installation
1. Install important packages:
```
pip install -r requirements.txt 
```
2. For every functions, run as below: 
- For Eye Blinking:
```
cd eyeBlinking 
python main.py
```
- For Eye Gazing:
```
cd eyeGazing 
python mainHor.py
python mainVer.py
```
- For Mouth Opening:
```
cd mouthOpening 
python main.py
```
- For Head Pose Estimation:
```
cd headPoseEstimation 
python main.py
```
- For Optical Character Recogintion: 
```
cd opticalCharacterRecognition
python opticalCharacterRecognition.py 
python opticalCharacterRecognitionMultipleLang.py
```
- For Spoofing Detection: 
```
cd spoofingDetection 
python main.py
```
- For Voice Recorder: 
```
cd voiceRecorder 
python main.py
```
- For Keypress Detection: 
```
cd keypressDetection  
python main.py
```

## Appendix

- [Proctortrack: World's most advanced AI-based online proctoring solution
](https://www.youtube.com/watch?v=ddW_oGy6AfY)
- [Proctorio Explained: How the AI-Based Exam Proctoring System Works
](https://www.youtube.com/watch?v=TGMXnrjXzD4)
- [ProctorExam demo for candidates
](https://www.youtube.com/watch?v=zIePW7DrcD0)
- [How AutoProctor Works
](https://www.youtube.com/watch?v=LoAqvp5rkEM)

## License

The code in this repository is licensed under the MIT License.

Please see LICENSE for details.

## Contact 

Please contact me through lenam1072004@gmail.com