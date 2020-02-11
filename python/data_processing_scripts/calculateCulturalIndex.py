import pandas as pd

def main():

    population = pd.read_csv("../data_processed/allCitiesOver100k.csv")

    columns_to_skip = "searchRadius"
    sights = pd.read_csv("../data_raw/sightsInCities_old.csv", usecols=lambda x: x not in columns_to_skip)
    # cities = pd.read_csv("../data_processed/allCitiesMinPopulation")

    df = pd.merge(sights, population, on="cityId")

    print(df)

    # sights[["hCountLevel0", "cCountLevel0", "rCountLevel0", "aCountLevel0",
    #         "iCountLevel0", "nCountLevel0"]] = sights[["hCountLevel0", "cCountLevel0", "rCountLevel0", "aCountLevel0",
    #                                                    "iCountLevel0", "nCountLevel0"]].apply(lambda x: x * 1)
    #
    # sights[["hCountLevel1", "cCountLevel1", "rCountLevel1", "aCountLevel1",
    #         "iCountLevel1", "nCountLevel1"]] = sights[["hCountLevel1", "cCountLevel1", "rCountLevel1", "aCountLevel1",
    #                                                    "iCountLevel1", "nCountLevel1"]].apply(lambda x: x * 2)
    #
    # sights[["hCountLevel2", "cCountLevel2", "rCountLevel2", "aCountLevel2",
    #         "iCountLevel2", "nCountLevel2"]] = sights[["hCountLevel2", "cCountLevel2", "rCountLevel2", "aCountLevel2",
    #                                                    "iCountLevel2", "nCountLevel2"]].apply(lambda x: x * 4)
    #
    # sights[["hCountLevel3", "cCountLevel3", "rCountLevel3", "aCountLevel3",
    #         "iCountLevel3", "nCountLevel3"]] = sights[["hCountLevel3", "cCountLevel3", "rCountLevel3", "aCountLevel3",
    #                                                    "iCountLevel3", "nCountLevel3"]].apply(lambda x: x * 8)
    #
    # sights[["hCountLevel7", "cCountLevel7", "rCountLevel7", "aCountLevel7",
    #         "iCountLevel7", "nCountLevel7"]] = sights[["hCountLevel7", "cCountLevel7", "rCountLevel7", "aCountLevel7",
    #                                                    "iCountLevel7", "nCountLevel7"]].apply(lambda x: x * 16)
    #
    # column_list = list(sights)
    # column_list.remove("cityId")
    # sights["cSum"] = sights[column_list].sum(axis = 1)
    #
    # print(sights.head(100))


if __name__ == '__main__':
    main()