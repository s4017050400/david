import requests
import pandas as pd


url='http://mops.twse.com.tw/mops/web/ajax_t163sb19'


r=requests.post(url,{
    'encodeURIComponent': 1,
    'step': 1,
    'firstin': 1,
    'TYPEK': 'sii',
    'code': '01',
    'year': 106,
    'season':'04'
    })


dfs = pd.read_html(r.text)



for df in dfs:
    df.to_csv('text.csv',encoding='utf_8_sig')


'''
result
             0           1      2    ...            6         7         8
0         公司代號        公司名稱    產業別    ...         營業利益  營業外收入及支出      稅後淨利
1         1104  環球水泥股份有限公司   水泥工業    ...       150227   1274987   1389535
2         1101  台灣水泥股份有限公司   水泥工業    ...     13962885   -138226  10322800
3   基本每股盈餘2至3元         計2家   2.10    ...          NaN       NaN       NaN
4         1102  亞洲水泥股份有限公司   水泥工業    ...      7436716   1062443   6665541
5         1103  嘉新水泥股份有限公司   水泥工業    ...      -229484   1311027    977309
6         1109  信大水泥股份有限公司   水泥工業    ...       854822     43102    710004
7   基本每股盈餘1至2元         計3家   1.48    ...          NaN       NaN       NaN
8         1110  東南水泥股份有限公司   水泥工業    ...      -137175    201190     58307
9   基本每股盈餘0至1元         計1家   0.11    ...          NaN       NaN       NaN
10        1108  幸福水泥股份有限公司   水泥工業    ...      -100344    -18667   -103078
11  基本每股盈餘小於0元         計1家  -0.25    ...          NaN       NaN       NaN
12        水泥工業         計7家   1.21    ...          NaN       NaN       NaN

[13 rows x 9 columns]
'''
