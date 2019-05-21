import requests
from bs4 import BeautifulSoup
import json
import os

dir=os.path.dirname(os.path.abspath(__file__))
##path that the result file will be stored

req=requests.get('https://www.naver.com/')
##get sourse

html=req.text
header=req.headers
status=req.status_code
boolen=req.ok
##take information from http

soup=BeautifulSoup(html,'html.parser')
##html to python

condition_tag=soup.select(
    '#PM_ID_themelist > ul > li > a'
    )
##tag condition(will be more)

data={}

for i in condition_tag:
    data[i.text] = i.get('href')
##the location where the tags with filter conditions are to be stored

with open(os.path.join(dir, 'result.json'), 'w+') as json_file:
    json.dump(data, json_file)
##save to result file at dir
