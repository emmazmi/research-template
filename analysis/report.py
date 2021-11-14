import pandas as pd

data = pd.read_csv("output/input.csv")

data['covid_date'] = pd.to_datetime(data['covid_date'])
data['long_covid_date'] = pd.to_datetime(data['long_covid_date'])

data['time'] = data['long_covid_date'] - data['covid_date']

data.to_csv("output/times.csv")

#fig = data.time.plot.hist().get_figure()
#fig.savefig("output/descriptive.png")