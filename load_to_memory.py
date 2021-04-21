import pandas as pd 

def load_to_memory(filename):
	data = pd.read_csv(f'{filename}') 
	json = data.to_json(path_or_buf='result.json')
	df = pd.DataFrame(data=data)
	print('DataFrame: ')
	print(df)
	
daily_report = 'COVID-19/csse_covid_19_data/csse_covid_19_daily_reports_us/01-01-2021.csv'
load_to_memory(daily_report)
