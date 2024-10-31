'''
This Python script solves the problems outlined in assignment Task_A2.2_I.
Author: Awara Pirkhdrie
Date: 2024-02-05


I- Visualize the indoor and outdoor temperature in one plot with different colors of your choice for the last week (strat from the top 02-12-2018 to 08-12-2018)
'''

import pandas as pd
import matplotlib.pyplot as plt


'''
Load the dataset
'''
_iot_data_df = pd.read_csv('IOT-temp.csv')


'''
Convert 'noted_date' to datetime format
'''
_iot_data_df['noted_date'] = pd.to_datetime(_iot_data_df['noted_date'], format = '%d-%m-%Y %H:%M')



'''
Filter data for the specified week
'''
_week_start_date = pd.Timestamp('2018-12-02')
_week_end_date = pd.Timestamp('2018-12-08')
_filtered_week_df = _iot_data_df[(_iot_data_df['noted_date'] >= _week_start_date) & (_iot_data_df['noted_date'] <= _week_end_date)]


'''
Separate indoor and outdoor temperature readings
'''
_indoor_temp_df = _filtered_week_df[_filtered_week_df['out/in'] == 'In']
_outdoor_temp_df = _filtered_week_df[_filtered_week_df['out/in'] == 'Out']


'''Plotting'''
plt.figure(figsize=(12, 8))
plt.plot(_indoor_temp_df['noted_date'], _indoor_temp_df['temp'], label='Indoor Temperature', color='blue', marker='o')
plt.plot(_outdoor_temp_df['noted_date'], _outdoor_temp_df['temp'], label='Outdoor Temperature', color='green', marker='x')
plt.title('Indoor vs Outdoor Temperature (02-12-2018 to 08-12-2018)')
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()  # Adjust layout to ensure labels are not cut off
plt.show()