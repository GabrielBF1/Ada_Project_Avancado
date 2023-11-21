import pandas as pd

covid_dataset = pd.read_csv('./dataset/cases-brazil-cities-time_changesOnly.csv')

print(covid_dataset.head());