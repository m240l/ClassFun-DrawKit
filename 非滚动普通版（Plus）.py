# coding=utf-8  
import sys  
import tkinter as tk  
import random  
import ctypes  
from open_csv import CSVProcessor  
  
def go_out(event):  
    window.destroy()  
  
def main(event):  
    global var1, lbl  
    show_member = random.choice(data)  
    var1.set(show_member)  
    lbl.config(text="[非滚动版]单击内容下一个，双击内容退出")
  
def setup_window(file_path):  
    user32 = ctypes.windll.user32  
    window = tk.Tk()  
    window.title('随机选择程序')  
    window.geometry('830x340+{}+{}'.format(  
        int((user32.GetSystemMetrics(0) - 830) / 2),  
        int((user32.GetSystemMetrics(1) - 340) / 2) - 40  
    ))  
    window.attributes("-topmost", True)  
    window.resizable(False, False)  
    window.overrideredirect(True)  
  
    bg_label = tk.Label(window, width=150, height=24, bg='#2B2B2B', fg="#AFB1B3")  
    bg_label.place(anchor="nw")
  
    var1 = tk.StringVar(value='即 将 开 始')  
    show_label1 = tk.Label(window, textvariable=var1, justify='left', anchor='center',  
                           width=12, height=2, bg='#353535', font='楷体 -125 bold', foreground='#AFB1B3')
    show_label1.bind("<Double-Button-1>", go_out)  
    show_label1.bind("<Button-1>", main)  
    show_label1.place(anchor='nw', x=28, y=52)  
  
    lbl = tk.Label(window, text='[非滚动版]点击“即将开始”抽取第一个', font=(None, 18), bg='#2B2B2B', fg="#AFB1B3")
    lbl.place(anchor='nw')
  
    return window, var1, lbl  
  
if __name__ == '__main__':  
    try:  
        csv_file_path_1 = sys.argv[1]  
    except Exception:  
        csv_file_path_1 = 'Random_roster.csv'  
  
    processor = CSVProcessor(csv_file_path_1)  
    data = processor.process()  # 调用 process 方法并获取返回结果  
  
    window, var1, lbl = setup_window(csv_file_path_1)  
    window.mainloop()