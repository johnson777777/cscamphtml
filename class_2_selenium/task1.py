from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(executable_path="/home/cscamp/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service)

url = "https://www.ptt.cc/bbs/Japan_Travel/index.html"
driver.get(url)
print(driver.title) # 印出網站的標題

element = driver.find_element(By.CLASS_NAME, "title")
print (element.text) # 印出標題的文字
print (element.tag_name) # 印出標題的標籤名稱

driver.quit() # 關閉瀏覽器