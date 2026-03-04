!ls runs/detect/train*
!yolo detect train data=datasets/receit-tel-date-total-2/data.yaml model=yolo11n.pt epochs=100 imgsz=640

from IPython.display import Image, display

# Assuming the latest run is in 'runs/detect/train'
# You might need to change 'train' to 'train2', 'train3', etc., based on the previous output
last_run_dir = 'runs/detect/train'

print(f"Displaying results from: {last_run_dir}")

display(Image(filename=f'{last_run_dir}/results.png', width=800))
display(Image(filename=f'{last_run_dir}/confusion_matrix.png', width=800))

# You can also check other plots like F1_curve.png, P_curve.png, R_curve.png, etc.
# For example, to see a batch with predictions:
# display(Image(filename=f'{last_run_dir}/val_batch0_pred.jpg', width=800)).

