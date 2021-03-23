import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from random import randint

link = 'https://auto.naver.com/car/mainList.nhn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

data = requests.get(link, headers=headers)
soup = BeautifulSoup(data.text, 'html.parser')
Total = soup.select('content > div.model_group_new > ul > li')
print(Total)
# content > div.model_group_new > ul > li:nth-child(1)
# content > div.model_group_new > ul > li:nth-child(1) > div > div > a.model_name > span > strong
