import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import urllib.request


def main():

        cities = pd.read_csv("../data_final/cityData_final.csv")

       # cities = cities[["cityName", "cityId"]]

        for index, city in cities.iterrows():

                cityName = city[4]
                cityId = city[0]
                if cityName == "cityName":
                        break

                URL = "https://www.bing.com/images/search?sp=-1&pq=ajma&sc=8-4&sk=&cvid=2FC3F99AA95E43B99EB54DEFDB48A96E&q=city " + cityName + "&qft=+filterui:photo-photo+filterui:aspect-wide+filterui:imagesize-large&FORM=IRFLTR"
                headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')
                images = soup.findAll('img', class_="mimg")
                x=0
                for image in images:
                        if x < 1:
                                link = image['src']
                                link = link + "&dpr=5"
                                print(link)
                                print("Ein Bild von " + cityName + str(cityId) + " wurde hinzugefügt")
                                urllib.request.urlretrieve(link, "C:/Users/cayci/Bilder/" + str(cityId) + ".jpg")
                                x = x+1


if __name__ == '__main__':
        main()