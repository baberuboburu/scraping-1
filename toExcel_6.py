import pandas as pd

df = pd.read_csv('csv/data_6.csv')
df = df.drop(4956)
df.to_excel('excel/data_6.xlsx')