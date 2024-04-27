# Key Press Detection

## Problem 

The candidates may press keys on the keyboard to do suspicious actions. 

## Solution 

Keep track whenever they do that. 

## How-to-do

**Step 1:**
I basically use the keyboard libraries and the read_key() function. I created a list of restricted keys, now containing: ctrl, tab and prtsc. 

**Step 2:** 
I stored the information on the *tracking* folder with the file name is the time of the action.