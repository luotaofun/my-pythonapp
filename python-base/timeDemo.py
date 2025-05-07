import time
# struct_time 转字符串
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())) # 2025-05-04 17:46:12
print('%B月份的名称',time.strftime('%B',time.localtime())) # May
print('%A星期的名称',time.strftime('%A',time.localtime())) # Sunday
# 字符串转struct_time
print(time.strptime('2025-05-04 17:46:12','%Y-%m-%d %H:%M:%S'))

from datetime import datetime
t1 =datetime(year=2025,month=5,day=1,hour=0,minute=0,second=0) # <class 'datetime.datetime'>
t2 =datetime(year=2025,month=10,day=1,hour=0,minute=0,second=0)
print(t1<t2) # True
# datetime转字符串
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) # 2025-05-04 17:59:07
# 字符串转datetime
print(datetime.strptime('2025-05-04 17:59:07','%Y-%m-%d %H:%M:%S'))

from datetime import timedelta
tsub = t2-t1
print(tsub,type(tsub)) # 153 days, 0:00:00 <class 'datetime.timedelta'>
tt=t1 + timedelta(days=10,seconds=0) #  往后10天
print(tt) # 2025-05-11 00:00:00