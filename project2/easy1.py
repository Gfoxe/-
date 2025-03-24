from ctypes import *
from ctypes import wintypes
from time import sleep

#调用Windows系统动态链接库user32.dll

user32 = windll.user32
p = wintypes.POINT()
buffer = create_string_buffer(255)

while True:

    sleep(0.1)
    #获取鼠标位置
    user32.GetCursorPos(byref(p))
    #获取鼠标所处位置的窗口句柄
    HWnd = user32.WindowFromPoint(p)
    #注释掉的代码本来是可以实现星号密码查看的，在Win7以后的系统中失效了
    #dwStyle = user32.GetWindowLongA(HWnd, -16) #-16是GWL_STYLE消息的值
    #user32.SetWindowWord(HWnd, -16, 0)
    sleep(0.1)
    #获取窗口文本
    user32.SendMessageA(HWnd, 13, 255, byref(buffer)) #13是WM_GETTEXT消息的值
    #user32.SetWindowLongA(HWnd, -16, dwStyle)
    print(buffer.value.decode('gbk'))