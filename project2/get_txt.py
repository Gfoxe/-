from win32gui import *
from win32api import *
from win32process import *
import win32con
import time
time.sleep(3)
# 获取窗体句柄
hWnd = GetForegroundWindow()
print('hownd: ', hWnd)
FormThreadID = GetCurrentThreadId()
print('FormThreadID: ', FormThreadID)
CWndThreadID = GetWindowThreadProcessId(hWnd)
print('CWndThreadID: ', CWndThreadID)
AttachThreadInput(CWndThreadID[0], FormThreadID, True)
# 获取光标所在文本框句柄
hWnd = GetFocus()
print('hWnd: ', hWnd)
AttachThreadInput(CWndThreadID[0], FormThreadID, False)
# SendMessage(hWnd, win32con.WM_SETTEXT, 0, "mextb1860 第一个文本框")
# 文本框内容长度
length = SendMessage(hWnd, win32con.WM_GETTEXTLENGTH)+1
print('Length: ', length)
buf = '0'*length
# 生成buffer对象
# buf = PyMakeBuffer(length)
# 获取文本框内容
print('get: ', SendMessage(hWnd, win32con.WM_GETTEXT, length, buf))
print('text: ', buf)