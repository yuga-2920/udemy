from selenium import webdriver
from PIL import Image
import io
from urllib import request

browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/image")

elems = browser.find_elements_by_class_name("material-placeholder")

for index,elem in enumerate(elems):

    elem = elem.find_element_by_tag_name("img")
    url = elem.get_attribute('src')
    f = io.BytesIO(request.urlopen(url).read())
    img =Image.open(f)
    img.save("udemy/PythonによるWebスクレイピング〜入門編〜【業務効率化への第一歩】/image/{}.jpg".format(index))