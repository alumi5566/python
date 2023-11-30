import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# res = requests.get('https://pala.tw/js-example/')
# print(res.text)
# input: title
# > 消失的文字
tag = input("Input element. add ',' before class; add '#' before id\n")
res = requests.get("https://pala.tw/js-example/")
soup = BeautifulSoup(res.text, 'lxml')

for drink in soup.select('{}'.format(tag)):
    print(drink.getText())
