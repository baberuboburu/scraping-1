import pandas as pd
import numpy as np
import glob


# csvファイルの取得
data_list = []
data_list.extend(glob.glob('csv/data_6/data_34.csv'))
data_list.extend(glob.glob('csv/data_6/data_132.csv'))
data_list.extend(glob.glob('csv/data_6/data_502.csv'))
data_list.extend(glob.glob('csv/data_6/data_503.csv'))

# 各csvデータの列名を正しく命名する
right_data_list = []
for i in range(len(data_list)):
  # データの1行目(列名になっている部分)を取り出してDataFrame型に直す
  a = pd.read_csv(data_list[i])
  if i == 1:
    print(len(a))
    a = a.iloc[47530:]
    print(len(a))
  print(type(a))
  b = a.columns
  d = pd.DataFrame(b)
  dd = pd.DataFrame.transpose(d)
  ## 列名を直す
  a.columns = ['クリニック名','住所','都道府県','管理者名','再生医療の名称','認定再生医療等委員会の名称','部位','治療法','区分']
  dd.columns = ['クリニック名','住所','都道府県','管理者名','再生医療の名称','認定再生医療等委員会の名称','部位','治療法','区分']
  # データ1行目を元のデータに加える
  aa = pd.concat([dd,a])
  # データを配列に格納する
  right_data_list.append(aa)


# csvファイルの連結
df = pd.concat(right_data_list)


# csvへの出力
df.to_csv("csv/data_6.csv",index=False)