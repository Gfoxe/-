from ultralytics import YOLO
 
model = YOLO("yolov8x.pt")
model.export(format = "onnx")  # export the model to onnx format