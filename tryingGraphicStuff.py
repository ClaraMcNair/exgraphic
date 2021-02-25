rom graphics import *
import time

win = GraphWin("cool",500, 500)
pt = Point(250,250)
cir = Circle(pt,100)

print('Hello. Can you read this?')

def bePINK():
  for x in range (255):
      if x<254:
        win.setBackground(color_rgb(x,0,255))
        time.sleep(0.03)
      else:
        beBLUE()


def beBLUE():
  for x in range (255,0,-1):
    if x >1:
      win.setBackground(color_rgb(x,0,255))
      time.sleep(0.03)
    else:
      bePINK()
    

beBLUE()
