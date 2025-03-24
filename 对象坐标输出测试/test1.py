from ultralytics import YOLO   
model =  YOLO('yolov8n.pt')#模型初始化
source='../baka.jpg'#检测图片的路径
results =model(source)
for r in results:
   print(r.boxes.xywh)#以中心点xy坐标、宽、高的顺序打印