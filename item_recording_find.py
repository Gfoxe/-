import numpy as np
import cv2
import pyautogui
import win32api
screen_width, screen_height = 1920,1080
capture_width, capture_height = 1920,1080

x = screen_width / capture_width
y = screen_height / capture_height

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('screen_capture.avi', fourcc, 100.0, (capture_width, capture_height))



template = cv2.imread("item_recording_find_template_1.png")
theight, twidth = template.shape[:2]
h, w = template.shape[:2]

h1,w1 = h//2,w//2

while True:
    # 获取屏幕截图
    screenshot = pyautogui.screenshot(region=(1,1,screen_width,screen_height))

    # 将截图转换为OpenCV图像
    frame1 = np.array(screenshot)

    # 调整捕获窗口的大小
    frame1 = cv2.resize(frame1, (capture_width, capture_height))
    
    res = cv2.matchTemplate(frame1, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.6
    loc = np.where(res >= threshold)
    coordinates = []
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame1, pt, (pt[0] + w, pt[1] + h),(0,255,0), 1)
        coordinates.append((pt[0], pt[1]))
    
    mouse = win32api.GetCursorPos()
    for coord in coordinates:
        x1 = int(coord[0]+h1)
        y1 = int(coord[1]+w1)
        print(x1,y1)
        #pyautogui.click(x1,y1,clicks=1)
        #win32api.SetCursorPos((x1+h1, y1+w1))


    
    #执行模板匹配，采用的匹配方式cv2.TM_SQDIFF_NORMED
    #result = cv2.matchTemplate(frame1,template,cv2.TM_SQDIFF_NORMED)

    #归一化处理
    #cv2.normalize( result, result, 0, 1, cv2.NORM_MINMAX, -1 )

    #寻找矩阵（一维数组当做向量，用Mat定义）中的最大值和最小值的匹配结果及其位置
    #min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    #匹配值转换为字符串
    #对于cv2.TM_SQDIFF及cv2.TM_SQDIFF_NORMED方法min_val越趋近与0匹配度越好，匹配位置取min_loc
    #对于其他方法max_val越趋近于1匹配度越好，匹配位置取max_loc
    #strmin_val = str(min_val)

    #绘制矩形边框，将匹配区域标注出来
    #min_loc：矩形定点
    #(min_loc[0]+twidth,min_loc[1]+theight)：矩形的宽高
    #(0,0,225)：矩形的边框颜色；2：矩形边框宽度
    #cv2.rectangle(frame1,min_loc,(min_loc[0]+twidth,min_loc[1]+theight),(0,0,225),2)

    # 将屏幕截图写入视频文件
    out.write(frame1)
    cv2.imshow('Screen Capture', frame1)

    # 按'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.destroyAllWindows()
