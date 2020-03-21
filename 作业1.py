import tkinter as tk  # tkinter是python标准绘制GUI库

def han():  # 定义一个函数，用来计算结果与绘制图形
    
    b1 = int(e0.get())  # 用于接收参数
    d1 = int(e1.get())
    b2 = int(e2.get())
    d2 = int(e3.get())
    h1 = int(e4.get())
    d3 = int(e5.get())
    
    s1 = b1*d1+b2*d2+h1*d3 # 计算过程
    s2 = (2*d2*d3+h1*d3+b1*d1-b2*d2)/(2*d3)
    if b2>=b1 :
        s3=1/12*b2*(h1+d1+d2)**3-1/12*b1*h1**3-1/12*(b2-b1)*(h1+d1)**3
    else:
        s3=1/12*b1*(h1+d1+d2)**3-1/12*b2*h1**3-1/12*(b1-b2)*(h1+d2)**3
    t = [s1, s2, s3]  # 整理过程
    e8.config(text=t[0])  # 改变结果值
    e9.config(text=t[1])
    e10.config(text=t[2])
    lo=200
    if d1+d2+h1>=400:
        b1,d1,b2,d2,h1,d3=0.7*b1,0.7*d1,0.7*b2,0.7*d2,0.7*h1,0.7*d3
    else:
        pass
    c1.create_line(lo-b1/2+b1/2-d3/2,lo-(h1+d1+d2)/2+d1,lo-b1/2+(b1-d3)/2,lo+(h1+d1+d2)/2-d2)  # 绘图    
    c1.create_line(lo-b1/2+b1/2+d3/2,lo-(h1+d1+d2)/2+d1,lo-b1/2+b1/2+d3/2,lo+(h1+d1+d2)/2-d2)  
    c1.create_rectangle(lo-b1/2,lo-(h1+d1+d2)/2,lo+b1/2,lo-(h1+d1+d2)/2+d1)
    c1.create_rectangle(lo-b2/2,lo+(h1+d1+d2)/2-d2,lo+b2/2,lo+(h1+d1+d2)/2)

win = tk.Tk()  # 创建一个窗口
win.title("惯性矩")
win.geometry('800x400')

y=['上翼缘板宽b1(mm)','上翼缘板厚d1(mm)','下翼缘板宽b2(mm)','下翼缘板厚d2(mm)','腹板净高h1(mm)','腹板厚d3(mm)','','目的','横截面积(mm^2)','中性轴位置(mm)','截面惯性矩(mm^4)']
ll1=500
ll2=650

for i in range(11):
    exec("l%d = tk.Label(win,text=y[i])"%i)   
    exec("l%d.place(x=ll1, y=20+30*i, anchor='nw')"%i)

for i in range(6):
    exec("e%d = tk.Entry(win)"%i)
    exec("e%d.place(x=ll2, y=20+30*i, anchor='nw')"%i)

e7 = tk.Label(win, text='数值')
e7.place(x=ll2, y=230, anchor='nw')

e8 = tk.Label(win, text=0)  # 用于存放结果
e8.place(x=ll2, y=260, anchor='nw')
e9 = tk.Label(win, text=0)
e9.place(x=ll2, y=290, anchor='nw')
e10 = tk.Label(win, text=0)
e10.place(x=ll2, y=320, anchor='nw')

b1 = tk.Button(win, text="开始计算", width=20,
               command=han)  # 创建一个按钮，用于触发函数
b1.place(x=ll2, y=350, anchor='nw')

c1 = tk.Canvas(win, height=400, width=500)  # 创建一个绘板，用于绘图
c1.place(x=0, y=0, anchor='nw')

win.mainloop()
