import pandas as pd
new_file_path = '/project/pythonProject1/data/Updated_Dataset_without_reg_time.csv'
data = pd.read_csv(new_file_path)

# Convert 'edregtime' and 'edouttime' to datetime format
data['edregtime'] = pd.to_datetime(data['edregtime'], errors='coerce')
data['edouttime'] = pd.to_datetime(data['edouttime'], errors='coerce')

# Calculate the time difference in seconds and store it in a new column 'reg_time'
data['reg_time'] = (data['edouttime'] - data['edregtime']).dt.total_seconds()

# Rearrange columns to place 'reg_time' between 'edouttime' and 'hospital_expire_flag'
columns = list(data.columns)
edouttime_index = columns.index('edouttime')
columns.insert(edouttime_index + 1, columns.pop(columns.index('reg_time')))
data = data[columns]

# Save the updated CSV file
final_file_path = '/project/pythonProject1/data/Updated_Dataset_with_new_reg_time.csv'

