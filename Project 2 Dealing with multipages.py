import requests
from bs4 import BeautifulSoup
import pandas as pd

# url = 'https://www.airbnb.ie/s/Portugal/homes?tab_id=home_tab&flexible_trip_lengths%5B%5D=one_week&source=structured_search_input_header&search_type=unknown&query=Portugal&place_id=ChIJ1SZCvy0kMgsRQfBOHAlLuCo&date_picker_type=calendar&checkin=2022-07-11&checkout=2022-07-24&drawer_open=true&map_toggle=true&refinement_paths%5B%5D=%2Fhomes'

# page = requests.get(url)
# page

# soup = BeautifulSoup(page.text, 'lxml')
# soup

# df = pd.DataFrame({'Links':[''],'Title':[''],'Details':[''],'Price':[''],'Rating':['']} )



# while True:
#     postings = soup.find_all('div', class_ = 'c4mnd7m dir dir-ltr')
#     for post in postings:
#         try:
#             link = post.find('a', class_='ln2bl2p dir dir-ltr').get('href')
#             linkFull = 'www.airbnb.ie' + link
#             titleId = post.find('a', class_='ln2bl2p dir dir-ltr').get('aria-labelledby')
#             title = post.find(id =titleId).text.strip()
#             price = post.find('span', class_='_tyxjp1').text
#             rating = post.find('span', class_='ru0q88m dir dir-ltr').text
#             details = post.find('span', class_='dir dir-ltr').text
#             df = df.append({'Links':linkFull,'Title':title, 'Details':details, 'Price':price, 'Rating':rating}, ignore_index =True )
#         except:
#             pass
       
#     try:
#         nextPage = soup.find('a',{'aria-label':'Next'}).get('href')
#         nextPageFull = 'https://www.airbnb.ie' + nextPage
#         url = nextPageFull
#         page = requests.get(url)
#         soup = BeautifulSoup(page.text, 'lxml')
#     except:
#         pass

# df.to_csv('/Users/am/Downloads/airbnbPortugal.csv')

# exercise

url ='https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7'
page = requests.get(url)
page

soup = BeautifulSoup(page.text, 'lxml')
df = pd.DataFrame({'Name':[''],'Detail':[''],'Price':[''],'Color':[''],'KM':[''],'Location':[''],'Links':['']} )



n = 10
while n > 0 :
    positions = soup.find_all('div', class_ ='media soft push-none rule')
    for post in positions:
        # 1 get link of each position
        link = post.find('h4',class_='hN').find('a').get('href')
        linkFull = 'https://www.carpages.ca/' + link
        
        # 2 get name of each car
        name = post.find('h4',class_='hN').text.strip()
        
        # 3 get price of each
        price = post.find('strong', class_='delta').text.strip()
        
        # 4 KM
        km = post.find('div', class_='grey l-column l-column--small-6 l-column--medium-4')
        kmNumber = km.find_all('span')
        kmString =''
        for s in kmNumber:
            kmString += s.text
            
        # 5 get color of each car
        color = post.find_all('div','span', class_='grey l-column l-column--small-6 l-column--medium-4')[-1].text.strip()
        
        # 6 get Details
        detail = post.find_all('h5', class_='hN')[0].text
        
        # 7 Location
        locationOne = post.find_all('h5', class_='hN')[0].text
        locationTwo = post.find_all('p', class_='hN')[-1].text
        location = locationOne +', ' + locationTwo
        
        # 8 get all data info 
        df = df.append({'Name':name,'Detail':detail,'Price':price,'Color':color,'KM':kmString,'Location':location,'Links':linkFull}, ignore_index= True)
        
    
    #next page
    nextPage = soup.find('a',{'title':'Next Page'}).get('href')
    nextPageFull = 'https://www.carpages.ca' + nextPage
    url = nextPageFull
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    n -= 1



df.to_csv('/Users/am/Downloads/cars.csv')
df = df.iloc[1: , :]







