import pandas as pd 

#Remove filename
#loop through the COVID-19 folder using OS
def load_to_memory(filename):
    data = pd.read_csv(f'{filename}', header=0) 

    print(data[0])
    print(data[1])
    return data

# time_series = '/Users/kaleighjaeger/Scripps/epidemiology/COVID-19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv''
# load_to_memory(time_series)


#json = data.to_json(path_or_buf='result.json')
#print('DataFrame: ')