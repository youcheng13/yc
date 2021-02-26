import selenium
from helium import *
import time
start_chrome("https://m.78500.cn/kaijiang/p5/")
# write("小姐姐")
# press(ENTER)
click("点击加载更多")
for i in range(60):
    click("点击加载更多")
    time.sleep(4)
    
# img = driver.find_element_by_name("pn1") 
# click(img)
# download = driver.find_element_by_class_name("btn-download")
# click(download)