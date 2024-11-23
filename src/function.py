# get data through pandas_datareader and clean it

import pandas_datareader.data 
from datetime import datetime

def fetch(dataname='CPIAUCSL', source='fred', start_date=datetime.now(), end_date=datetime.now()):
    data = pandas_datareader.data.DataReader(name = dataname,
                                    data_source = source,
                                    start = start_date,
                                    end = end_date)

    data=data.dropna()
    return data

