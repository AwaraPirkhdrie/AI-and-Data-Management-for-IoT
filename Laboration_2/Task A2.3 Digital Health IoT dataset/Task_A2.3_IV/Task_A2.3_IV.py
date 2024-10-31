'''
This Python script solves the problems outlined in assignment Task_A2.3_IV.
Author: Awara Pirkhdrie
Date: 2024-02-05

IV- Normalize the "age", "height", and "weight", and Standardize "steps" and "height rate" columns in a separate column at the end of the dataframe
'''
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import pandas as pd

'''Assuming your DataFrame is loaded as 'data'''
_data = pd.read_csv('appleWatch/aw_fb_data.csv')

'''Initialize scalers'''
_min_max_scaler = MinMaxScaler()
_standard_scaler = StandardScaler()

'''Normalize "age", "height", and "weight"'''
_data['age_normalized'] = _min_max_scaler.fit_transform(_data[['age']])
_data['height_normalized'] = _min_max_scaler.fit_transform(_data[['height']])
_data['weight_normalized'] = _min_max_scaler.fit_transform(_data[['weight']])

'''
Standardize "steps" and "heart rate" 
Note: Adjust the column name for heart rate if it's different in your dataset'''
_heart_rate_column = 'hear_rate' if 'hear_rate' in _data.columns else 'heart_rate'
_data['steps_standardized'] = _standard_scaler.fit_transform(_data[['steps']])
_data['heart_rate_standardized'] = _standard_scaler.fit_transform(_data[[_heart_rate_column]])

'''Display the first few rows to verify the changes'''
print(_data[['age_normalized', 'height_normalized', 'weight_normalized', 'steps_standardized', 'heart_rate_standardized']].head())
