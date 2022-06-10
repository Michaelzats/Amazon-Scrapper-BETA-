from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get("https://www.amazon.de/")
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input#twotabsearchtextbox"))).send_keys("iphone 13" + Keys.RETURN)
s = [my_elem.text for my_elem in driver.find_elements(
    By.XPATH, "//span[@data-component-type='s-search-results']//div[@class='sg-col-inner']")]

print(s)
