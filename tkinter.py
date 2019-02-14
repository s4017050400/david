import tkinter as tk
from tkinter import filedialog
 
root = tk.Tk()
root.withdraw()
 
file_path = filedialog.askopenfilename()
 
print(file_path)　# 打印文件的路径



#__________________________________________
#方法寫法
import tkinter as tk
from tkinter import filedialog
 
root = tk.Tk()
root.withdraw()
 
file_path = filedialog.askopenfilename()

class Path():
    def __init__(self, path2):
        self.path2 = path2
        
b=Path(file_path)

print(b.path2)


#__________________________________________
https://openhome.cc/Gossip/CodeData/PythonTutorial/FunctionModuleClassPackagePy3.html
