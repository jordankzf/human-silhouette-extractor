##################################################
## MOG2 / GMG Silhouette Extractor
##################################################
## Takes video file as input, generates silhouette
## mask and saves it.
##################################################
## Author: Jordan Kee
## Date: 2020-10-25
##################################################

import cv2
import time

# Loads video file into CV2
cap = cv2.VideoCapture('1_source.mp4')

# Get video file's dimensions
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Creates output video file
# out = cv2.VideoWriter('1_gmg.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 30, (frame_width,frame_height))

# Create SE to be used as kernel during morphological operation
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))

# Creates subtractor, uncomment appropriate line to use either MOG2 or GMG
# subtractor = cv2.createBackgroundSubtractorMOG2()
subtractor = cv2.bgsegm.createBackgroundSubtractorGMG(10, .8)

prev_frame_time = 0
new_frame_time = 0

while(cap.isOpened):
    # Read each frame one by one
    ret, frame = cap.read()
    # Run if there are still frames left
    if (ret):
        # Apply background subtraction to extract foreground (silhouette)
        mask = subtractor.apply(frame)
        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time 
        fps = str(fps)
        print(fps)
        # Convert binary mask to BGR to allow saving
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
        
        # OPTIONAL: Apply opening operation to close gaps..
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
        # Apply thresholding to convert mask to binary map
        ret, thresh = cv2.threshold(mask,127,255,cv2.THRESH_BINARY)
        
        # Write processed frame to output file
        # out.write(thresh)
        
        #Display mask
        cv2.imshow('Silhouette Extractor', thresh)
        
        # Allow early termination with Esc key
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    # Break when there are no more frames    
    else:
        break


# Release resources
cap.release()
# out.release()
cv2.destroyAllWindows()