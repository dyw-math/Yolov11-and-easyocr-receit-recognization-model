import os
HOME = os.getcwd()

# 1. Run inference using the trained model on the test dataset
# Note: Ultralytics saves predictions to a directory like 'runs/detect/predict' or 'runs/detect/predictX'
!yolo detect predict model=runs/detect/train/weights/best.pt source={HOME}/datasets/receit-tel-date-total-2/test/images imgsz=640 conf=0.5 device=0 save=True

# 2. Display a few of the prediction results
import glob
from IPython.display import Image, display

# Find the latest prediction run directory. It's usually 'runs/detect/predict' or 'runs/detect/predictX'
predict_runs = sorted(glob.glob('runs/detect/predict*'))

if predict_runs:
    latest_predict_run_dir = predict_runs[-1]
    print(f"Displaying results from: {latest_predict_run_dir}")

    # Get image paths from the prediction directory
    image_paths = glob.glob(f'{latest_predict_run_dir}/*.jpg') + \
                  glob.glob(f'{latest_predict_run_dir}/*.jpeg') + \
                  glob.glob(f'{latest_predict_run_dir}/*.png')
    image_paths = sorted(image_paths) # Sort for consistent order

    if image_paths:
        print(f"Found {len(image_paths)} predicted images. Displaying the first 3:")
        for image_path in image_paths[:3]:
            display(Image(filename=image_path, width=600))
        print("\n")
    else:
        print(f"No predicted images found in {latest_predict_run_dir}")
else:
    print("No prediction run directories found.")
