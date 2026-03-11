from ultralytics import YOLO


model = YOLO("runs/detect/train/weights/best.pt")

metrics = model.val(
    data="dataset/data.yaml",  
    imgsz=640
)

print("Validation complete. Metrics:")
print(metrics)