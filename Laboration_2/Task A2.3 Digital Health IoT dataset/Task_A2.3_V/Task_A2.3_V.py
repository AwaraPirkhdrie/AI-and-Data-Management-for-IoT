'''
This Python script solves the problems outlined in assignment Task_A2.3_V.
Author: Awara Pirkhdrie
Date: 2024-02-05

V- Split the dataset into three categories with the following distribution: Train (70%), Validation (15%), and Test (15%)
'''
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler

'''Step 1: Load the dataset'''
_file_path = 'Dataset/appleWatch/aw_fb_data.csv'  # Update this with the actual path to your file
_data = pd.read_csv(_file_path)

'''
Step 2: Normalize and Standardize selected columns
Initialize scalers'''
_min_max_scaler = MinMaxScaler()
_standard_scaler = StandardScaler()

'''
Normalize "age", "height", and "weight"
'''
_data['age_normalized'] = _min_max_scaler.fit_transform(_data[['age']])
_data['height_normalized'] = _min_max_scaler.fit_transform(_data[['height']])
_data['weight_normalized'] = _min_max_scaler.fit_transform(_data[['weight']])

'''
Standardize "steps" and "heart rate"
'''
_heart_rate_column = 'hear_rate' if 'hear_rate' in _data.columns else 'heart_rate'
_data['steps_standardized'] = _standard_scaler.fit_transform(_data[['steps']])
_data['heart_rate_standardized'] = _standard_scaler.fit_transform(_data[[_heart_rate_column]])

'''
Step 3: Split the dataset into Train, Validation, and Test sets
Split the data into training and temporary sets (70% train, 30% temp)
'''
_train_data, _temp_data = train_test_split(_data, test_size=0.3, random_state=42)

'''
Split the temporary set into validation and test sets (50% validation, 50% test of the temp_data)
'''
_validation_data, _test_data = train_test_split(_temp_data, test_size=0.5, random_state=42)

'''
Display the sizes of each dataset to verify the splits
'''
print(f"Training set size: {len(_train_data)}")
print(f"Validation set size: {len(_validation_data)}")
print(f"Test set size: {len(_test_data)}")
