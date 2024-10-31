'''
This Python script solves the problems outlined in assignment Task_A2.3_II.
Author: Awara Pirkhdrie
Date: 2024-02-05

III- Visualize "steps", "heart_rate", and "calories" of the first three participants in three plots with subplots (stacked plot), 
in a way that the steps of each three participants are depicted with different colored lines, the same for other two datasets. 
The legends should be on the top corner of each plot (participant #1, participant #2, participant#3)
'''
import pandas as pd
import matplotlib.pyplot as plt

'''Ladda in datasetet'''
aw_fb_data = pd.read_csv('applewatch/aw_fb_data.csv')

'''Definiera metrics för visualisering'''
metrics = ['steps', 'hear_rate', 'calories']
colors = ['blue', 'green', 'red']  # Färger för varje antagen deltagare

'''Skapa subplots'''
fig, axs = plt.subplots(3, 1, figsize=(10, 15))

'''
Antagande: Vi tar de första distinkta sekvenserna av inlägg som representanter för olika deltagare
Observera: Detta är en förenkling och bör anpassas baserat på faktisk deltagaridentifiering'''
for i, metric in enumerate(metrics):
    for j in range(3):  # För de första 3 antagna deltagarna
        # Slicerar data för varje antagen deltagare - en approximation
        participant_data = aw_fb_data.iloc[j*20:(j+1)*20]  # Antagande: 20 inlägg per deltagare
        axs[i].plot(participant_data['X1'], participant_data[metric], label=f'Participant #{j+1}', color=colors[j], marker='o')
    
    axs[i].set_title(f'{metric.capitalize()} over Time')
    axs[i].set_xlabel('Entry Index')
    axs[i].set_ylabel(metric.capitalize())
    axs[i].legend(loc='upper right')
    axs[i].grid(True)

plt.tight_layout()
plt.show()

