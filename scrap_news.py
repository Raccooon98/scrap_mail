from bs4 import BeautifulSoup
import requests
import json
import re

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

url = "http://rscanner.ndmi.go.kr/scanning/policy_news_weekly.php"

response = requests.get(url, headers=header)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')


script_tags = soup.find_all('script')
data_script = None

for script in script_tags:
    try:
        if 'var dataSet = [' in script.string:
            data_script = script
            break
    except:
        pass


if data_script:
    match = re.search(r'var dataSet = (\[.*?\]);', data_script.text)
    
    if match:
        data_text = match.group(1)
        data_set = json.loads(data_text)
        print(data_set)
    else:
        print("Data not found in script.")
else:
    print("Data script not found in the page.")