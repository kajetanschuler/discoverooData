#Das Skript ändert die Iso3 Codes in Iso2 Codes und droppt NaN Werte
#17.02.2020 Malik

import pandas as pd
import country_converter as coco


def main():
    quality = pd.read_csv("../data_raw/overallQualityOfInfrastructure.csv")
    quality['countryCode'] = quality['countryCode'].apply(lambda x: coco.convert(names=x, to='Iso2'))
    quality = quality.dropna()
    quality = quality.rename(columns={'infrastructureValue1718': 'infrastructureValue'})

    # print(quality)

    quality.to_csv("../data_processed/qualityOfInfrastructure.csv", index=False)
    print('Infrastrukturdaten erstellt')

if __name__ == '__main__':
    main()