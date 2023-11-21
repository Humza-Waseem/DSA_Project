import requests
from bs4 import BeautifulSoup
import sys
import csv
import pandas as pd

i = 1

def SpeedScrap(base_url, startPage, EndPage, data, catagory):
    print(base_url)
    for count in range(startPage, startPage + 1):
        if(count != 1):
            url1 = base_url + f'?page={count}'
        else: 
            url1 = base_url
        print(url1)
        r = requests.get(url1)
        content = r.content
        soup = BeautifulSoup(content,'html.parser')


        # Find all the divs with class "well search-list clearfix ad-container page-"
        if(count != 1):
            car_listings = soup.find_all('div', class_='well search-list clearfix ad-container page-'+ f'{count}')
        else:
            car_listings = soup.find_all('div', class_='well search-list clearfix ad-container page-')

        for car_listing in car_listings:
            # Find the anchor tag in the div with class "search-title"
            car_name = car_listing.find('div', class_='search-title').find('a')['title']

            # Find the price of the car
            price_details = car_listing.find('div', class_='price-details generic-dark-grey')
            if price_details:
                price = price_details.get_text(strip=True)
            else:
                price = "N/A"

            # Find the city of the car
            city = car_listing.find('ul', class_='list-unstyled search-vehicle-info fs13').find('li').get_text(strip=True)

            # Find the ul with class "list-unstyled search-vehicle-info-2 fs13"
            ul_info_2 = car_listing.find('ul', class_='list-unstyled search-vehicle-info-2 fs13')

            # Find individual pieces of information within ul_info_2
            li_tags = ul_info_2.find_all('li')

            car_model = li_tags[0].get_text(strip=True)
            distance_travelled = li_tags[1].get_text(strip=True)
            fuel_type = li_tags[2].get_text(strip=True)
            engine_capacity = li_tags[3].get_text(strip=True)
            gear_type = li_tags[4].get_text(strip=True)

            global i

            # Print or use the extracted information for each car
            print(f"{i}. {car_name},  {price}, {city}, {car_model}, {distance_travelled}, {fuel_type}, {engine_capacity}, {gear_type}, {catagory}")
            print("\n")
            i += 1
            data.append([
                car_name, price, city, car_model, distance_travelled,
                fuel_type, engine_capacity, gear_type, catagory
            ])
        df = pd.DataFrame(data, columns=[
            'Car Name', 'Price', 'City', 'Car Model', 'Distance Travelled',
            'Fuel Type', 'Engine Capacity', 'Gear Type', 'Category'
        ])
        # save data to csv
        df.to_csv('CarData6.csv', mode='a', index=False, header= False)
        data = []

# Set the standard output encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')

url = "https://www.pakwheels.com/"

# Now you can continue with the rest of your code
r = requests.get(url)
content = r.content

# Create a BeautifulSoup object with 'html.parser' as the parser
soup = BeautifulSoup(content, 'html.parser')
# Find all <li> tags with the class "col-sm-2"
li_tags = soup.find_all('li', class_='col-sm-2')

# Initialize a list to store the extracted links
links = []
categories = []

# Loop through the <li> tags and find the anchor tags within each one
for li_tag in li_tags:
    anchor_tag = li_tag.find('a')
    if anchor_tag:
        # Get the href attribute of the anchor tag (link)
        link = anchor_tag.get('href')
        links.append(url + link)

for li_tag in li_tags:
    catagory = li_tag.find('a')['title']
    categories.append(catagory)


li_tags_2 = soup.find_all('li', class_='col-sm-3')

# Initialize a list to store the extracted links
links2 = []
categories2 = []

# Loop through the <li> tags and find the anchor tags within each one
for li_tag in li_tags_2:
    anchor_tag = li_tag.find('a')
    if anchor_tag:
        # Get the href attribute of the anchor tag (link)
        link = anchor_tag.get('href')
        links2.append(url + link)

for li_tag in li_tags_2:
    catagory = li_tag.find('a')['title']
    categories2.append(catagory)


data = []

print(links2[13])
index = 12
SpeedScrap(links2[index],1763,1781,data, categories2[index])