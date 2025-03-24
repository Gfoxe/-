import cv2
import numpy as np
from PIL import ImageGrab
import pyautogui
pyautogui.FAILSAFE=False
from ultralytics import YOLO

def get_leftmost_person_center(detections):
    leftmost_center = None
    leftmost_x = float('inf')

    for det in detections:
        cls = det[-1]
        if cls == 0:  # 人类别的索引为0
            x1, y1, x2, y2 = det[:4]
            center_x = (x1 + x2) / 2
            center_y = (y1 + y2) / 2

            if center_x < leftmost_x:
                leftmost_x = center_x
                leftmost_center = (center_x.item(), center_y.item())

    return leftmost_center

# 初始化YOLOv5模型
model = YOLO('yolov8n.pt')

while True:
    # 屏幕截图
    screenshot = ImageGrab.grab()
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 图像输入模型进行检测
    results = model.predict(img)

    # 获得最左侧人的检测框中心位置
    leftmost_center = get_leftmost_person_center(results.boxes.xyxy[0])

    if leftmost_center:
        # 获取当前鼠标位置
        current_position = pyautogui.position()

        # 计算x和y方向上的增量
        delta_x = leftmost_center[0] - current_position[0]
        delta_y = leftmost_center[1] - current_position[1]

        # 平滑移动鼠标到目标位置
        pyautogui.move(delta_x, delta_y, duration=0.25)

        # 打印坐标信息
        print("最左侧人的检测框中心位置：", leftmost_center)