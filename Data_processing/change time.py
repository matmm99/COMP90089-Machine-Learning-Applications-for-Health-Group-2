# Convert 'stay_time' and 'reg_time' from seconds to hours and round to 2 decimal places
data['stay_time'] = (data['stay_time'] / 3600).round(2)
data['reg_time'] = (data['reg_time'] / 3600).round(2)

# Display the updated dataset to the user
import ace_tools as tools; tools.display_dataframe_to_user(name="Updated Data", dataframe=data)
