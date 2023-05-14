import time
import pandas as pd

xls = pd.read_excel('./data.xls')
print(type(xls))
print(xls.info())
print('========================================')
time_cloumn = xls['当地时间 重庆/九龙坡(机场)']
print(time_cloumn)
print('========================================')
mktime = []
for i in time_cloumn:
    timeArray = time.strptime(i, "%d.%m.%Y %H:%M")
    timestamp = time.mktime(timeArray)
    mktime.append(timestamp)

for i in range(len(mktime)):
    xls.at[i,'当地时间 重庆/九龙坡(机场)'] = mktime[i]
print('========================================')

print(xls)
xls.to_csv('output.csv')
print("本数据集的时间已经全部处理为时间戳！")

###本程序将原数据集中的时间改为了时间戳的格式