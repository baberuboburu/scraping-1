import pandas as pd

df = pd.read_csv('csv/data_6.csv')
labels = ['写真URL','施設名','エリア','住所','電話番号','営業時間','対応ジャンル','公式サイト','Youtube']
df_firstRow = df.columns
df.columns = labels
df.iloc[0] = df_firstRow
df.to_excel('excel/data_6.xlsx')