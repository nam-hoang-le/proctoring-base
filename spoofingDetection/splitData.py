import os
import random
import shutil
from itertools import islice

# =======================================
outputFolderPath = "dataset/splitData"
inputFolderPath = "dataset/all"
splitRatio = {"train": 0.7, "validation": 0.2, "test": 0.1}
classes = ["fake", "real"]
# =======================================

try:
    # ------------ Remove everything ------------
    shutil.rmtree(outputFolderPath)
except OSError as e:
    os.mkdir(outputFolderPath)


# ------------ Directories to create ------------------
os.makedirs(f"{outputFolderPath}/train/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/train/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/val/labels", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/images", exist_ok=True)
os.makedirs(f"{outputFolderPath}/test/labels", exist_ok=True)

# ------------ Get the unique names ------------------
listNames = os.listdir(inputFolderPath)
uniqueNames = []
for name in listNames:
    uniqueNames.append(name.split(".")[0])
uniqueNames = list(set(uniqueNames))

# ------------ Shuffle the dataset------------------
random.shuffle(uniqueNames)

# ------------ Find the numbers of images for each folder ------------------
lenData = len(uniqueNames)
lenTrain = int(lenData * splitRatio["train"])
lenVal = int(lenData * splitRatio["validation"])
lenTest = int(lenData * splitRatio["test"])

# ------------ Put remaining images in training ------------------
if lenData != lenTrain + lenVal + lenVal:
    remaining = lenData - (lenTrain + lenVal + lenTest)
    lenTrain += remaining
print(f"Total images: {lenData} \nTrain: {lenTrain}, Val: {lenVal}, Test: {lenTest}")

# ------------ Split the list ------------------
lengthToSplit = [lenTrain, lenVal, lenTest]
Input = iter(uniqueNames)
Output = [list(islice(Input, elem)) for elem in lengthToSplit]
# print(Output)

# ------------ Copy the files ------------------
sequence = ['train', 'val', 'test']
for idx, out in enumerate(Output):
    for filename in out:
        shutil.copy(src=f"{inputFolderPath}/{filename}.jpg", dst=f"{outputFolderPath}/{sequence[idx]}/images/{filename}.jpg")
        shutil.copy(src=f"{inputFolderPath}/{filename}.txt", dst=f"{outputFolderPath}/{sequence[idx]}/labels/{filename}.txt")

# ------------ Create data.yaml file ------------------
dataYaml = f'path: ../data/\n\
train: ../train/images\n\
val: ../val/images\n\
test: ../test/images\n\
\n\
nc: {len(classes)}\n\
names: {classes}'

f = open(f"{outputFolderPath}/data.yaml", 'a')
f.write(dataYaml)
f.close()