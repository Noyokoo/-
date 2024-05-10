import pandas as pd
from datetime import datetime
import os

csv_file_path = 'filename.csv'
if os.path.exists(csv_file_path):
    dataframe = pd.read_csv(csv_file_path, index_col=0)
else:
    columns = ['year', 'month', 'day', 'hour', 'minute', 'second']
    dataframe = pd.DataFrame(columns=columns)
now = datetime.now()
new_row = pd.DataFrame([{
    'year': now.year,
    'month': now.month,
    'day': now.day,
    'hour': now.hour,
    'minute': now.minute,
    'second': now.second
}])
dataframe = pd.concat([dataframe, new_row], ignore_index=True)
dataframe.to_csv(csv_file_path)
print(csv_file_path)