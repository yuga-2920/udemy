from selenium import webdriver
import pandas

browser = webdriver.Chrome()
browser.get("https://scraping-for-beginner.herokuapp.com/ranking/")

titles = []

#elems_rankingBox = browser.find_elements_by_class_name("u_areaListRankingBox")

"""
for elem_rankingBox in elems_rankingBox:
    elem_title = elem_rankingBox.find_element_by_class_name("u_title")
    title = elem_title.text.split("\n")[1]
    titles.append(title)
"""
#category_rank = elem_category.find_element_by_class_name("evaluateNumber")
for page in range(1,4): 
    browser.get("https://scraping-for-beginner.herokuapp.com/ranking/?page={}".format(page))
    ranking = []
    elems_category = browser.find_elements_by_class_name("u_categoryTipsItem")
    for elem_category in elems_category:
        elems_rank = elem_category.find_elements_by_class_name("is_rank")
        category = []
        for elem_rank in elems_rank:
            elem_rank = elem_category.find_element_by_class_name("evaluateNumber")
            rank = elem_rank.text
            category.append(float(rank))
        ranking.append(category)

    print(ranking)