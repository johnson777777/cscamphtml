from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=service)

driver.get("https://www.ptt.cc/bbs/Japan_Travel/index.html")

element = driver.find_element(By.CLASS_NAME, "query") 
element.clear() # 清除輸入結果
element.send_keys("北海道" + Keys.ENTER)
links = driver.find_elements(By.PARTIAL_LINK_TEXT, "伴手禮")
links[0].click()
content = driver.find_element(By.ID, "main-content")
print(content.text)

time.sleep(5)
driver.quit()