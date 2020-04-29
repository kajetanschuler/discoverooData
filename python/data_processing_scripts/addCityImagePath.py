# Skript, das eine "image_links" Spalte zu city_data_final hinzufügt um auf das jeweilige Stadtbild zu verweisen
# created 20.03.2020 by Malik

import pandas as pd
import numpy as np


def main():
    s3 = 'https://travelapiimages.s3.eu-central-1.amazonaws.com/'
    city_data = pd.read_csv("../data_final/cityData_final.csv")

    city_data['image_links'] = s3 + city_data['cityId'].apply(lambda x: str(x) + ".jpg")

    city_data = city_data[['cityId', 'image_links']]

    city_data.to_csv("../data_processed/cityImagePath.csv", index=False)


if __name__ == '__main__':
    main()
