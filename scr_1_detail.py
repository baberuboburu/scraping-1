import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# 定数の定義
prefectures_kanji = ['北海道', '青森県', '岩手県', '宮城県', '秋田県', '山形県', '福島県', '茨城県', '栃木県', '群馬県', '埼玉県', '千葉県', '東京都', '神奈川県', '新潟県', '富山県', '石川県', '福井県', '山梨県', '長野県', '岐阜県', '静岡県', '愛知県', '三重県', '滋賀県', '京都府', '大阪府', '兵庫県', '奈良県', '和歌山県', '鳥取県', '島根県', '岡山県', '広島県', '山口県', '徳島県', '香川県', '愛媛県', '高知県', '福岡県', '佐賀県', '長崎県', '熊本県', '大分県', '宮崎県', '鹿児島県', '沖縄県']
prefectures_roman = ['hokkaido', 'aomori', 'iwate', 'miyagi', 'akita', 'yamagata', 'fukushima', 'ibaraki', 'tochigi', 'gunma', 'saitama', 'chiba', 'tokyo', 'kanagawa', 'niigata', 'toyama', 'ishikawa', 'fukui', 'yamanashi', 'nagano', 'gifu', 'shizuoka', 'aichi', 'mie', 'shiga', 'kyoto', 'osaka', 'hyogo', 'nara', 'wakayama', 'tottori', 'shimane', 'okayama', 'hiroshima', 'yamaguchi', 'tokushima', 'kagawa', 'ehime', 'kochi', 'fukuoka', 'saga', 'nagasaki', 'kumamoto', 'oita', 'miyazaki', 'kagoshima', 'okinawa']


# 1データのスクレイピング
browser = webdriver.Chrome()


features = []
words_1 = []
words_2 = []
words_3 = []
infusions = []
HPs = []
names = []
for prefecture in prefectures_roman:
  matrix = []
  csv_path = f'/Users/sasakiaoto/Downloads/scraping_1/csv/data_1/data_{prefecture}.csv'
  url = f'https://www.iv-therapy.org/clinic/?area={prefecture}&flag_specification%5B%5D=%E9%AB%98%E6%BF%83%E5%BA%A6%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3%EF%BC%A3%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95%EF%BC%88%E3%81%8C%E3%82%93%E6%B2%BB%E7%99%82%EF%BC%89&flag_specification%5B%5D=%E9%AB%98%E6%BF%83%E5%BA%A6%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3%EF%BC%A3%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95%EF%BC%88%E3%82%A2%E3%83%B3%E3%83%81%E3%82%A8%E3%82%A4%E3%82%B8%E3%83%B3%E3%82%B0%EF%BC%89&flag_specification%5B%5D=%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%AA%E3%83%9D%E9%85%B8%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E3%83%9E%E3%82%A4%E3%83%A4%E3%83%BC%E3%82%BA%E3%82%AB%E3%82%AF%E3%83%86%E3%83%AB%EF%BC%88%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3%E3%83%BB%E3%83%9F%E3%83%8D%E3%83%A9%E3%83%AB%E7%82%B9%E6%BB%B4%EF%BC%89&flag_specification%5B%5D=%E3%82%B0%E3%83%AB%E3%82%BF%E3%83%81%E3%82%AA%E3%83%B3%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E3%82%AD%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E7%99%82%E6%B3%95%28Ca-EDTA%29&flag_specification%5B%5D=%E3%82%AD%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E7%99%82%E6%B3%95%28Na-EDTA%29&flag_specification%5B%5D=%E3%83%97%E3%83%A9%E3%82%BB%E3%83%B3%E3%82%BF%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E8%A1%80%E6%B6%B2%E3%82%AA%E3%82%BE%E3%83%B3%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E5%B9%B9%E7%B4%B0%E8%83%9E%E5%9F%B9%E9%A4%8A%E4%B8%8A%E6%B8%85%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E3%82%AA%E3%83%BC%E3%82%BD%E3%83%A2%E3%83%AC%E3%82%AD%E3%83%A5%E3%83%A9%E3%83%BC%E6%A0%84%E9%A4%8A%E7%99%82%E6%B3%95&s='
  #url = f'https://www.iv-therapy.org/clinic/?area=tokyo&flag_specification%5B%5D=%E9%AB%98%E6%BF%83%E5%BA%A6%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3%EF%BC%A3%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95%EF%BC%88%E3%81%8C%E3%82%93%E6%B2%BB%E7%99%82%EF%BC%89&flag_specification%5B%5D=%E9%AB%98%E6%BF%83%E5%BA%A6%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3%EF%BC%A3%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95%EF%BC%88%E3%82%A2%E3%83%B3%E3%83%81%E3%82%A8%E3%82%A4%E3%82%B8%E3%83%B3%E3%82%B0%EF%BC%89&flag_specification%5B%5D=%E3%82%A2%E3%83%AB%E3%83%95%E3%82%A1%E3%83%AA%E3%83%9D%E9%85%B8%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E3%83%9E%E3%82%A4%E3%83%A4%E3%83%BC%E3%82%BA%E3%82%AB%E3%82%AF%E3%83%86%E3%83%AB%EF%BC%88%E3%83%93%E3%82%BF%E3%83%9F%E3%83%B3%E3%83%BB%E3%83%9F%E3%83%8D%E3%83%A9%E3%83%AB%E7%82%B9%E6%BB%B4%EF%BC%89&flag_specification%5B%5D=%E3%82%B0%E3%83%AB%E3%82%BF%E3%83%81%E3%82%AA%E3%83%B3%E7%82%B9%E6%BB%B4%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E3%82%AD%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E7%99%82%E6%B3%95%28Ca-EDTA%29&flag_specification%5B%5D=%E3%82%AD%E3%83%AC%E3%83%BC%E3%82%B7%E3%83%A7%E3%83%B3%E7%99%82%E6%B3%95%28Na-EDTA%29&flag_specification%5B%5D=%E3%83%97%E3%83%A9%E3%82%BB%E3%83%B3%E3%82%BF%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E8%A1%80%E6%B6%B2%E3%82%AA%E3%82%BE%E3%83%B3%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E5%B9%B9%E7%B4%B0%E8%83%9E%E5%9F%B9%E9%A4%8A%E4%B8%8A%E6%B8%85%E7%99%82%E6%B3%95&flag_specification%5B%5D=%E3%82%AA%E3%83%BC%E3%82%BD%E3%83%A2%E3%83%AC%E3%82%AD%E3%83%A5%E3%83%A9%E3%83%BC%E6%A0%84%E9%A4%8A%E7%99%82%E6%B3%95&s='
  browser.get(url)
  pickupClinic_elements = browser.find_elements(By.CLASS_NAME,'pickup-clinic')
  num_pickups = len(pickupClinic_elements)
  print(num_pickups)
  if num_pickups == 0:
    continue
  for i in range(num_pickups):
    piupInfo_element = pickupClinic_elements[i].find_elements(By.CLASS_NAME,'clinic-info')
    click_element = piupInfo_element[0].find_elements(By.CSS_SELECTOR,'a')
    # ハンドル
    newURL  = click_element[0].get_attribute('href')
    browser.execute_script("window.open('https://www.google.com','new_window')")
    handles = browser.window_handles
    browser.switch_to.window(handles[1])
    browser.get(newURL)
    # クリニック特徴
    feature_element = browser.find_elements(By.ID,'feature')
    featureText_element = feature_element[0].find_elements(By.XPATH,'div/div[1]')
    featureText = featureText_element[0].text
    features.append(featureText)
     # 点滴療法
    therapy_element = browser.find_elements(By.ID,'therapy')
    ul_element = therapy_element[0].find_elements(By.CSS_SELECTOR,'ul')
    li_elements = ul_element[0].find_elements(By.CSS_SELECTOR,'li')
    num_lis = len(li_elements)
    infusions_pre = []
    for j in range(num_lis):
      li_text = li_elements[j].text
      infusions_pre.append(li_text)
    infusion = ",".join(infusions_pre)
    infusions.append(infusion)
    # 医師からの一言
    interview_element = browser.find_elements(By.ID,'interview')
    for j in range(3):
      interviewText_element = interview_element[0].find_elements(By.XPATH,f'div[{j+2}]')
      interviewText = interviewText_element[0].text
      if j == 0:
        words_1.append(interviewText)
      elif j == 1:
        words_2.append(interviewText)
      elif j == 2:
        words_3.append(interviewText)
    # 責任者と公式サイト
    info_element = browser.find_elements(By.ID,'info')
    HP_element = info_element[0].find_elements(By.XPATH,'div/div[2]/table/tbody/tr[6]/td/a')
    if len(HP_element) == 0:
      HP = 'none'
    else:
      HP = HP_element[0].text
    HPs.append(HP)
    name_element = info_element[0].find_elements(By.XPATH,'div/div[2]/table/tbody/tr[3]/td')
    name = name_element[0].text
    name = name.replace('院長','')
    names.append(name)
    browser.close()
    browser.switch_to.window(handles[0])

  matrix.extend(np.transpose(np.array([features,words_1,words_2,words_3,infusions,HPs,names])).tolist())

  # csvに出力
  with open(csv_path, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerows(matrix)