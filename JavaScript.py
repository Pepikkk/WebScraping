

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome('/Users/am/Downloads/chromedriver')

# driver.get('https://sites.google.com/chromium.org/driver/downloads')
# driver.get('https://www.goat.com/sneakers')

# By.XPATH
# for i in range(1,20):
#     price = driver.find_element(By.XPATH,'//*[@id="grid-body"]/div/div[1]/div['+str(i)+']/a/div[1]/div[2]/div/div').text
#     print(price)

# input box and endter
driver.get('https://www.google.com/')

# try:
#     eks = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[3]/div[1]/span[1]/svg')
#     eks.clear()
# except:
#         pass

privacy = driver.find_element(By.XPATH, '//*[@id="L2AGLb"]/div')
privacy.click()

box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
# box.clear()
box.send_keys('web scraping')
box.send_keys(Keys.ENTER)


# click button
button = driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[2]/a')
button.click()

link = driver.find_element(By.XPATH,'//*[@id="tads"]/div[1]/div/div/div/div[1]/a/div[1]')
link.click()

# take screenshot
# driver.save_screenshot('/Users/am/Downloads/pagescrape.jpg')

driver.find_element(By.XPATH, '//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="islrg"]/div[1]/div[2]/a[1]/div[1]/img').screenshot('/Users/am/Downloads/pagescrape.jpg')


# selfscrolling 
driver.execute_script('return document.body.scrollHeight')
driver.execute_script('window.scrollTo(0,88046)')


keepGoing = True
while keepGoing:

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    try:
       showMore = driver.find_element(By.XPATH,'//*[@id="islmp"]/div/div/div/div[1]/div[2]/div[2]/input').click()
    except:
        pass
# wait time
button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[5]/center/input[1]')))