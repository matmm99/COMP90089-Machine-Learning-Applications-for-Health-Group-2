# Load the dataset
import pandas as pd
file_path = 'D:/project/pythonProject1/data/full_ami_data.csv'
df = pd.read_csv(file_path)

# Remove duplicate subject_id entries
df_unique = df.drop_duplicates(subset=['subject_id'])

# Save the resulting DataFrame to a new CSV file
output_path = '/project/pythonProject1/data/full_ami_data_unique.csv'
df_unique.to_csv(output_path, index=False)