from ultralytics import YOLO

model = YOLO("runs/detect/train/weights/best.pt")

results = model.predict(
    source="dataset/test/images",
    show=True,
    save=True
)