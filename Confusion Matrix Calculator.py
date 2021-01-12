##################################################
## Confusion Matrix Calculator
##################################################
## Takes 2 binary map image files as input, prints
## confusion matrix derivations.
##################################################
## Author: Jordan Kee
## Date: 2020-10-30
##################################################

import cv2
import numpy as np

# Read image files
ground_truth = cv2.imread('E:/University Local/FYP/Test Data/2/Frames/Ground Truth/3.png', 0)
output = cv2.imread('E:/University Local/FYP/Test Data/2/Frames/deeplabv3/3.png', 0)

# Apply thresholding on image files to convert them to binary maps.
ret, ground_truth = cv2.threshold(ground_truth,127,255,cv2.THRESH_BINARY)
ret, output = cv2.threshold(output,127,255,cv2.THRESH_BINARY)

# Get dimensions of binary maps
(height, width) = np.shape(output)

TP = 0
FP = 0
FN = 0
TN = 0

for x in range(height):
    for y in range(width):
        if ground_truth[x, y] == 255 and output[x, y] == 255:
            TP += 1
        elif ground_truth[x, y] == 0 and output[x, y] == 255:
            FP += 1
        elif ground_truth[x, y] == 255 and output[x, y] == 0:
            FN += 1
        elif ground_truth[x, y] == 0 and output[x, y] == 0:
            TN += 1

TPR = TP / (TP + FN)
TNR = TN / (TN + FP)
FPR = FP / (FP + TN)
FNR = FN / (FN + TP)

Accuracy = (TP + TN) / (TP + TN + FP + FN)
BalancedAccuracy = (TPR + TNR) / 2
F1 = 2 * TP / (2 * TP + FP + FN)
MCC = (TP * TN - FP * FN) / (((TP + FP) * (TP + FN) * (TN + FP) * (TN + FN)) ** 0.5)

print("TP", TP)
print("FP", FP)
print("FN", FN)
print("TN", TN)
print("F1", F1)