import send_mail
import datetime


now = datetime.datetime.now()
timesss = str(now.year) + "年" + str(now.month) + "月" + str(now.day) + "日" + str(now.hour) + "时" + str(now.minute) + "分" + str(now.second) + "秒"
timessss = str(now.year) + "年" + str(now.month) + "月" + str(now.day) + "日"

send_mail.send_notice_mail('写接收邮箱','陆大帅',timesss,1,timessss)



# import pandas as pd
# import numpy as np
# 这里只是用来整理csv的
# data = pd.read_csv('物理172班打卡记录.csv', sep='\n' and ',')
# data = np.array(data)
# data = data[:, 1:5]  # 第四列放邮箱
# 
#
# record = {'学号': data[:, 0], '姓名': data[:, 1], '累积未打卡次数': data[:, 2],'邮箱':data[:,3]}
# record = pd.DataFrame(record)
# record.to_csv('物理172班打卡记录.csv')
