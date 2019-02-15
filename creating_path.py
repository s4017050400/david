import os

filename = "/foo/bar/baz.txt"¨ #first '/' means a 'C:' if no 'no' means 'wtcwd'
os.makedirs(os.path.dirname(filename), exist_ok=True) 'exist_ok means judged file-existing 
with open(filename, "w") as f:
    f.write("FOOBAR")

   
#_________________________________________________
#多層資料夾實現

>>> str1=['FT1_-40','FT2_25','FT3_90','FT4_125']
>>> str2=['HH','LL','TT','HL','LH']

>>> for x in str1:
...     for y in str2:
...             filename = "foo/bar/{0}/{1}/This_is_{0}+{1}_dir.txt".format(x,y)
...             os.makedirs(os.path.dirname(filename), exist_ok=True)
...             with open(filename, "w") as f:
...                     f.write('hello!')
...                     f.close()


#______________________________________________________


from os import listdir
mypath = r'C:\Users\CKLu0\Desktop\UAA077 DD1C corner EV\eda_file_search_2019-02-12.14.24.45\eda_file_archive2\eda_export_data\ftwb\壓縮檔'
>>> files = listdir(mypath)
>>> for f in files:
...     print(f)


#______________________________________________________
#pamo.py

import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()




def path():
    file = filedialog.askopenfilename()     #取得檔案路徑
    return str(file)

def direct():
    direct = filedialog.askdirectory()      #取得目錄路徑
    return str(direct)

#______________________________________________________
import pamo #自己弄的檔案↑
from os import listdir
import os


dict1={'FT1':'FT1_-40','FT2':'FT2_25','FT3':'FT3_90','FT4':'FT4_125'}
dict2={'ZW':'HH','ZU':'LL','ZR':'TT','ZT':'HL','ZS':'LH'}

mypath = pamo.direct() #輸入資料目录路径
outpath = pamo.direct() #輸出資料目录路径
files = listdir(mypath) #把目錄下的檔案列出

for file in files: #列出
    d1=dict1[file[17:20]]   #dict1={'FT1':'FT1_-40','FT2':'FT2_25','FT3':'FT3_90','FT4':'FT4_125'}
    d2=dict2[file[11:13]]   #dict2={'ZW':'HH','ZU':'LL','ZR':'TT','ZT':'HL','ZS':'LH'}
    
    filename = outpath+"/{0}/{1}/This_is_{0}+{1}_dir.txt".format(d1,d2)
    os.makedirs(os.path.dirname(filename), exist_ok=True)   #創造路徑
    with open(filename, "w") as f1:
        f=open(mypath+'/'+file)
        f1.write(f.read())
        f1.close

