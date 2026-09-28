import os,zipfile,requests
URL='https://archive.ics.uci.edu/static/public/222/bank+marketing.zip'
os.makedirs('data/raw',exist_ok=True)
r=requests.get(URL,timeout=60); r.raise_for_status(); open('data/raw/bank.zip','wb').write(r.content)
with zipfile.ZipFile('data/raw/bank.zip') as z:z.extractall('data/raw')
print('Downloaded UCI Bank Marketing dataset.')