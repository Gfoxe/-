import cv2
import numpy as np
import YOLODet
import gradio as gr

model = 'yolov8n.onnx'
yolo_det = YOLODet(model, conf_thres=0.5, iou_thres=0.3)

def det_img(cv_src):
    yolo_det(cv_src)
    cv_dst = yolo_det.draw_detections(cv_src)

    return cv_dst

if __name__ == '__main__':

     input = gr.Image()
     output = gr.Image()

     demo = gr.Interface(fn=det_img, inputs=input, outputs=output)
     demo.launch()
