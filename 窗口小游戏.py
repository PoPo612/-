
import tkinter as tk  # 使用Tkinter前需要先导入
import random
import tkinter.messagebox
number=random.randint(0,100)
# 实例化object，建立窗口window
window = tk.Tk()


# 给窗口的可视化起名字
window.title('猜数字小游戏')

# 设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
# 第4步，在图形界面上设定标签
l1 = tk.Label(window, text='你好！,欢迎来到猜数字小游戏', bg='green', font=('Arial', 12), width=30, height=2)
l2 = tk.Label(window, text='请输入一个数:', bg='white', font=('Arial', 12), width=15, height=1)
# 说明： bg为背景，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 放置标签
l1.pack()# Label内容content区域放置位置，自动调节尺寸
l2.pack(side='left')
# 放置lable的方法有：1）l.pack(); 2)l.place();


# 在图形界面上设定输入框控件entry并放置控件

e = tk.Entry(window, show=None, width=40)  # 显示成明文形式

e.pack(side='right')
def gess_bo():
    a=int(e.get())

    for i in range(1, 6):
        if a < number :
            tkinter.messagebox.showinfo(title='Hi', message='您输入的数太小了')
        elif a > number:
            tkinter.messagebox.showinfo(title='Hi', message='您输入的数太大了')
        else:
            tkinter.messagebox.showinfo(title='Hi', message='恭喜您答对了！')
        window.destroy()

    i=i+1


tk.Button(window, text='猜', bg='green', font=('Arial', 14), command=gess_bo,).pack(side='bottom')
    # 主窗口循环显示

window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。
