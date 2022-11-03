import urllib.request 
from bs4 import BeautifulSoup

# providing url
s=str(input("Enter the rule"))
url="http://127.0.0.1:5501/samples_all_rules/{}.html".format(s)
#url ="http://127.0.0.1:5500/body_1_3_1.html"
print(url)
# opening the url for reading
html = urllib.request.urlopen(url)
soup=BeautifulSoup(html, 'html.parser')
content=soup.find('div',id="1.3.1")
print(content)
url1="https://samples.d30cdmax87qbqr.amplifyapp.com/"
html1=urllib.request.urlopen(url1)
soup1=BeautifulSoup(html1,'html.parser')
if content in soup1:
    print("already there")
else:
    if 'head' in s:
     soup1.head.append(content)
    else:
     soup1.body.append(content)
savechanges = soup1.prettify("utf-8")
with open("index.html", "wb") as file:
    file.write(savechanges)