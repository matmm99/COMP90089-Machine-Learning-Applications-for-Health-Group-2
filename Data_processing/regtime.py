import pandas as pd
new_file_path = '/project/pythonProject1/data/Updated_Dataset_without_reg_time.csv'
data = pd.read_csv(new_file_path)

# Convert 'edregtime' and 'edouttime' to datetime
data['edregtime'] = pd.to_datetime(data['edregtime'], errors='coerce')
data['edouttime'] = pd.to_datetime(data['edouttime'], errors='coerce')

# Calculate 'reg_time'
data['reg_time'] = data['edouttime'] - data['edregtime']

# Reorder columns to place 'reg_time' between 'edouttime' and 'hospital_expire_flag'
columns = list(data.columns)
edouttime_index = columns.index('edouttime')
columns.insert(edouttime_index + 1, 'reg_time')
data = data[columns]

# Reorder columns to place 'reg_time' between 'edouttime' and 'hospital_expire_flag'
columns = list(data.columns)
edouttime_index = columns.index('edouttime')
columns.insert(edouttime_index + 1, 'reg_time')
data = data[columns]

# Convert 'stay_time' and 'reg_time' from seconds to hours, rounding to 2 decimal places
data['stay_time'] = (data['stay_time'] / 3600).round(2)
data['reg_time'] = (data['reg_time'] / pd.Timedelta(hours=1)).round(2)

# Save the updated dataset to a new CSV file
final_file_path = '/project/pythonProject1/data/Updated_Dataset_with_new_reg_time.csv'
data.to_csv(final_file_path, index=False)

# Save the updated CSV file
final_file_path = '/project/pythonProject1/data/Updated_Dataset_with_new_reg_time.csv'


# Convert 'stay_time' and 'reg_time' from seconds to hours and round to 2 decimal places
data['stay_time'] = (data['stay_time'] / 3600).round(2)
data['reg_time'] = (data['reg_time'] / 3600).round(2)

# Display the updated dataset to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Updated Data", dataframe=data)
