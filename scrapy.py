from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver

URL="https://en.wikipedia.org/wiki/List_of_brightest_stars"
browser = webdriver.Chrome()  # Initializing Chrome WebDriver
browser.get(URL)
time.sleep(2)




scraped_data=[]
def scrape():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    bright_star_table = soup.find("table", attrs={"class": "wikitable sortable sticky-header jquery-tablesorter"})

    # Access the first tbody element
    table_body = bright_star_table.find('tbody')

    # Find all rows within the tbody
    table_rows = table_body.find_all('tr')
    for rows in table_rows:
        table_col=rows.find_all('td')
        print(table_col)
        temp_list=[]
        for col_data in table_col:
            data=col_data.text.strip()
            temp_list.append(data)
        scraped_data.append(temp_list)

stars_data = []

for i in range(0, len(scraped_data)):
    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

headers=["Star_names","Distance","Mass","Radius","Lum"]

df=pd.DataFrame(stars_data,columns=headers)
df.to_csv("scraped_data.csv",index=True,index_label="id")
scrape()




