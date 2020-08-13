from selenium import webdriver

import numpy as np
import pandas as pd
import datetime
from time import sleep
import send_mail


# 这里是登录网站爬数据的
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)

# browser = webdriver.Chrome()

browser.get("http://zyt.zjnu.edu.cn/H5/Login.aspx")
#表单赋值
browser.find_element_by_id("UserText").send_keys("写学号")

browser.find_element_by_id("PasswordText").send_keys("写密码")  #输入密码

browser.set_window_size(900, 800) # 由于树莓派屏幕的分辨率可能因为外界屏幕而改变了，而这个分辨率可能不能按下登录按钮，故，要固定尺寸，这个尺寸随便取的，能打就行。

#点击提交按钮
button = browser.find_element_by_id('btn_Login')
button.click()
#这边已经登录完成


# 爬出未打卡的人
url = 'http://zyt.zjnu.edu.cn/H5/index/AjaxImg.ashx?type=DKSJ&typeTS=&count=100&indextab=%E6%9C%AA%E6%89%93%E5%8D%A1&r=661'
browser.get(url)
a = browser.find_element_by_tag_name("body").text
# a是网页源代码，包含了未打卡的人的信息。

now = datetime.datetime.now()
timesss = str(now.year) + "年" + str(now.month) + "月" + str(now.day) + "日" + str(now.hour) + "时" + str(now.minute) + "分" + str(now.second) + "秒"
timessss = str(now.year) + "年" + str(now.month) + "月" + str(now.day) + "日"




if a == '[]': # 无人未打卡走这边
    text = "【战役通】截止" + timesss + "，物理172班已全部完成打卡"
    send_mail.send_user_mail(text)
else:
    # 后面都是提醒打卡的
    a = str.replace(a, "null", "1")
    a = str.replace(a, "[", '')
    a = str.replace(a, "]", '')
    b = eval(a)

    # 访问数据记录
    data = pd.read_csv('物理172班打卡记录.csv', sep='\n' and ',')
    data = np.array(data)
    data = data[:,1:5] # 第四列放邮箱

    if isinstance(b, tuple) == 1: # 多人未打卡
        print(1)
        record_list = []
        for i in b:
            dic = eval(str(i))
            dic = dic["PERSONCODE"]
            for ii in range(len(data[:, 0])):
                if dic == str(data[ii, 0]):
                    data[ii, 2] = 1 + data[ii, 2]
                    record = {'学号': data[:, 0], '姓名': data[:, 1], '累积未打卡次数': data[:, 2],'邮箱':data[:,3]}
                    record = pd.DataFrame(record)
                    record.to_csv('物理172班打卡记录.csv')
                    record_list.append(ii)
                    pass
                pass
            pass
    else: # 一人未打卡
        print(0)
        dic = b
        record_list = []
        dic = dic["PERSONCODE"]
        for ii in range(len(data[:, 0])):
            if dic == str(data[ii, 0]):
                data[ii, 2] = 1 + data[ii, 2]
                record = {'学号': data[:, 0], '姓名': data[:, 1], '累积未打卡次数': data[:, 2],'邮箱':data[:,3]}
                record = pd.DataFrame(record)
                record.to_csv('物理172班打卡记录.csv')
                record_list.append(ii)
                pass
            pass
        pass

    # print(record_dict)
    # 有未打卡的人都输出下面的东西
    for i in record_list:
        send_mail.send_notice_mail(data[i,3],data[i,1],timesss,data[i,2],timessss)
        sleep(2)

    text = "【战役通】截止" + timesss + "\n 物理172班还有"+str(len(record_list))+"位同学暂未打卡，已私聊提醒。\n 已向"
    for i in record_list:
        text = text + data[i,1]
        pass
    text = text + str(len(record_list)) + '位同学发送邮件提醒。'

    send_mail.send_user_mail(text)

    pass



browser.close()

browser.quit()
