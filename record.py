import cv2
import os
from datetime import datetime

save_folder = "recordVideo"

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_path = os.path.join(save_folder, f'output_{timestamp}.avi')

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(output_path, fourcc, 20.0, (640, 480))

recording = False
brightness = 0 


while True:
    ret, frame = cap.read()
    if not ret:
        break

    adjusted_frame = cv2.convertScaleAbs(frame, alpha=1, beta=brightness)

    if recording:
        out.write(adjusted_frame)

    display_frame = adjusted_frame.copy()
    if recording:
        cv2.circle(display_frame, (30, 30), 10, (0, 0, 255), -1)

    cv2.imshow('Video Recorder', display_frame)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  
        break
    elif key == 32:  
        recording = not recording
     
    elif key == ord('q'):  
        brightness = min(brightness + 10, 100)  

    elif key == ord('w'):  
        brightness = max(brightness - 10, -100)  


cap.release()
out.release()
cv2.destroyAllWindows()
