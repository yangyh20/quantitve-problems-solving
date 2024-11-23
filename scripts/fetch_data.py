# Write code that can fetch the US CPI data and reports the last 4 quarters of inflation in the US.

# import sys
# sys.path.append(r'd:\classes\quantitve_problems\quantitve_problems_solving')
import os
from datetime import datetime
from src.function import *

# get cpi data using function in /src/function.py
Start_date='2020-01-01'
End_date=datetime.now()
cpi_data = fetch('CPIAUCSL','fred',Start_date,End_date)

# Calculate inflation rate
cpi_quarterly=cpi_data.resample('QE').mean()
inflation_rates=cpi_quarterly.pct_change() * 100
inflation_rates=inflation_rates.dropna()
print(f'The last 4 quarters of inflation:\n{inflation_rates.tail(4)}')

# Save result in data folder
data_folder_path=os.path.join(os.getcwd(), 'data')
if not os.path.exists(data_folder_path):
    print(f"Creating directory: {data_folder_path}")
    os.makedirs(data_folder_path)
file_path = os.path.join(data_folder_path, 'inflation_rates.csv')
inflation_rates.to_csv(file_path)
