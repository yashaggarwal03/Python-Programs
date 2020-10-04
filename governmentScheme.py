
from bs4 import BeautifulSoup
import lxml
import urllib.request
import re
from gtts import gTTS
from playsound import playsound
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
url = r"https://wbxpress.com/schemes/"
res = urllib.request.urlopen(url).read()
res = res.decode("utf-8")
soup = BeautifulSoup(res,features="lxml")
a=[]
b=[]
soup = soup.find("div",{"class":"entry-content"})
for h in soup.findAll(re.compile("h3")):
    a.append(h.text.strip())
for p in soup.findAll(re.compile("p")):
    b.append(p.text.strip())
b=(b[1:])
d={}
for i in range(0,len(a)):
    #print(a[i])
    d[a[i]]=b[i]
    #print("\n",b[i])
    #print()
soupPara = soup.find_all(re.compile("p"))
#print(soupPara)
j = json.dumps(d)
print(j)
with open("db.json","w",encoding="utf-8") as f:
    json.dump(j,f,ensure_ascii=False,indent=4)
#print("Hello World")
