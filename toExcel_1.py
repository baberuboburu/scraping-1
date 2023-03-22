import pandas as pd

df = pd.read_csv('csv/data_1.csv')
labels = ['写真URL','施設名','住所','電話番号','診療科目','都道府県','クリニック特徴','医師からの一言(専門分野・得意とする点滴療法)','医師からの一言(点滴や治療において心掛けていること)','医師からの一言(来院を検討中の方へのメッセージ)','点滴療法','公式HP','責任者'] 
df_firstRow = df.columns
df.columns = labels
df.iloc[0] = df_firstRow
df.to_excel('excel/data_1.xlsx')