import pandas as pd
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定数の定義
num = 16
csv_path = f'/Users/sasakiaoto/Downloads/scraping_1/csv/data_5/data_5_{num}.csv'


# XPATHの定義
list_xpath = '/html/body/div[1]/div[1]/main/div/div[1]'


# 1データのスクレイピング
browser = webdriver.Chrome()


def getMatrix():
  matrix = []
  names   = []
  titles  = []
  imgs    = []
  Hnames  = []
  newURLs = []
  HPs     = []
  tels    = []
  genders = []
  bloods = []
  universities = []
  kinds = []
  majors = []
  for i in range(1): #16
    url = f'https://www.hospita.jp/doctor/search?page={num}&specialist=79'
    browser.get(url)
    for j in range(20):#20
      # XPATHの定義
      if j<10:
        card_xpath = f'{list_xpath}/div[{j+4}]'
      else:
        card_xpath = f'{list_xpath}/div[{j+5}]'
      person_xpath   = f'{card_xpath}/div[1]/div[1]/div'
      hospital_xpath = f'{card_xpath}/div[2]'
      name_xpath     = f'{person_xpath}/div[1]/h1/a'
      title_xpath    = f'{person_xpath}/div[1]/div[1]'
      img_xpath      = f'{person_xpath}/div[2]/div/a/img'
      Hname_xpath    = f'{hospital_xpath}/div[1]/a'
      tel_xpath      = f'{hospital_xpath}/div[3]'
      # 要素の取得
      name    = browser.find_elements(By.XPATH,name_xpath)[0].text
      title   = browser.find_elements(By.XPATH,title_xpath)[0].text
      img     = browser.find_elements(By.XPATH,img_xpath)[0].get_attribute('src')
      Hname   = browser.find_elements(By.XPATH,Hname_xpath)[0].text
      newURL  = browser.find_elements(By.XPATH,Hname_xpath)[0].get_attribute('href')
      tel     = browser.find_elements(By.XPATH,tel_xpath)[0].text
      # その他要素の取得
      others = browser.find_elements(By.XPATH,f'{person_xpath}/div[1]')[0].find_elements(By.CLASS_NAME,'mt-3')
      item_elements = others[0].find_elements(By.CLASS_NAME,'badge')
      genders_pre = []
      bloods_pre = []
      universities_pre = []
      kinds_pre = []
      for k in range(len(item_elements)):
        item = item_elements[k].text
        if len(kinds_pre) == 0:
          kinds_pre.append('none')
        if len(genders_pre) == 0:
          genders_pre.append('none')
        if len(bloods_pre) == 0:
          bloods_pre.append('none')
        if len(universities_pre) == 0:
          universities_pre.append('none')
        if '男性' in item or '女性' in item:
          if genders_pre[-1] == 'none':
            genders_pre[-1] = item
          else:
            genders_pre.append(item)
        elif 'A型' in item or 'B型' in item or 'O型' in item or 'AB型' in item:
          if bloods_pre[-1] == 'none':
            bloods_pre[-1] = item
          else:
            bloods_pre.append(item)
        elif '大学' in item:
          if universities_pre[-1] == 'none':
            universities_pre[-1] = item
          else:
            universities_pre.append(item)
        elif '専門医' in item:
          if kinds_pre[-1] == 'none':
            kinds_pre[-1] = item
          else:
            kinds_pre.append(item)
      gender = ','.join(genders_pre)
      blood = ','.join(bloods_pre)
      university = ','.join(universities_pre)
      kind = ','.join(kinds_pre)
      # ハンドル
      browser.execute_script("window.open('https://www.google.com','new_window')")
      handles = browser.window_handles
      browser.switch_to.window(handles[1])
      browser.get(newURL)
      table_elements = browser.find_elements(By.CLASS_NAME,'table')
      if len(table_elements) == 1:
        HP_elements = table_elements[0].find_elements(By.CSS_SELECTOR,'a')
      elif len(table_elements) == 2:
        HP_elements = table_elements[1].find_elements(By.CSS_SELECTOR,'a')
      HP = 'none'
      for l in range(len(HP_elements)):
        if 'http' in HP_elements[l].text:
          HP = HP_elements[l].text
          break
      print(HP)
      browser.close()
      browser.switch_to.window(handles[0])
      # 配列への格納
      names.append(name)
      titles.append(title)
      imgs.append(img)
      Hnames.append(Hname)
      newURLs.append(newURL)
      HPs.append(HP)
      tels.append(tel)
      kinds.append(kind)
      genders.append(gender)
      bloods.append(blood)
      universities.append(university)
  matrix.extend(np.transpose(np.array([names,titles,imgs,Hnames,HPs,tels,genders,bloods,universities,kinds])).tolist())
  return matrix
#print(getMatrix())

# csvに出力
with open(csv_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(getMatrix())