import requests
from bs4 import BeautifulSoup
import re
import pandas as pd




url='https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets'
page = requests.get(url)
page.text
soup = BeautifulSoup(page.text, features='lxml')
soup
soup.header



# Tags
headerTag = soup.header
divTag = soup.div
divTag

#Atributss
aTag = headerTag.a
aTag.attrs
aTag['data-toggle']
aTag['newAttributs'] = 'Andypandy'

aTag.attrs


#find
soup.find('header')

soup.header.attrs
soup.find('div', {'class':'container test-site'})

soup.find('h4',{'class':'pull-right price'})
soup.find('h4', class_='pull-right price')


#find all
soup.find_all('h4',{'class':'pull-right price'})
soup.find('header')
soup.header.attrs
soup.find('div', {'class':'container test-site'})
soup.find('h4',{'class':'pull-right price'})
soup.find('h4', class_='pull-right price')


#find all
soup.find_all('h4',{'class':'pull-right price'})
soup.find_all('a', class_='title')
soup.find_all('p',class_ ='pull-right')
soup.find_all('h4',{'class':'pull-right price'})[0:6]
soup.find_all(['h4','p'])
soup.find_all(id=True)
soup.find_all(string = 'Galaxy Tab 3')
soup.find_all(string=['Galaxy Tab 3','Galaxy Note'])

soup.find_all(string = re.compile('Gal'))
soup.find_all(class_ = re.compile('pull'))
soup.find_all('p',class_ = re.compile('pull'))
soup.find_all('p',class_ = re.compile('pull'), limit = 3)
soup.find_all('p',class_ = re.compile('pull'))[0:3]




#find all to table
productName = soup.find_all('a', class_ ='title')
productName

price = soup.find_all('h4', class_ = 'pull-right price')
price

reviews = soup.find_all('p',class_ = re.compile('pull'))
reviews

description = soup.find_all('p', class_ = 'description')
description

productNameList =[]

for i in productName:
    name = i.text
    productNameList.append(name)


productNameList

priceList =[]

for i in price:
    name = i.text
    priceList.append(name)

reviewsList =[]

for i in reviews:
    name = i.text
    reviewsList.append(name)
    
    

descriptionList =[]

for i in description:
    name = i.text
    descriptionList.append(name) 
    

table2 = pd.DataFrame({'Product Name': productNameList,
                     'Description': descriptionList,
                     'Price': priceList, 'Review':reviewsList})

table2



#nested html
boxes = soup.find_all('div',class_='col-sm-4 col-lg-4 col-md-4')[2]
boxes

boxes.find('a').text

boxes.find('p', class_ = 'description').text
    
    
    
    

