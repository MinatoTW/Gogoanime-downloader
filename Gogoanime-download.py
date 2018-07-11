import requests
from pySmartDL import SmartDL
import sys
import os
from clint.textui import progress
from bs4 import BeautifulSoup
def download(url,dest):
    obj=SmartDL(url, dest)
    obj.start()
    return
u=raw_input("Enter URL of first episode> " )
url=u[:-1]
try:
    rq=requests.get(url)
    if rq.status_code == 200:
        f=raw_input("Enter episode to start with> ")
        l=raw_input("Enter episode to end with> ")
        n=raw_input("Enter name to be saved as> ")
        d=raw_input("Enter full path to destination folder")
        s=raw_input("Switch off when downloaded?(y/n) ")
except:
    print "Wrong URL dude"
    sys.exit()
for i in range(int(f),int(l)+1):
    u=url+str(i)
    r=requests.get(u)
    soup=BeautifulSoup(r.text,'html.parser')
    links=soup.find_all(target='_blank')
    for link in links:
        l=link.get('href')
        if 'download' in l:
            r1=requests.get(l)
            s1=BeautifulSoup(r1.text,'html.parser')
            l1=s1.find_all('a')
            for l2 in l1:
                l3=l2.get('href')
                if 'fbcdn' in l3:
                    print(l3)
                    des=d+'/'+n+str(i)+'.mp4'
                    print des
                    download(l3,des)
if s == "y":
    if os.name == 'nt':
        os.system("shutdown /s")
    else:
        os.system("poweroff")
