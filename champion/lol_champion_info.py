
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from champion.champion_info import champion_info_from

browser = webdriver.PhantomJS()
browser.implicitly_wait(5)
browser.get('https://lol.garena.tw/game/champion')
content = browser.page_source
browser.quit()

soup_content = BeautifulSoup(content , 'lxml')
urls = soup_content.find_all('a' , class_ = 'champlist-item__link')

for url in urls:
    champion_info_from('https://lol.garena.tw' + url['href'])

print("Update is finished.")
