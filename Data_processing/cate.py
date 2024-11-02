import pandas as pd

# Load the user's uploaded file
file_path = '/project/pythonProject1/data/Processing_data.csv'
data = pd.read_csv(file_path)

# Drop specified columns and save the resulting dataframe
columns_to_drop = [
    'troponin_level_category', 'hdl_cholesterol_category',
    'ldl_cholesterol_calculated_category', 'ldl_cholesterol_measured_category',
    'total_cholesterol_category', 'natiuretic_category',
    'creatinine_category', 'glucose_category',
    'ck_mb_category', 'ck_cpk_category', 'c_index_category'
]
data_cleaned = data.drop(columns=columns_to_drop)

# Save the cleaned data
cleaned_file_path = '/project/pythonProject1/data/Cleaned_Processing_data.csv'
data_cleaned.to_csv(cleaned_file_path, index=False)

# Function to categorize data into 'low', 'medium', 'high' based on thresholds
def discretize_column(series, low_threshold, high_threshold):
    return pd.cut(series, bins=[-float('inf'), low_threshold, high_threshold, float('inf')],
                  labels=['low', 'medium', 'high'], right=False)

# Define clinical thresholds for columns
thresholds = {
    'average_troponin_level': (0.04, 0.4),
    'average_cholesterol_HDL': (40, 60),
    'average_cholesterol_LDL_Calculated': (100, 160),
    'average_cholesterol_LDL_Measured': (100, 160),
    'average_cholesterol_Total': (200, 240),
    'min_natiurectic': (50, 100),
    'max_natiurectic': (50, 100),
    'avg_natiurectic': (50, 100),
    'min_creatinine': (0.6, 1.2),
    'max_creatinine': (0.6, 1.2),
    'avg_creatinine': (0.6, 1.2),
    'min_icu_cholestrol': (150, 200),
    'max_icu_cholestrol': (150, 200),
    'avg_icu_cholestrol': (150, 200),
    'min_glucose': (70, 100),
    'max_glucose': (70, 100),
    'avg_glucose': (70, 100),
    'min_ck_mb': (3, 5),
    'max_ck_mb': (3, 5),
    'avg_ck_mb': (3, 5),
    'min_ck_cpk': (20, 200),
    'max_ck_cpk': (20, 200),
    'avg_ck_cpk': (20, 200),
    'min_c_index': (1, 2),
    'max_c_index': (1, 2),
    'avg_c_index': (1, 2)
}

# Apply discretization to columns based on thresholds
for column, (low, high) in thresholds.items():
    if column in data_cleaned.columns:
        data_cleaned[f'{column}_category'] = discretize_column(data_cleaned[column], low, high)

# Save the discretized dataframe
discretized_file_path = '/project/pythonProject1/data/Discretized_Processing_data.csv'
data_cleaned.to_csv(discretized_file_path, index=False)

# Load the discretized file and assign numeric values to ordered categories
df = pd.read_csv(discretized_file_path)

# Columns to map from categories ('low', 'medium', 'high') to integers
category_columns = [
    'average_troponin_level_category', 'average_cholesterol_HDL_category',
    'average_cholesterol_LDL_Calculated_category', 'average_cholesterol_LDL_Measured_category',
    'average_cholesterol_Total_category', 'min_natiurectic_category', 'max_natiurectic_category',
    'avg_natiurectic_category', 'min_creatinine_category', 'max_creatinine_category',
    'avg_creatinine_category', 'min_icu_cholestrol_category', 'max_icu_cholestrol_category',
    'avg_icu_cholestrol_category', 'min_glucose_category', 'max_glucose_category',
    'avg_glucose_category', 'min_ck_mb_category', 'max_ck_mb_category',
    'avg_ck_mb_category', 'min_ck_cpk_category', 'max_ck_cpk_category',
    'avg_ck_cpk_category', 'min_c_index_category', 'max_c_index_category',
    'avg_c_index_category'
]

# Map categories to integers
category_mapping = {'low': 0, 'medium': 1, 'high': 2}
for column in category_columns:
    if column in df.columns:
        df[f'{column}_numeric'] = df[column].map(category_mapping)

# Save the dataframe with numeric categories
updated_file_path = '/project/pythonProject1/data/Updated_Data_with_Numeric_Categories.csv'
df.to_csv(updated_file_path, index=False)

# Load the file and add 'Death' column based on 'deathtime' presence
df = pd.read_csv(updated_file_path)
df['Death'] = df['deathtime'].notna().astype(int)

# Reorder 'Death' column to be next to 'deathtime'
col_order = df.columns.tolist()
death_index = col_order.index('deathtime') + 1
col_order.insert(death_index, col_order.pop(col_order.index('Death')))
df = df[col_order]

# Save the final updated dataframe
updated_file_with_death_path = '/project/pythonProject1/data/Updated_Data_with_Death_Column.csv'
df.to_csv(updated_file_with_death_path, index=False)
