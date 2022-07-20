

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('/Users/am/Downloads/chromedriver')

driver.get('https://www.nike.com/ie/w/sale-3yaep')
privacy = driver.find_element(By.XPATH, '//*[@id="hf_cookie_text_cookieAccept"]').click()


try:
    newsletter = driver.find_element(By.XPATH, '//*[@id="gen-nav-commerce-header-v2"]/div[1]/div/button').click()
except Exception:
    pass

lastHight = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    newHeight = driver.execute_script("return document.body.scrollHeight")
    if newHeight == lastHight:
        break
    lastHight = newHeight
    
    
soup = BeautifulSoup(driver.page_source, 'lxml')
productCard = soup('div', class_ = 'product-card__body')
df = pd.DataFrame({'Link':[""],'Title':[''], 'Subtitle':[''], 'Color':[''], 'Sale Price':[""], 'Product Price': [""]})

for product in productCard:
    
    try:
        link = product.find('a', class_ ='product-card__img-link-overlay').get('href')
        title = product.find('div', class_='product-card__title').text
        subtitle = product.find('div', class_='product-card__subtitle').text
        color = product.find('button', class_= 'product-card__colorway-btn').text
        currentPrice = product.find('div', class_='product-price is--current-price css-s56yt7').text
        productPrice = product.find('div', class_='product-price is--striked-out').text
        df = df.append({'Link':link,'Title':title, 'Subtitle':subtitle, 'Color':color, 'Sale Price':currentPrice, 'Product Price': productPrice}, ignore_index=True)
    except Exception:
        pass

df = df.iloc[1: , :]