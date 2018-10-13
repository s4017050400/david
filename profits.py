import requests
from bs4 import BeautifulSoup as bs4
import pandas as pd
from io import StringIO

url = "http://mops.twse.com.tw/server-java/t05st09sub"


r = requests.post(url, {
        'step':1,
        'TYPEK':'otc',
        'YEAR':'104',
        })
#print(r.text)
r.encoding='big5'

dfs=pd.read_html(StringIO(r.text))
df=pd.concat(dfs).drop_duplicates(subset=0).drop([0,1]).reset_index(drop=True) //duplicates mean to delete the row which has same data.
// drop means to delete the row of index=0,1. 
list1=['公司代號	名稱', '資料來源', '期別', '董事會決議', 
'日期',	'期初未分配',
'本期淨利',
'可分配	',
'分配後期末未',
'盈餘分配之現金股利',
'法定盈餘',
'股東配發之現金(股利)',
'盈餘轉增資配股',
'法定盈餘',	
'股東配股']
list2=[p for p in range(0,10)]
df.columns=list1+list2
df[['代號','公司']]=df['公司代號\t名稱'].str.split(' - ', expand=True)//split 1 column into 2 columns called ['代號','公司'] by ' - '

df.to_csv('profit104.csv',encoding='utf_8_sig')
