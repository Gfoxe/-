import cv2
img = cv2.imread('baka.jpg')
show = cv2.imshow('test',img)
def show_xy(A,X,Y,B,C):
    print(A,X,Y,B,C)
while True:
    keycode = cv2.waitKey(0)
    code = chr(keycode)
    print(keycode,code)
    cv2.setMouseCallback('test',show_xy)
    if keycode == 27:
        break
cv2.destroyAllWindows()
