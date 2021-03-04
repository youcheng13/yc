import selenium
from helium import *
start_chrome("www.baidu.com")
write("小姐姐")
press(ENTER)
click("图片")
img = driver.find_element_by_name("pn1") 
click(img)
download = driver.find_element_by_class_name("btn-download")
click(download)