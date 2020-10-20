# coding=utf-8
import sys
if sys.version_info[0] == 2:
  import Tkinter
  from Tkinter import *
else:
  import tkinter as Tkinter
  from tkinter import *
import random
name_list = ['周嘉铖','钱珑超','徐展','尤桉哲','钱涛','黄舒怡','胡志辉','吴昭耀','陈萌萌','郑巧悦','陈艳','梁明皓','蒋俊超','徐颖','倪宏涛','潘梦倩','俞靖庐','王中阳','毛贞强','张嫒','朱速航','陈涛','陆元超','叶振雄','奚申杰','叶梦婷','徐丽丽','潘艳']
going = True
is_run = False
def name_roll(var1, var2):
  global going
  show_member = random.choice(name_list)
  var1.set(show_member)
  if going:
    window.after(50, name_roll, var1, var2)#after起到一个定时器的效果
  else:
    var2.set('恭喜 {} ！！！'.format(show_member))
    going = True
    return
def name_start(var1, var2):
  global is_run
  if is_run:
    return
  is_run = True
  var2.set('祝你玩得开心')
  name_roll(var1, var2)
def name_end():
  global going, is_run
  if is_run:
    going = False
    is_run = False
if __name__ == '__main__':
  window = Tkinter.Tk()
  window.geometry('400x400')
  window.title('   随 机 点 名')
  l1 = Label(window, width=70, height=24, bg='#ECf5FF')
  l1.place(anchor=NW, x=0, y=0)
  var1 = StringVar(value='即 将 开 始')
  label1 = Label(window, textvariable=var1, justify='left', anchor=CENTER, width=17, height=3, bg='#009393',
            font='楷体 -40 bold', foreground='black')
  label1.place(anchor=NW, x=21, y=20)
  var2 = StringVar(value='欢迎您，点击开始抽取幸运儿')
  label2 = Label(window, textvariable=var2, justify='left', anchor=CENTER, width=38, height=3, bg='#ECf5FF',
            font='楷体 -18 bold', foreground='black')
  label2.place(anchor=NW, x=21, y=240)
  button1 = Button(window, text='开始', command=lambda: name_start(var1, var2), width=14, height=2, bg='white',
           font='宋体 -18 bold')
  button1.place(anchor=NW, x=20, y=175)
  button2 = Button(window, text='结束', command=lambda: name_end(), width=14, height=2, bg='white',
           font='宋体 -18 bold')
  button2.place(anchor=NW, x=232, y=175)
  window.mainloop()