import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook
import matplotlib.pyplot as plt
import urllib.request

Stadt= "Abu Dh"
Link2 = "https://th.bing.com/th/id/OIP.OX5J0RmVEFq6MBZXSCLs-QHaHa?w=177&h=175&c=7&o=5&dpr=5&pid=5"
Link3 = "https://th.bing.com/th/id/OIP.OX5J0RmVEFq6MBZXSCLs-QHaHa?w=177&h=175&c=7&o=5&dpr=1.13&pid=1.7"
Link = "https://tse4.mm.bing.net/th/id/OIP.Pb8urNCn0tzsDGWBqLDkdQHaEo?w=240&h=160&c=7&o=5&pid=1.7&dpr=1.12"
urllib.request.urlretrieve(Link,
                           "C:/Users/cayci/Bilder/" + Stadt + ".jpg")

