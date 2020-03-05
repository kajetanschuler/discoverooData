import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import urllib.request

def main():

        cities = pd.read_csv("../data_final/cityData_final.csv")
        city_names = cities["cityName"]
        for city in city_names:
                URL = "https://www.bing.com/images/search?cw=1519&ch=478&q=" + city + "&qft=+filterui:imagesize-medium+filterui:photo-photo&FORM=IRFLTR"
                headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}
                page = requests.get(URL, headers=headers)
                soup = BeautifulSoup(page.content, 'html.parser')

                images = soup.findAll('img', class_="mimg")
                x=0
                for image in images:
                        if x < 1:
                                Link = image['src']
                                urllib.request.urlretrieve(
                                        Link,
                                        "C:/Users/cayci/Bilder/" + city + ".jpg")
                                print("Ein Bild von " + city + " wurde hinzugefügt")

                                x = x+1


if __name__ == '__main__':
        main()