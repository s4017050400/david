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
