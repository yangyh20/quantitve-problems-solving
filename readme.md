## Homework1

杨雨函 2401212468

URL: https://github.com/yangyh20/quantitve-problems-solving.git

Write code that can fetch the US CPI data and reports the last 4 quarters of inflation in the US.

### 1.Set up environment
Install pandas using pip
```
pip install pandas
```
Install pandas-datareader using pip
```
pip install pandas-datareader
```

### 2.fetch data
Run /scripts/fetch_data.py 

p.s. If there is a problem: "ModuleNotFoundError: No module named 'src'", try :
```
import sys
sys.path.append(r'path_to\quantitve_problems_solving')
```
add this before "frome src.function import *".

### 3.Results
Inflation rates are stored in /data/inflation_rates.csv

p.s. If cannot find inflation_rates.csv, using
```
os.getcwd()
```
to check the current working directory, the /data/inflation_rates.csv is in this folder.
