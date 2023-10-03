from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
#for sleep to observe chrome live


print("imlive")

driver = webdriver.Chrome()

driver.get("https://newhouse.591.com.tw/housing-list-6.html")
# totals = driver.find_element(By.XPATH, './/span[@class = "fc-red"]').text
# totals = driver.find_element(By.XPATH, "//span[@class='fc-red' and @id='total-build']")
# totals = driver.find_element(By.xpath("//span[@class='fc-red' and @id='total-build']"
# //h2[contains(@class, 'jobTitle')]/span[@title]")
# totals = driver.find_element("total-build")
# titles = driver.find_element(By.CLASS_NAME,'fc-red')
# print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='listMenu_right']/span"))).get_attribute("innerHTML"))
# print(titles.text)
# for title in titles:
#     print(title.text)
print(driver.title)

time.sleep(10) # as import time statement