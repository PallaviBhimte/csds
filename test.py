import os
import pandas as pd
import numpy as np

# method to join df


joinedcolumns = ['X', 'Y', 'HOSPITAL_NAME', 'HOSPITAL_TYPE', 'HQ_CITY', 'HQ_STATE', 'HQ_ZIP_CODE',
                 'COUNTY_NAME', 'STATE_FIPS', 'CNTY_FIPS', 'FIPS', 'NUM_LICENSED_BEDS', 'NUM_STAFFED_BEDS',
                 'NUM_ICU_BEDS', 'ADULT_ICU_BEDS', 'PEDI_ICU_BEDS', 'BED_UTILIZATION',
                 'Potential_Increase_In_Bed_Capac',
                 'AVG_VENTILATOR_USAGE']

data = pd.DataFrame(columns=joinedcolumns)


def datacombiner(df, data):
    if data.shape[0] == 0:
        data = df
    else:
        data = pd.concat([data, df])
    return data


data_folder = "/Users/ayushranjan/Documents/MY_Folder/csds/data"
for months in os.listdir(data_folder):
    if months != ".DS_Store":
        for days in os.listdir(os.path.join(data_folder, months)):
            if days != ".DS_Store":
                csv_path = os.path.join(data_folder, months)
                csv_path = csv_path + "/" + days
                df = pd.read_csv(csv_path)
                df = df.loc[:, joinedcolumns]
                df['date'] = days[:-4]
                data = datacombiner(df, data)

data = data.reset_index(drop=True)
print(data.shape)
# print(data.columns)

