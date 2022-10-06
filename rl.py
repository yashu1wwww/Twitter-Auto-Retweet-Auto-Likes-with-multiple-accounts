#here i am added upto 5 accs which auto login and retweet and like if you want more means copy line from 3 to 40 and paste that in 197 line use note++ to find the number line
#(note for auto login used accs must be non authentication accounts)

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("@twitter123") #replace with your twitter acc and do it for below code also 
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twiee1@#$") #replace with your twitter password and dot it for below code also
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f: #put your in url in text file and no need it for all 
    for url in f:
        driver.get(url) 

time.sleep(5)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()

retweet_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()

time.sleep(2)

like_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))).click()

time.sleep(2)

driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("@twitter123") #replace with your twitter acc and do it for below code also 
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twiee1@#$") #replace with your twitter password and dot it for below code also
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url) 

time.sleep(5)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()

retweet_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()

time.sleep(2)

like_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))).click()

time.sleep(2)

driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("@twitter123") #replace with your twitter acc and do it for below code also 
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twiee1@#$") #replace with your twitter password and dot it for below code also
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url) 

time.sleep(5)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()

retweet_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()

time.sleep(2)

like_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))).click()

time.sleep(2)

driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("@twitter123") #replace with your twitter acc and do it for below code also 
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twiee1@#$") #replace with your twitter password and dot it for below code also
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url) 

time.sleep(5)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()

retweet_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()

time.sleep(2)

like_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))).click()

time.sleep(2)

driver.close()

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver= webdriver.Chrome()
driver.maximize_window()

driver.get("https://twitter.com/i/flow/login")
time.sleep(10)
email = driver.find_element_by_name('text')
email.send_keys("@twitter123") #replace with your twitter acc and do it for below code also 
email.send_keys(Keys.ENTER)
time.sleep(3)
password = driver.find_element_by_name("password")
password.send_keys("twiee1@#$") #replace with your twitter password and dot it for below code also
password.send_keys(Keys.ENTER)
time.sleep(5)

with open("urls.txt") as f:
    for url in f:
        driver.get(url) 

time.sleep(5)

retweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Retweet']"))).click()

retweet_confirm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='retweetConfirm']"))).click()

time.sleep(2)

like_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Like']"))).click()

time.sleep(2)

driver.close()