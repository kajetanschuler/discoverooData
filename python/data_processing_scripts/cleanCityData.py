
import pandas as pd


def main():
    cityData = pd.read_csv('../data_processed/cityData_regionCode.csv')

    cityData["cityName"] = cityData["cityName"].str.replace("ă", "a", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ả", "a", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ạ", "a", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ā", "a", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ế", "e", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ề", "e", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ề", "e", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ė", "e", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ệ", "e", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ế", "e", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ī", "i", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("İ", "i", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ị", "i", case=False)
    #cityData["cityName"] = cityData["cityName"].str.replace("ı", "l", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ộ", "o", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ố", "o", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ơ", "o", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ō", "o", case=True)
    cityData["cityName"] = cityData["cityName"].str.replace("Ō", "O", case=True)
    cityData["cityName"] = cityData["cityName"].str.replace("ū", "u", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ū", "u", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ư", "u", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("Đ", "D", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ğ", "g", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("H̱", "H", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("Ḩ̱", "H", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("Ş", "S", case=True)
    cityData["cityName"] = cityData["cityName"].str.replace("ş", "s", case=True)
    cityData["cityName"] = cityData["cityName"].str.replace("ś", "s", case=True)
    cityData["cityName"] = cityData["cityName"].str.replace("Ś", "S", case=True) #schräger Strich auf o,i und a wird erkannt
    cityData["cityName"] = cityData["cityName"].str.replace("ţ", "t", case=False)
    cityData["cityName"] = cityData["cityName"].str.replace("ł", "l", case=False)

    cityData["regionName"] = cityData["regionName"].str.replace("ă", "a", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ả", "a", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ạ", "a", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ā", "a", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ế", "e", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ề", "e", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ề", "e", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ė", "e", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ệ", "e", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ế", "e", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ī", "i", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("İ", "i", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ị", "i", case=False)
    #cityData["regionName"] = cityData["regionName"].str.replace("ı", "l", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ộ", "o", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ố", "o", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ơ", "o", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ō", "o", case=True)
    cityData["regionName"] = cityData["regionName"].str.replace("Ō", "O", case=True)
    cityData["regionName"] = cityData["regionName"].str.replace("ū", "u", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ū", "u", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ư", "u", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("Đ", "D", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ğ", "g", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("H̱", "H", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("Ḩ̱", "H", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("Ş", "S", case=True)
    cityData["regionName"] = cityData["regionName"].str.replace("ş", "s", case=True)
    cityData["regionName"] = cityData["regionName"].str.replace("ś", "s", case=True)
    cityData["regionName"] = cityData["regionName"].str.replace("Ś", "S", case=True)  # schräger Strich auf o,i und a wird erkannt
    cityData["regionName"] = cityData["regionName"].str.replace("ţ", "t", case=False)
    cityData["regionName"] = cityData["regionName"].str.replace("ł", "l", case=False)

    cityDataIndexNames = cityData[cityData['cityName'].str.contains('Municipality|City of|municipality|Sector|Zhumadian Shi')].index
    cityData.drop(cityDataIndexNames, inplace=True)

    cityData["cityName"] =  cityData["cityName"].str.replace("Gemeente","").str.replace("Kommune","").str.replace("Kommun","").str.replace("Partido de","")
    cityData["cityName"] =  cityData["cityName"].str.strip()
    cityData =cityData.sort_values("elevation",ascending=False)
    cityData.drop_duplicates(subset="cityName", keep='first', inplace=True)

    cityData["cityName"] = cityData["cityName"].str.title()

    #print(cityData.count(axis=1))

    cityData.to_csv("../data_processed/cityData_clean.csv", index=False, header=True)


if __name__ == '__main__':
    main()
