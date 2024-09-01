import tkinter as tk
from PIL import Image, ImageTk
import os
import sys
import random
import ctypes
from open_csv import CSVProcessor
import pkg_resources
import io


windows_state = False

def go_out(event):
    global window,windows_state
    windows_state = False
    window.destroy()
    
  
def main(event):  
    global lbl,data,show_label1
    show_member = random.choice(data)
    show_label1.config(text=show_member)
    lbl.config(text="[非滚动版]单击内容下一个，双击内容退出")
    window.update_idletasks()
  
def setup_main_window(file_path):
    global window,lbl,show_label1
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
  
    show_label1 = tk.Label(window, text="即 将 开 始", justify='left', anchor='center',width=12, height=2, bg='#353535', font='楷体 -125 bold', foreground='#AFB1B3')
    show_label1.bind("<Double-Button-1>", go_out)  
    show_label1.bind("<Button-1>", main)  
    show_label1.place(anchor='nw', x=28, y=52)  
    window.update_idletasks()
    lbl = tk.Label(window, text='[非滚动版]点击“即将开始”抽取第一个', font=(None, 18), bg='#2B2B2B', fg="#AFB1B3")
    lbl.place(anchor='nw')
  
    return window, lbl  

    # ... 此处是原setup_window函数内容，但使用Toplevel代替Tk，且不立即调用mainloop()
    # 注意修改window为top_level_window或其他合适名称以避免混淆
    pass

def open_main_window(event):
    global data, lbl, top_level_window,window,windows_state
    
    if windows_state:
        window.destroy()
        
    windows_state = True

    try:
        csv_file_path_1 = sys.argv[1]
    except IndexError:
        csv_file_path_1 = 'Random_roster.csv'
    
    processor = CSVProcessor(csv_file_path_1)
    data = processor.process()
    
    window, lbl = setup_main_window(csv_file_path_1)
    window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())  # 确保子窗口关闭时能释放资源
    window.mainloop()

def on_drag_start(event):
    global dragging, drag_x, drag_y  
    dragging = True  
    drag_x = event.x  
    drag_y = event.y  
    pass

def on_drag_motion(event):
    global dragging, drag_x, drag_y  
    if dragging:  
        root.geometry(f"+{event.x_root - drag_x}+{event.y_root - drag_y}") 
    pass

def on_drag_end(event):
    global dragging  
    dragging = False
    pass

root = tk.Tk()
root.title("透明可拖动窗口")  
  
# 设置窗口初始大小和位置  
screen_width = root.winfo_screenwidth()  
screen_height = root.winfo_screenheight()  
window_width = 64  
window_height = 64  
initial_x = 100  # 减去一些偏移量以确保窗口不会完全位于屏幕边缘  
initial_y = screen_height - window_height - 100
root.geometry(f"{window_width}x{window_height}+{initial_x}+{initial_y}")  
  
# 设置窗口属性  
root.resizable(False, False)  # 不允许修改大小  
root.overrideredirect(True)  # 不显示标题栏  
root.wm_attributes('-transparentcolor', '#1e1e1e')  # 设置透明色  
root.wm_attributes('-alpha', 0.5)  # 设置窗口透明度  
root.wm_attributes('-topmost', True)  # 设置窗口始终在最上方  
  
# 加载图片并创建Label

image_data = pkg_resources.resource_string(__name__, 'logo.png')
image_file = io.BytesIO(image_data)
image = Image.open(image_file)
photo_image = ImageTk.PhotoImage(image)  
image_label = tk.Label(root, image=photo_image)  
image_label.pack(fill=tk.BOTH, expand=tk.YES)  
  
# 拖动窗口的变量  
dragging = False  
drag_x = 0  
drag_y = 0  

# 绑定双击事件打开新窗口
root.bind('<Double-Button-1>', open_main_window)
root.bind('<Button-1>', on_drag_start)
root.bind('<B1-Motion>', on_drag_motion)
root.bind('<ButtonRelease-1>', on_drag_end)

root.mainloop()