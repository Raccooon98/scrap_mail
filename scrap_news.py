from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
url= "http://rscanner.ndmi.go.kr/scanning/negative_news_weekly.php"

response= requests.get(url,headers=header).content
response = response.decode('utf-8')
soup = BeautifulSoup(response,'html.parser')


print(soup)