from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.common.by import By
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
import os




#Starts the driver and goes to our starting webpage
driver = webdriver.Chrome('/Users/am/Downloads/chromedriver')

driver.get('https://ca.indeed.com/')

#Inputs a job title into the input box
input_box = driver.find_element(By.XPATH,'//*[@id="text-input-what"]')
input_box.send_keys('data analyst')

#Clicks on the search button
button = driver.find_element(By.XPATH,'//*[@id="jobsearch"]/button').click()

#Creates a dataframe
df = pd.DataFrame({'Link':[''], 'Job Title':[''], 'Company':[''], 'Location':[''],'Salary':[''], 'Date':['']})

#This loop goes through every page and grabs all the details of each posting
#Loop will only end when there are no more pages to go through
while True:  
    #Imports the HTML of the current page into python
    soup = BeautifulSoup(driver.page_source, 'lxml')
    
    #Grabs the HTML of each posting
    postings = soup.find_all('div', class_ = 'job_seen_beacon')
    
    #grabs all the details for each posting and adds it as a row to the dataframe
    for post in postings:
        link = post.find('a', class_ = 'jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
        link_full = 'https://ca.indeed.com'+link
        
        try:
            name = post.find('h2', class_ = 'jobTitle jobTitle-newJob css-bdjp2m eu4oa1w0').text.strip()
        except Exception:
            name = post.find('h2', class_ = 'jobTitle css-1h4a4n5 eu4oa1w0').text.strip()
            pass
        
        
        try:
            company = post.find('a', class_ = 'turnstileLink companyOverviewLink').text.strip()
        except Exception:
            
            company = post.find('span', class_ = 'companyName').text.strip()
            
            pass
        
        try:
            location = post.find('div', class_ = 'companyLocation').text.strip()
        except:
            location = 'N/A'
        date = post.find('span', class_ = 'date').text.strip()
    
        try:
            salary = post.find('div', class_ = 'metadata salary-snippet-container').text.strip()
        except:
            salary = 'N/A'
    
        df = df.append({'Link':link_full, 'Job Title':name, 'Company':company, 'Location':location,'Salary':salary, 'Date':date},
                       ignore_index = True)
        

    # checks if there is a button to go to the next page, and if not will stop the loop
    try:
        button = soup.find('a', attrs = {'aria-label': 'Next'}).get('href')
        driver.get('https://ca.indeed.com'+button)
    except:
        break
        print(button)
        pass
        

# https://www.youtube.com/watch?v=uVDq4VOBMNM
# https://towardsdatascience.com/automate-sending-emails-with-gmail-in-python-449cc0c3c317


sender = 'email'
app_password ='app_password from 2 factor setup'
host ='smtp.gmail.com'
port = 465
receiver = 'email'

subject = 'New list of jobs'
contextTxt = 'some body text 3'
attachment = '/Users/am/Downloads/cars.csv'


msg = MIMEMultipart()
msg['Subject'] = Header(subject)
msg['From'] = Header(sender)
msg['To'] = Header(receiver)
msg.attach(MIMEText(contextTxt,'plain','utf-8'))

part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attachment,'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename="cars.csv"')
msg.attach(part)
# sending
server = smtplib.SMTP_SSL(host, port)
server.login(sender, app_password)
server.sendmail(sender,receiver,msg.as_string())
server.quit()
print('Email sent sucessfully')












