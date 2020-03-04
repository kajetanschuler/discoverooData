import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import urllib.request

def main():
    # Load city names
    cities = pd.read_csv("../data_final/cityData_final.csv")
    city_names = cities["cityName"]
    #class_="rg_i q4LuWd tx8vtf"

    URL = "https://www.google.com/search?q=AbuDhabi&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiEmPbQpIDoAhXwsaQKHSi7D14Q_AUoAnoECBoQBA&biw=1920&bih=910"

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0'}
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    links = soup.findAll('a', href=True)
    print(links)


    #urllib.request.urlretrieve("https://upload.wikimedia.org/wikipedia/commons/c/ca/London_Montage_B.jpg", "C:/Users/cayci/Bilder/Bild1.jpg")

    #for x in city_names:
        #wikipage = 'https://de.wikipedia.org/wiki/' + x


    # Load Wiki







if __name__ == '__main__':
        main()