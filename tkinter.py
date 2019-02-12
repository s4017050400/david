import tkinter as tk
from tkinter import filedialog
 
root = tk.Tk()
root.withdraw()
 
file_path = filedialog.askopenfilename()
 
print(file_path)　# 打印文件的路径
