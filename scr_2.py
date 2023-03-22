import pandas as pd
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定数の定義
csv_path = '/Users/sasakiaoto/Downloads/scraping_1/csv/data_2.csv'
btn_xpath = '/html/body/div[1]/div/div/main/div[3]/div[1]/div[5]/p[7]/a'
detail_xpath = '/html/body/div/div[1]/div/main/div/article'
url = 'https://chelation.jp/doctorlist/'
area_names = ['北海道','東北','関東','甲信越','東海','近畿','中国','四国','九州','沖縄']
num_lis = [4,2,37,8,10,8,6,0,13,2]


# XPATHの定義
area_xpaths = []
ul_xpaths   = []
areaName_xpaths = []
num_prefs = [1,1,5,4,4,4,3,0,6,1]
for i in range(10):
  area_xpath = f'/html/body/main/div[2]/article/div[{i+3}]'
  area_xpaths.append(area_xpath)
  areaName_xpath = f'{area_xpath}/h2'
  areaName_xpaths.append(areaName_xpath)
  num_pref = num_prefs[i]
  for pref in range(num_pref):
    ul_xpath = f'{area_xpath}/section[{pref+1}]/div/ul'
    ul_xpaths.append(ul_xpath)


# 1データのスクレイピング
browser = webdriver.Chrome()


def getMatrix():
  matrix = []
  names = []
  hrefs = []
  areas = []
  tels  = []
  mails = []
  browser.get(url)
  li_elements = []
  # エリア
  count = 0
  for num_pref in num_prefs:
    index = count
    count += 1
    num_li = num_lis[index]
    for i in range(num_li):
      areas.append(area_names[index])
  for ul_xpath in ul_xpaths:
    ul_element = browser.find_elements(By.XPATH,ul_xpath) # 各ulのelement
    li_elements = ul_element[0].find_elements(By.CSS_SELECTOR,'li') # 各liのelementが配列で格納されている
    for li_element in li_elements:
      # 施設名 and 公式サイトURL
      co_name = li_element.find_element(By.CLASS_NAME,'co-name')
      name = co_name.text
      href = co_name.find_elements(By.CSS_SELECTOR,'a')
      if len(href) == 0:
        href.append('none')
        href = href[0]
      else:
        href = href[0].get_attribute('href')
      names.append(name)
      hrefs.append(href)
      # 電話番号
      tel_element = li_element.find_element(By.CLASS_NAME,'tel-link')
      tel = tel_element.text
      if '-' in tel:
        tel = tel
      else:
        tel = 'none'
      tels.append(tel)
      # メールアドレス
      mail_element_pre = li_element.find_element(By.CLASS_NAME,'mail')
      mail_element = mail_element_pre.find_elements(By.CSS_SELECTOR,'a')
      if len(mail_element) == 0:
        mail_element.append('none')
        mail = mail_element[0]
      else:
        mail = mail_element[0].get_attribute('href')
      mail = mail.replace('mailto:','')
      mails.append(mail)
  
  matrix.extend(np.transpose(np.array([names,areas,tels,mails,hrefs])).tolist())
  return matrix
#getMatrix()

# csvに出力
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(getMatrix())