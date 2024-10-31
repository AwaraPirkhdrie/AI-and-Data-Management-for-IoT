'''
This Python script solves the problems outlined in assignment Task_A2.1_II.
Author: Awara Pirkhdrie
Date: 2024-02-05

II- Visualize the data with a line graph with two axes: time & temperature with these criteria (1pt-Mandatory)
The color of the line should be orange
- Add labels for each axes (Temperature (degrees Celsius), Time(seconds)),
- Turn on the grids 
- Add legend on the top right corner - temperature
'''


import pandas as pd # Importerar pandas-biblioteket
import matplotlib.pyplot as plt # Importerar pyplot-modulen från matplotlib-biblioteket


'''Load the CSV file'''
_file_actual_path = '_tempratureDataValue.csv'
_data = pd.read_csv(_file_actual_path)


'''Data cleaning: Remove extra semicolons from the 'Temprature' column and convert to float'''
_data['Temprature'] = _data['Temprature;;;'].str.replace(';;;', '').astype(float)


'''Drop the original 'Temprature;;;' column'''
_data.drop(columns=['Temprature;;;'], inplace=True)


'''Plotting'''
plt.figure(figsize=(10, 6))
plt.plot(_data['Timesteps'], _data['Temprature'], color='orange', label='Temperature')


'''Adding labels, legend, and grid'''
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (degrees Celsius)')
plt.legend(loc='upper right')
plt.grid(True)


'''Show the plot'''
plt.show()
