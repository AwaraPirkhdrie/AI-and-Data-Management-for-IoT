'''
This Python script solves the problems outlined in assignment Task_A2.2_I.
Author: Awara Pirkhdrie
Date: 2024-02-05


I- Based on the instruction on the distribution transformation, transform the "calories" column to take the shape of a distribution close to normal distribution. The current distribution looks
something like the below figure. Experiment with different transforms (log, cube, etc.) to find the right one. 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

'''Ladda in datasetet'''
data = pd.read_csv('applewatch/aw_fb_data.csv')

'''
Tillämpa logaritmisk transformation på "calories" kolumnen
Notera: Vi lägger till en liten konstant för att undvika log(0) eftersom det är odefinierat
'''
data['log_calories'] = np.log(data['calories'] + 1)

'''Visualisera den transformerede fördelningen'''
plt.figure(figsize=(10, 6))
sns.histplot(data['log_calories'], kde=True, bins=30)
plt.title('Log Transformation of Calories Distribution')
plt.xlabel('Log(Calories)')
plt.ylabel('Frequency')
plt.show()
