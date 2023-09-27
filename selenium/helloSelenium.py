from selenium import webdriver
import time #for sleep to observe chrome live


print("imlive")

driver = webdriver.Chrome()

driver.get("https://www.google.com")

print(driver.title)

time.sleep(10) # as import time statement