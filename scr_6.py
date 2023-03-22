import numpy as np
import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# 定数の定義
num_continue = 1
#num_continue = 27 # 34までやり直し
#num_continue = 35
#num_continue = 133
#num_continue = 503


# XPATHの定義
h2_xpaths = []
tbody_xpaths = []
for i in range(10):
  h2_xpath = f'/html/body/div[1]/div/main/div[3]/div/div/h2[{i+1}]'
  h2_xpaths.append(h2_xpath)
  tbody_xpath = f'/html/body/div[1]/div/main/div[3]/div/div/table[{i+1}]/tbody'
  tbody_xpaths.append(tbody_xpath)


# 1データのスクレイピング
browser = webdriver.Chrome()


clinics = []
addresses = []
prefectures = []
names = []
others1 = []
others2 = []
parts = []
methods = []
dots = []
for i in range(34-num_continue+1): #503
  matrix = []
  page = i*10 + (num_continue-1)*10
  csv_path = f'/Users/sasakiaoto/Downloads/scraping_1/csv/data_6/data_{i+num_continue}.csv'
  url = f'https://saiseiiryo.jp/search/?offset={page}&limit=10&agencyAll0=on&agencyAll1=on&prefecture=%E5%8C%97%E6%B5%B7%E9%81%93&agencyAll2=on&prefecture=%E9%9D%92%E6%A3%AE%E7%9C%8C&prefecture=%E7%A7%8B%E7%94%B0%E7%9C%8C&prefecture=%E5%B2%A9%E6%89%8B%E7%9C%8C&prefecture=%E5%B1%B1%E5%BD%A2%E7%9C%8C&prefecture=%E5%AE%AE%E5%9F%8E%E7%9C%8C&prefecture=%E7%A6%8F%E5%B3%B6%E7%9C%8C&agencyAll3=on&prefecture=%E7%BE%A4%E9%A6%AC%E7%9C%8C&prefecture=%E6%A0%83%E6%9C%A8%E7%9C%8C&prefecture=%E8%8C%A8%E5%9F%8E%E7%9C%8C&prefecture=%E5%9F%BC%E7%8E%89%E7%9C%8C&prefecture=%E6%9D%B1%E4%BA%AC%E9%83%BD&prefecture=%E7%A5%9E%E5%A5%88%E5%B7%9D%E7%9C%8C&prefecture=%E5%8D%83%E8%91%89%E7%9C%8C&prefecture=%E6%96%B0%E6%BD%9F%E7%9C%8C&prefecture=%E9%95%B7%E9%87%8E%E7%9C%8C&prefecture=%E5%B1%B1%E6%A2%A8%E7%9C%8C&agencyAll4=on&prefecture=%E7%9F%B3%E5%B7%9D%E7%9C%8C&prefecture=%E5%AF%8C%E5%B1%B1%E7%9C%8C&prefecture=%E5%B2%90%E9%98%9C%E7%9C%8C&prefecture=%E4%B8%89%E9%87%8D%E7%9C%8C&prefecture=%E6%84%9B%E7%9F%A5%E7%9C%8C&prefecture=%E9%9D%99%E5%B2%A1%E7%9C%8C&agencyAll5=on&prefecture=%E5%85%B5%E5%BA%AB%E7%9C%8C&prefecture=%E4%BA%AC%E9%83%BD%E5%BA%9C&prefecture=%E6%BB%8B%E8%B3%80%E7%9C%8C&prefecture=%E7%A6%8F%E4%BA%95%E7%9C%8C&prefecture=%E5%A4%A7%E9%98%AA%E5%BA%9C&prefecture=%E5%A5%88%E8%89%AF%E7%9C%8C&prefecture=%E5%92%8C%E6%AD%8C%E5%B1%B1%E7%9C%8C&agencyAll6=on&prefecture=%E5%B1%B1%E5%8F%A3%E7%9C%8C&prefecture=%E5%B3%B6%E6%A0%B9%E7%9C%8C&prefecture=%E9%B3%A5%E5%8F%96%E7%9C%8C&prefecture=%E5%BA%83%E5%B3%B6%E7%9C%8C&prefecture=%E5%B2%A1%E5%B1%B1%E7%9C%8C&prefecture=%E6%84%9B%E5%AA%9B%E7%9C%8C&prefecture=%E9%A6%99%E5%B7%9D%E7%9C%8C&prefecture=%E5%BE%B3%E5%B3%B6%E7%9C%8C&prefecture=%E9%AB%98%E7%9F%A5%E7%9C%8C&agencyAll7=on&prefecture=%E9%95%B7%E5%B4%8E%E7%9C%8C&prefecture=%E4%BD%90%E8%B3%80%E7%9C%8C&prefecture=%E7%A6%8F%E5%B2%A1%E7%9C%8C&prefecture=%E7%86%8A%E6%9C%AC%E7%9C%8C&prefecture=%E5%A4%A7%E5%88%86%E7%9C%8C&prefecture=%E5%AE%AE%E5%B4%8E%E7%9C%8C&prefecture=%E9%B9%BF%E5%85%90%E5%B3%B6%E7%9C%8C&prefecture=%E6%B2%96%E7%B8%84%E7%9C%8C&treatment=&target=&search=&division=%E6%B2%BB%E7%99%82'
  browser.get(url)
  time.sleep(7)
  for j in range(10):
    # elementの取得
    h2_element = browser.find_elements(By.XPATH,h2_xpaths[j])
    if len(h2_element) == 0:
      h2_element.append('none')
      h2 = h2_element[0]
    else:
      h2 = h2_element[0].text
    tbody_element = browser.find_elements(By.XPATH,tbody_xpaths[j])
    tr_elements = tbody_element[0].find_elements(By.CSS_SELECTOR,'tr')
    num_tr = len(tr_elements)
    # h2
    clinic = h2
    clinics.append(clinic)
    # table/tbody
    if num_tr != 8:
      print(f'{i+1}ページ目のj番目のtable : trの数{num_tr}')
    for j in range(num_tr):
      th_element = tr_elements[j].find_elements(By.CSS_SELECTOR,'th')
      th = th_element[0].text
      td_element = tr_elements[j].find_elements(By.CSS_SELECTOR,'td')
      td = td_element[0].text
      if '都道府県' in th:
        addresses.append(td)
        prefecture = str(td[0:3])
        prefectures.append(prefecture)
        continue
      elif '管理者' in th:
        names.append(td)
        continue
      elif '再生医療等の名称' in th:
        others1.append(td)
        continue
      elif '認定再生医療等委員会' in th:
        others2.append(td)
        continue
      elif '部位' in th:
        parts.append(td)
        continue
      elif '治療法' in th:
        methods.append(td)
        continue
      elif '治療・研究の区分' in th:
        dots.append(td)
        continue
  matrix.extend(np.transpose(np.array([clinics,addresses,prefectures,names,others1,others2,parts,methods,dots])).tolist())

  with open(csv_path, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(matrix)