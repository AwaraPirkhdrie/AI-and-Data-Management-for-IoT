'''
This Python script solves the problems outlined in assignment Task_A2.2_II.
Author: Awara Pirkhdrie
Date: 2024-02-05

II- Do these modifications on the dataframe made from the CSV dataset: (3pts Mandatory)
- Change the "In" and "Out" text of the "Out\In" column to 1 and 0 respectively.
- Separate the date and time in the "noted_date" column, into two separate columns.
- Keep only the data of the last day 08-12-2018, remove the rest of the rows with the appropriate function
'''
import pandas as pd

'''
Correcting the date format to match the dataset
'''
_iot_sensor_data = pd.read_csv('IOT-temp.csv')

'''
Convert 'noted_date' to datetime format with the correct format
'''
_iot_sensor_data['noted_date'] = pd.to_datetime(_iot_sensor_data['noted_date'], format='%d-%m-%Y %H:%M')

'''
Change the "In" and "Out" text in the "out/in" column to 1 and 0 respectively
'''
_iot_sensor_data['out/in'] = _iot_sensor_data['out/in'].map({'In': 1, 'Out': 0})

'''
Separate the date and time into two separate columns
'''
_iot_sensor_data['date'] = _iot_sensor_data['noted_date'].dt.date
_iot_sensor_data['time'] = _iot_sensor_data['noted_date'].dt.time

'''
Keep only the data of the last day (08-12-2018), and remove the rest
'''
_target_day = pd.Timestamp('2018-12-08')
_last_day_data = _iot_sensor_data[_iot_sensor_data['date'] == _target_day.date()]

'''
Display the first few rows of the filtered dataframe to confirm the changes
'''
_last_day_data.head()
