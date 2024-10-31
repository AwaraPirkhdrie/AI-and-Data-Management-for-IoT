
'''
This Python script solves the problems outlined in assignment Task A2.1_III.
Author: Awara Pirkhdrie
Date: 2024-02-05

III- With the functions mentioned in the instruction above, write a code to delete rows with normal room temperature. Delete the normal room temperature. Add data-value for 10 min
'''
import pandas as pd # Importerar pandas-biblioteket
import matplotlib.pyplot as plt  # Importerar pyplot-modulen från matplotlib-biblioteket


'''
Definierar sökvägen till CSV-filen som innehåller temperaturdata. Använder pandas read_csv-funktion för att läsa in CSV-filen och lagra datan i DataFrame-objektet _data
'''
_file_actual_path = '_tempratureDataValue.csv'
_data = pd.read_csv(_file_actual_path)


'''
Datarensning, Ta bort extra semikolon från kolumnen 'Temperatur' och konvertera till flytande
'''
_data['Temprature'] = _data['Temprature;;;'].str.replace(';;;', '').astype(float)


'''
Filtrerar data för att ta bort temperaturer under 22 grader Celsius
'''
_data_filtered_above_22 = _data[_data['Temprature'] >= 22]


'''
Plotta den filtrerade datan
'''
plt.figure(figsize=(10, 6))
plt.plot(_data_filtered_above_22['Timesteps'], _data_filtered_above_22['Temprature'], color='orange', label='Temperature')


'''
Adding labels, legend, and grid
'''
plt.xlabel('Time (seconds)')
plt.ylabel('Temperature (degrees Celsius)')
plt.legend(loc='upper right')
plt.grid(True)


'''
Display the plot
'''
plt.show()