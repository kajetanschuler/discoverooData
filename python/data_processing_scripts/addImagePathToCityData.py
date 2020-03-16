import pandas as pd
import numpy as np

def main():

    city_data = pd.read_csv("../data_final/cityData_final.csv")

    city_data['image_links'] = city_data['cityId'].apply(lambda x: str(x) + ".jpg")
    print(city_data)

    city_data.to_csv("../data_final/city_data_final_image_links.csv", index=False)



if __name__ == '__main__':
        main()