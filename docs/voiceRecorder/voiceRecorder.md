# Voice Recorder 

## Problem: 
When the candidates open their mouth, we'll need to record what they talk for the later. 

## Solution: 
Record whenever the candidates open their mouth, combining with the mouth opening function. 

## How-to-do: 
**Step 1:** For good performance, I just used a simple pyaudio and wave library to record the candidates. 

Below are my settings for my machine, note that we may need to change these depending on the machine's specs. 

```
format=pyaudio.paInt16 
channels=1 
rate=44100 
input=True 
frames_per_buffer=1024
```

**Step 2:** I saved it in the *recordings* folder, with the name of the file is the current time, so it's easy for us to keep track later on. 

