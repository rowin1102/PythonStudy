from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'https://www.ikosmo.co.kr/main'
driver.get(url)

driver.find_element(By.XPATH, '//*[@id="header"]/div[1]/div/ul/li[1]/a').click()
time.sleep(2)

driver.find_element(By.NAME, 'id').send_keys('rowin1102')
time.sleep(2)
driver.find_element(By.NAME, 'password').send_keys('ma001102@')

driver.find_element(By.XPATH, '//*[@id="subConts"]/div/div/div/div/section/section/form/fieldset/div[2]/ul/li/a').click()
time.sleep(5)