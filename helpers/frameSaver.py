import cv2
from datetime import datetime
import os


def save(label, frame):
    if (label == "No Mask"):
        filename = str(int(datetime.now().timestamp())) + ".jpg"
        path = "/Users/sumitkushwah/Desktop/maskDetection/ui/non_mask_images"
        cv2.imwrite(os.path.join(path, filename), frame)