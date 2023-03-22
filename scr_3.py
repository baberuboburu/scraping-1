import pandas as pd
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定数の定義
csv_path = '/Users/sasakiaoto/Downloads/scraping_1/csv/data_3.csv'
url = 'https://cellbank.co.jp/search/'
area_names = ['北海道','関東','中部','関西','九州・沖縄']
num_lists = [1,48,4,21,4]


# XPATHの定義
dl_xpath = '/html/body/div[1]/div/section[1]/div[3]/section/dl'
area_xpaths = []
ul_xpaths = []
for i in range(len(area_names)):
  area_xpath = f'/html/body/div[1]/div/section[1]/div[3]/section/dl/dt[{i+1}]'
  area_xpaths.append(area_xpath)
  if i == 0:
    ul_xpath = f'{dl_xpath}/dd[{i+1}]/ul'
  else:
    ul_xpath = f'{dl_xpath}/dd[{i+1}]/ul[2]'
  ul_xpaths.append(ul_xpath)


# 1データのスクレイピング
browser = webdriver.Chrome()


def getMatrix():
  browser.get(url)
  # matrixに格納する配列の定義
  matrix = []
  images = []
  names = []
  areas = []
  addresses = []
  tels  = []
  hours = []
  genles = []
  HPs = []
  youtubes = []
  # その他定義
  ul_elements = []
  # エリア
  count = 0
  for num_list in num_lists:
    index = count
    count += 1
    num_li = num_lists[index]
    for i in range(num_li):
      areas.append(area_names[index])
  for i in range(len(area_names)):
    ul_element = browser.find_elements(By.XPATH,ul_xpaths[i])
    ul_elements.append(ul_element)
    p_elements = ul_element[0].find_elements(By.CLASS_NAME,'search-map__clinic-image--link')
    content_elements = ul_element[0].find_elements(By.CLASS_NAME,'search-map__clinic-content')
    btn_elements = ul_element[0].find_elements(By.CLASS_NAME,'search-map__clinic-site')
    num_cards = len(p_elements)
    for num_card in range(num_cards):
      # 写真URL
      image_element = p_elements[num_card].find_elements(By.CSS_SELECTOR,'img')
      image = image_element[0].get_attribute('src')
      images.append(image)
      # 施設名
      content_element = content_elements[num_card].find_elements(By.CLASS_NAME,'search-map__clinic-name')
      name = content_element[0].find_elements(By.CLASS_NAME,'search-map__clinic-link')[0].text
      names.append(name)
      # 住所
      address_element = content_elements[num_card].find_elements(By.CLASS_NAME,'search-map__clinic-address')
      address = address_element[0].text
      address = address.replace('\n',' ')
      addresses.append(address)
      # 電話番号
      tel_element = content_elements[num_card].find_elements(By.CLASS_NAME,'search-map__clinic-tel')[0].find_elements(By.CLASS_NAME,'pc-tab-show')
      tel = tel_element[0].text
      tels.append(tel)
      # 営業時間
      hour_element = content_elements[num_card].find_elements(By.CLASS_NAME,'search-map__clinic-time')
      hour = hour_element[0].text
      hours.append(hour)
      # 対応ジャンル
      genleUl_element = content_elements[num_card].find_elements(By.CSS_SELECTOR,'ul')
      genle_element = genleUl_element[0].find_elements(By.CSS_SELECTOR,'li')
      num_genle = len(genle_element)
      genles_pre = []
      for j in range(num_genle):
        genle = genle_element[0].text
        genles_pre.append(genle)
      str_genles_pre = str(genles_pre)
      str_genles_pre =  str_genles_pre.replace('[','').replace("'","").replace(']','').replace(',',' ')
      genles.append(str_genles_pre)
      # 公式サイト
      HP_element = btn_elements[num_card].find_elements(By.CSS_SELECTOR,'a')
      HP = HP_element[0].get_attribute('href')
      HPs.append(HP)
      # Youtube
      youtube_element = content_elements[num_card].find_elements(By.CLASS_NAME,'search-map__clinic-report')
      if len(youtube_element) == 0:
        youtube = 'none'
      else:
        youtube = youtube_element[0].find_elements(By.CSS_SELECTOR,'a')[0].get_attribute('href')
      youtubes.append(youtube)
  matrix.extend(np.transpose(np.array([images,names,areas,addresses,tels,hours,genles,HPs,youtubes])).tolist())
  return matrix
#getMatrix()

# csvに出力
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(getMatrix())