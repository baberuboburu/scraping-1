import pandas as pd

df = pd.read_csv('csv/data_2.csv')
labels = ['施設名','エリア','電話番号','メールアドレス','公式サイト']
df_firstRow = df.columns
df.columns = labels
df.iloc[0] = df_firstRow
df.to_excel('excel/data_2.xlsx')