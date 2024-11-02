
# Load the new dataset
import pandas as pd

file_path_new = 'D:/project/pythonProject1/data/time_Data.csv'
new_data = pd.read_csv(file_path_new)

# Identify the columns to be standardized
columns_to_standardize = [
    'average_troponin_level', 'average_cholesterol_HDL', 'average_cholesterol_LDL_Calculated',
    'average_cholesterol_LDL_Measured', 'average_cholesterol_Total', 'min_natiurectic', 
    'max_natiurectic', 'avg_natiurectic', 'min_creatinine', 'max_creatinine', 'avg_creatinine', 
    'min_icu_cholestrol', 'max_icu_cholestrol', 'avg_icu_cholestrol', 'min_glucose', 'max_glucose', 
    'avg_glucose', 'min_ck_mb', 'max_ck_mb', 'avg_ck_mb', 'min_ck_cpk', 'max_ck_cpk', 'avg_ck_cpk', 
    'min_c_index', 'max_c_index', 'avg_c_index', 'min_abp_sys', 'max_abp_sys', 'avg_abp_sys', 
    'min_abpd', 'max_abpd', 'avg_abpd', 'min_abpm', 'max_abpm', 'avg_abpm', 'min_nbps', 'max_nbps', 
    'avg_nbps', 'min_nbpd', 'max_nbpd', 'avg_nbpd', 'min_nbpm', 'max_nbpm', 'avg_nbpm', 'min_heartv', 
    'max_heartv', 'avg_heartv', 'min_hearta', 'max_hearta', 'avg_hearta'
]

# Standardize the selected columns
standardized_data = new_data.copy()
standardized_data[columns_to_standardize] = (standardized_data[columns_to_standardize] - standardized_data[columns_to_standardize].mean()) / standardized_data[columns_to_standardize].std()

# Save the standardized data to a new CSV file
output_path = 'D:/project/pythonProject1/data/standardized_time_data.csv'
standardized_data.to_csv(output_path, index=False)


