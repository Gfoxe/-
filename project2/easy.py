import win32con as wcon
import ctypes
from time import sleep
import pyautogui
import pyperclip
from threading import Timer

def isPressed(key):
    return(bool(ctypes.windll.user32.GetAsyncKeyState(key)&0x8000))
# 用0x8000与运算，是因为GetAsyncKeyState()返回的值，最左bit位的0、1分别代表按键状态抬起、按下


ESC=0x1B
LBUTTON = 0x01
press = 0
tm = 0

while True: 
    if(isPressed(LBUTTON)): # 每按下一次鼠标，press就加一
        press += 1
        
        if(press == 2 ):

            pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
            if(pyperclip.paste() == 'true'):
                pyautogui.write('false')
                pyperclip.copy('')

            elif(pyperclip.paste() == 'false'):
                pyautogui.write('true')
                pyperclip.copy('')

            pyperclip.copy('')
                
            press = 0

        
    if(isPressed(ESC)):    # 按下esc退出
        break


