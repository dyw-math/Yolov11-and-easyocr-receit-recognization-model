%pip install "ultralytics<=8.3.40" supervision roboflow
# prevent ultralytics from tracking your activity
!yolo settings sync=False
import ultralytics
ultralytics.checks()

!pip install roboflow
from roboflow import Roboflow
rf = Roboflow(api_key="XJjcrta5pDq3kAuiYkjN")
project = rf.workspace("rbfl7dyw").project("receit-tel-date-total")
version = project.version(2)
dataset = version.download("yolov11")

!pip install ultralytics
!python -m ultralytics.cli help

print(f'Your dataset is located in: {HOME}/yolov11')
!ls {HOME}/yolov11

# Create the 'datasets' directory if it doesn't exist
!mkdir -p datasets

# Move the downloaded dataset into the 'datasets' directory
!mv receit-tel-date-total-2 datasets/
