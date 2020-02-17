#Das Skript ändert die Iso3 Codes in Iso2 Codes und droppt NaN Werte
#17.02.2020 Malik

import pandas as pd
import country_converter as coco
cc = coco.CountryConverter()
def main():


    quality = pd.read_csv("../data_raw/overallQualityOfInfrastructure.csv", sep=';')
    quality['CountryISO3'] = quality['CountryISO3'].apply(lambda x: coco.convert(names=x, to='Iso2'))
    quality = quality.dropna()
    print(quality)

    quality.to_csv("../data_processed/qualityOfInfrastructure_clean.csv")
    print('Datei wurde erstellt')


if __name__ == '__main__':
    main()