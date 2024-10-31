
'''

This Python script solves the problems outlined in assignment Task_A2.4.
Author: Awara Pirkhdrie
Date: 2024-02-05

Task A2.4: Gone with the Wind! (3pts - Optional) You are presented with a dataset of wind speed and the wind angle of the wind from a meteorological site. 
The problem is that some data while being so similar have values very differently. Angles are not ideal as model inputs since 360° and 0° should be in close proximity, 
smoothly transitioning.  The direction becomes irrelevant when there is no wind blowing. (for example 0.1m/s at 359° is not represented well or the similarity of 10 m/s at 0.1° 
and 359.9°).  The model will find it more straightforward to interpret if you transform the columns for wind direction and velocity into a wind vector (X and Y).
Download the weather dataset from here: Climate2016.csv (https://mau.instructure.com/courses/16134/files/2498686?wrap=1)
 (https://mau.instructure.com/courses/16134/files/2498686/ download?download_frd=1)
We only focus on the columns "windvelo m/s" and "winddeg deg" which represent wind velocity and wind direction. See the data summary with the functions in the text to get the overview of the data 

- Use mathematical functions to convert the Wind "speed&velocity" vector into two separate X & Y vectors. Add two more columns to your CSV file as windveloX and windveloY, and save your CSV file.
- Use the normalize function to normalize the data
- Use the "Hist2d" function to visualize the data before and after changes. It should look something like the two below figures
'''

import pandas as pd # Importerar pandas-biblioteke
import numpy as np # Importerar numpy-biblioteket
from sklearn.preprocessing import MinMaxScaler # Importerar MinMaxScaler från scikit-lear
import matplotlib.pyplot as plt # Importerar matplotlibs pyplot-modul

'''
Definierar en lista med kolumner som ska användas när datasetet läses in, Ange kolumnnamnen manuellt baserat på felutdata.
'''
_columns = [
    "Date Time", "press (mbar)", "Temp (degC)", "Temppot (K)", "Tempdew (degC)", 
    "relativehum (%)", "VPressmax (mbar)", "VPressact (mbar)", "VPressdef (mbar)", 
    "sh (g/kg)", "H2OC (mmol/mol)", "relativeho (g/m**3)", "windvelo (m/s)", 
    "max. windvelo (m/s)", "winddeg (deg)"
]

'''
Ladda datauppsättningen med manuella kolumner och korrekt analys, Läser in datasetet från den angivna sökvägen, använder kommatecken som avgränsare.
'''
_file_actual_path = 'Climate2016.csv'
_climate_data_2016 = pd.read_csv(_file_actual_path, delimiter=',', names=_columns, header=0)

'''
Beräknar X- och Y-komponenterna för vindhastigheten baserat på vindens hastighet och riktning och lägger till dessa som nya kolumner i datasetet.
'''
_climate_data_2016['windveloX'] = _climate_data_2016['windvelo (m/s)'] * np.cos(np.radians(_climate_data_2016['winddeg (deg)']))
_climate_data_2016['windveloY'] = _climate_data_2016['windvelo (m/s)'] * np.sin(np.radians(_climate_data_2016['winddeg (deg)']))

'''
Skapar en instans av MinMaxScaler, som används för att skala och transformera data så att den passar inom en given radie, 
Normaliserar de beräknade X- och Y-komponenterna för vindhastigheten till ett område mellan 0 och 1.
'''
_min_max_normalizer = MinMaxScaler()
_climate_data_2016[['windveloX', 'windveloY']] = _min_max_normalizer.fit_transform(_climate_data_2016[['windveloX', 'windveloY']])

plt.figure(figsize=(14, 6)) # Skapar en ny figur för visualisering med specificerade dimensioner.
plt.subplot(1, 2, 1) # Skapar en subplot i figuren. Detta är den första subploten i en 1x2 layout.
plt.hist2d(_climate_data_2016['winddeg (deg)'], _climate_data_2016['windvelo (m/s)'], bins=(50, 50), cmap='viridis') # Skapar en 2D-histogram för att visualisera distributionen av vindhastighet och vindriktning med 50 bins för varje axel och använder färgkartan 'viridis'.
plt.colorbar() # Lägger till en färgskala till histogrammet
plt.title('Original Wind Velocity and Direction')
plt.xlabel('Wind Velocity (m/s)')
plt.ylabel('Wind Direction (degrees)')

'''
Visualisering efter ändringar: Normaliserade vindvektorkomponenter (X och Y)
'''
plt.subplot(1, 2, 2)
plt.hist2d(_climate_data_2016['windveloX'], _climate_data_2016['windveloY'], bins=(50, 50), cmap='viridis')
plt.colorbar()
plt.title('Normalized Wind Vector Components (X and Y)')
plt.xlabel('windveloX')
plt.ylabel('windveloY')
plt.tight_layout()
plt.show()

'''Spara den ändrade datamängden till en ny CSV-fil'''
_output_file_path = 'c:/Users/0000/Desktop/lab2/Task A2.4 Gone with the Wind/Modified_Climate2016.csv'  # Uppdatera med den faktiska utdatasökvägen
_climate_data_2016.to_csv(_output_file_path, index=False)

print("Dataset saved to:", _output_file_path)
