import pandas as pd
import numpy as np
import glob


# csvファイルの取得
data_list = glob.glob('csv/data_1/*.csv')
print(len(data_list))


# 各csvデータの列名を正しく命名する
right_data_list = []
for i in data_list:
  # データの1行目(列名になっている部分)を取り出してDataFrame型に直す
  a = pd.read_csv(i)
  b = a.columns
  d = pd.DataFrame(b)
  dd = pd.DataFrame.transpose(d)
  # 列名を直すfeatures,words_1,words_2,words_3,infusions,HPs,names
  a.columns = ['クリニック特徴','医師からの一言(専門分野・得意とする点滴療法)','医師からの一言(点滴や治療において心掛けていること)','医師からの一言(来院を検討中の方へのメッセージ)','点滴療法','公式HP','責任者']
  dd.columns = ['クリニック特徴','医師からの一言(専門分野・得意とする点滴療法)','医師からの一言(点滴や治療において心掛けていること)','医師からの一言(来院を検討中の方へのメッセージ)','点滴療法','公式HP','責任者']
  # データ1行目を元のデータに加える
  aa = pd.concat([dd,a])
  # データを配列に格納する
  right_data_list.append(aa)


# csvファイルの連結
df = pd.concat(right_data_list)


# csvへの出力
df.to_csv("csv/data_1_detail.csv",index=False)