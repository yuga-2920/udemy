from selenium import webdriver
from PIL import Image
import pandas as pd

browser=webdriver.Chrome()
browser.get('https://scraping-for-beginner.herokuapp.com/login_page')

elem_username = browser.find_element_by_id('username')
elem_username.send_keys('imanishi')

elem_password = browser.find_element_by_id('password')
elem_password.send_keys('kohei')

elem_login_btm = browser.find_element_by_id('login-btn')
elem_login_btm.click()

elems_th = browser.find_elements_by_tag_name("th")

keys = []

for elem_th in elems_th:
    key = elem_th.text
    keys.append(key)

elems_td =browser.find_elements_by_tag_name("td")
values = []

for elem_td in elems_td:
    value =elem_td.text
    values.append(value)

df = pd.DataFrame()
df["項目"] = keys
df["値"] = values

df.to_csv("講師情報.csv", index=False)