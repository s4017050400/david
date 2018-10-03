from datetime import date
from datetime import timedelta

today=date.today() #which is like datetime.date(2018,10,3)
one_day=timedelta(days=1) #one day which can be plused

for i in range(1,11):
  date=today+i*one_day
  standard=date.isoformat().translate({ord(c):None for c in '-'})#date.isoformat() is 2018-10-03
  print(standard)
  
