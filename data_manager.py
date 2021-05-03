import pandas as pd 
import re
import os

daily_report_re = re.compile('\d\d-\d\d-\d\d\d\d.csv')

class DataManager:
    def __init__(self, source):
        if source == 'JHU-daily':
            daily_report_folder = 'COVID-19/csse_covid_19_data/csse_covid_19_daily_reports/'
            dailies = []
            for report_filename in os.listdir(daily_report_folder):
                if daily_report_re.search(report_filename):
                    daily_report = pd.read_csv(os.path.join(daily_report_folder, report_filename))
                    daily_report['date'] = report_filename.split('.')[0]
                    dailies.append(daily_report)

            self.df = pd.concat(dailies)
            self.df_groups = self.df.groupby(self.df.FIPS)


jhu_csse = DataManager('JHU-daily')
import pdb;pdb.set_trace()
