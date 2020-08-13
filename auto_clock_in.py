from selenium import webdriver

from time import sleep


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

browser.set_window_size(900, 800)
#点击提交按钮
button = browser.find_element_by_id('btn_Login')
button.click()
#这边已经登录完成


# 打卡
browser.find_element_by_xpath("//*[@id='apply-content']/div[2]/ul/li[2]").click()
browser.find_element_by_id("submit").click()
sleep(1)
browser.find_element_by_name("DATA_15").click()
browser.find_element_by_id("btn_save").click()

browser.close()

browser.quit()


