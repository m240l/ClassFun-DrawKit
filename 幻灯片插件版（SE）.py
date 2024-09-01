# coding=utf-8
import sys
if sys.version_info[0] == 2:
  import Tkinter
  from Tkinter import *
else:
  import tkinter as Tkinter
  from tkinter import *
import random
import ctypes
import time
user32 = ctypes.windll.user32
data = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
going = True
is_run = False
def lottery_roll(var1, var2):
  global going
  show_member = random.choice(data)
  var1.set(show_member)
  if going:
    window.after(50, lottery_roll, var1, var2)
  else:
    var2.set('恭喜 {} ！！！'.format(show_member))
    going = True
    return
def lottery_start(var1, var2):
  global is_run
  window.attributes("-alpha", 0.98)
  time.sleep(0.05)
  window.attributes("-alpha", 0.96)
  time.sleep(0.05)
  window.attributes("-alpha", 0.95)
  if is_run:
    return
  is_run = True
  var2.set('幸运儿是你吗。。。')
  lottery_roll(var1, var2)
  lbl["text"] = "点击滚动中的数字数字停止滚动"
def lottery_end():
  global going, is_run
  if is_run:
    going = False
    is_run = False
  window.attributes("-alpha", 0.96)
  time.sleep(0.02)
  window.attributes("-alpha", 0.98)
  time.sleep(0.02)
  window.attributes("-alpha", 1)
  lbl["text"] = "单击数字继续滚动，双击数字退出"
def go_out(event):
    window.destroy()
main_TF = False
def main(event):
  global main_TF
  if main_TF == False:
    main_TF = True
    lottery_start(var1, var2)
    return 0
  main_TF = False
  lottery_end()
if __name__ == '__main__':
  window = Tkinter.Tk()
  window.geometry('830x340+{}+{}'.format(int((user32.GetSystemMetrics(0)-830)/2),int((user32.GetSystemMetrics(1)-340)/2)-40))
  window.attributes ("-topmost",True)
  window.resizable(False,False)
  window.overrideredirect(True)
  bg_label = Label(window, width=150, height=24, bg='#2B2B2B',fg="#AFB1B3")
  bg_label.place(anchor=NW)
  var1 = StringVar(value='即 将 开 始')
  show_label1 = Label(window, textvariable=var1, justify='left', anchor=CENTER, width=12, height=2, bg='#353535',
            font='楷体 -125 bold', foreground='#AFB1B3')
  show_label1.bind("<Double-Button-1>", go_out)
  show_label1.bind("<Button-1>", main)
  show_label1.place(anchor=NW, x=28, y=52)
  var2 = StringVar(value='幸运儿是你吗。。。')
  lbl = Label(window, text='点击“即将开始”开始滚动', font=(None, 18), bg='#2B2B2B',fg="#AFB1B3")  # 创建组件
  lbl.pack()  # 将组件放置在窗口上
  window.mainloop()

### 参考（https://www.jb51.net/article/177913.htm）作者邮箱：m240l@outlook.com