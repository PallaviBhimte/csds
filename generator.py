# This file lodes all file and keep only relavent one
# creates only one df out of all data

import os
import pandas as pd
from datetime import datetime

# columns to keep from hospital bed data
joinedcolumns = ['X', 'Y', 'HOSPITAL_NAME', 'HOSPITAL_TYPE', 'HQ_CITY', 'HQ_STATE', 'HQ_ZIP_CODE',
                 'COUNTY_NAME', 'STATE_FIPS', 'CNTY_FIPS', 'FIPS', 'NUM_LICENSED_BEDS', 'NUM_STAFFED_BEDS',
                 'NUM_ICU_BEDS', 'ADULT_ICU_BEDS', 'PEDI_ICU_BEDS', 'BED_UTILIZATION',
                 'Potential_Increase_In_Bed_Capac',
                 'AVG_VENTILATOR_USAGE']

# empty df
data = pd.DataFrame(columns=joinedcolumns)


# method to combine df
def datacombiner(df, data):
    if data.shape[0] == 0:
        data = df
    else:
        data = pd.concat([data, df])
    return data


# reading all files and preparing one df for hospital bed data
data_folder = "/Users/ayushranjan/Documents/MY_Folder/csds/data"
# for months in os.listdir(data_folder):
#     if months != ".DS_Store":
#         for days in os.listdir(os.path.join(data_folder, months)):
#             if days != ".DS_Store":
#                 csv_path = os.path.join(data_folder, months)
#                 csv_path = csv_path + "/" + days
#                 df = pd.read_csv(csv_path)
#                 df = df.loc[:, joinedcolumns]
#                 df['date'] = days[:-4]
#                 data = datacombiner(df, data)
#
# data = data.reset_index(drop=True)
# print(data.shape)
# print(data.columns)

covid_data_path = "/Users/ayushranjan/Documents/MY_Folder/csds/covid_time " \
                  "series/covid-19-testing-data_dataset_states_daily.csv "

covid_df = pd.read_csv(covid_data_path)
# print(covid_df.shape)

# checking sparse columns in the data
# print(covid_df.isnull().sum() / covid_df.shape[0])

# selecting columns which have considerable amount of data
covid_columns = ['date', 'state', 'positive', 'negative',
                 'hospitalizedCurrently', 'hospitalizedCumulative', 'inIcuCurrently',
                 'onVentilatorCurrently', 'recovered', 'dataQualityGrade', 'lastUpdateEt', 'dateModified',
                 'checkTimeEt', 'death', 'hospitalized', 'dateChecked',
                 'totalTestsViral', 'positiveCasesViral', 'deathConfirmed',
                 'fips', 'positiveIncrease', 'negativeIncrease',
                 'total', 'totalTestResultsSource', 'totalTestResults',
                 'totalTestResultsIncrease', 'posNeg', 'deathIncrease',
                 'hospitalizedIncrease', 'hash', 'commercialScore',
                 'negativeRegularScore', 'negativeScore', 'positiveScore', 'score']

covid_df = covid_df.loc[:, covid_columns]


# fix the date field
# print("current data type = " + covid_df.date.dtype)

covid_df.date = covid_df.date.astype(str)

def convert_time(str):
    date = datetime.strptime(str, "%Y%m%d")
    return date


# covid_df.date = pd.datetime(covid_df.date, format="%Y%m%d")
covid_df.date = covid_df['date'].apply(lambda x: convert_time(x))

# print("current data type = {}".format(covid_df.date.dtype))

# Treating missing values

# POSITIVE COLUMN

# x = covid_df.loc[covid_df.positive.isnull(), :]

# The observations before 30/03/2020 are null across all features
# possible reason can be, beginning of pandemic
# remove all obsevations as can't be use or imputed

covid_df = covid_df[covid_df.positive.notna()]

# features not useful(remove)
# negative, hospitalizedCumulative, recovered , lastUpdateEt, dateModified,
# checkTimeEt, dateChecked,

print(covid_df.isnull().sum() / covid_df.shape[0])