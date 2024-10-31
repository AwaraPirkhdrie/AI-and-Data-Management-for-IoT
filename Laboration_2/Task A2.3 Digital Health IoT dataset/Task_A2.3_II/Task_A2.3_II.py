'''
This Python script solves the problems outlined in assignment Task_A2.3_II.
Author: Awara Pirkhdrie
Date: 2024-02-05

II- As mentioned before, the data reflects 46 participants. Make a copy of the original dataframe and Find a way to keep one sample from each participant. 
Therefore, the new dataframeshould have 46 rows. You should use a specific function or a mix of functions in the instruction. Afterward,
visualize the "age", "height", and "weight" of the participants on each subplot(stacked plot). Grids should be on, Legends should be on top, 
and The color of the line plot for each subplot should be different. 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Laddar in datasetet
'''
data_aw_path = 'appleWatch/data_for_weka_aw.csv'
data_aw = pd.read_csv(data_aw_path)

'''
Deduplicerar baserat på antaget unika identifierare
'''
unique_samples = data_aw.drop_duplicates(subset=['age', 'gender', 'height', 'weight'])

'''
Skriv ut antalet unika deltagare efter deduplicering
'''
print(f"Antal unika deltagare efter deduplicering: {unique_samples.shape[0]}")

'''
Visualiserar "age", "height", och "weight"
'''
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

'''Ålder'''
axs[0].plot(unique_samples.index, unique_samples['age'], label='Ålder', color='blue', marker='o')
axs[0].set_title('Ålder hos deltagarna')
axs[0].set_ylabel('Ålder')
axs[0].grid(True)

'''Längd'''
axs[1].plot(unique_samples.index, unique_samples['height'], label='Längd', color='green', marker='o')
axs[1].set_title('Längd hos deltagarna')
axs[1].set_ylabel('Längd (cm)')
axs[1].grid(True)

'''Vikt'''
axs[2].plot(unique_samples.index, unique_samples['weight'], label='Vikt', color='red', marker='o')
axs[2].set_title('Vikt hos deltagarna')
axs[2].set_ylabel('Vikt (kg)')
axs[2].grid(True)

'''
Sätter legenden överst för alla subplots
'''
for ax in axs:
    ax.legend(loc='upper center')

plt.tight_layout()
plt.show()
