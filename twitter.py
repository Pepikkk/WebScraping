
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome('/Users/am/Downloads/chromedriver')

driver.get('https://twitter.com/i/flow/login')
time.sleep(2)

celebrity = 'The Rock'

login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
login.send_keys('UR-EMAIL')
loginNext = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
loginNext.click() 
time.sleep(2)

try:
    phone = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
    phone.send_keys('0000000')
    
    phoneNext = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div')
    phoneNext.click()
except Exception:
    pass

time.sleep(2)
password = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password.send_keys('UR-PASSWD')
loginButton = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
loginButton.click()
time.sleep(2)
acceptCookies = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div')
acceptCookies.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')))

search = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input')
search.send_keys(celebrity)
search.send_keys(Keys.ENTER)
time.sleep(3)
people = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div')
people.click()
time.sleep(3)
profile = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]')
profile.click()
time.sleep(5)


soup = BeautifulSoup(driver.page_source, 'lxml')
posts = soup.find_all('div', class_= 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')

tweets = []
tweetsTwo =[]
while True:
    for post in posts:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    posts = soup.find_all('div', class_= 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    tweetsTwo = list(dict.fromkeys(tweets))
    if len(tweetsTwo)>100:
        break
    






