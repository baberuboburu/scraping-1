import pandas as pd
import numpy as np
import glob


# csvファイルの取得
data_list = glob.glob('csv/data_5/*.csv')
print(len(data_list))


# 各csvデータの列名を正しく命名する
right_data_list = []
for i in data_list:
  # データの1行目(列名になっている部分)を取り出してDataFrame型に直す
  a = pd.read_csv(i)
  b = a.columns
  d = pd.DataFrame(b)
  dd = pd.DataFrame.transpose(d)
  ## 列名を直す
  a.columns = ['先生名前','施設種別','写真URL','クリニック名','公式HP','電話番号','性別','血液型','出身大学','専門医種別']
  dd.columns = ['先生名前','施設種別','写真URL','クリニック名','公式HP','電話番号','性別','血液型','出身大学','専門医種別']
  # データ1行目を元のデータに加える
  aa = pd.concat([dd,a])
  # データを配列に格納する
  right_data_list.append(aa)


# csvファイルの連結
df = pd.concat(right_data_list)


# csvへの出力
df.to_csv("csv/data_5.csv",index=False)