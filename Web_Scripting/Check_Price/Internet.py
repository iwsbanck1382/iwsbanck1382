import requests
from bs4 import BeautifulSoup
import os
import time

def to_int(string):
    s=""
    for i in string:
        if(ord(i) >=1776)and(ord(i)<=1785):
            result=chr(ord(i)-1728)
            s=s+result
    return(s)
def price(name):
    List=[]
    url="https://www.digikala.com/search/?q="+name+"&sortby=21"
    try:
        web=requests.get(url)
    except:
        raise ConnectionError("Please check your internet and try again!")
        return 0
    text=web.text
    soup=BeautifulSoup(text,"html.parser")
    divs=soup.find_all("div")
    for price in divs:
        Class=(price.get('class'))
        if (Class !=None):
            if "c-price__value-wrapper" in Class:
                #print(price.get_text())
                List.append(int(to_int(price.get_text())))
        else:
            continue
    List.sort()
    result="minimum : {} - maximum : {}".format(List[1],List[-1])
    return(result)
if __name__=='__main__':
    all_price=(price("mobile"))
    print(all_price)
    print(timing()) 
    #print(to_int("۰"))

def search_wiki(name):
    p=""
    url1="https://www.google.com/search?safe=active&rlz=1C1SQJL_enIR901IR901&ei=qlcTX53VNqeAjLsP6o-g4A4&q="
    url2="&oq=water+and+ice&gs_lcp=CgZwc3ktYWIQAzICCAAyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BAgAEEM6AgguOgUILhCTAjoECAAQClDzSFjmZmCVbWgCcAB4AIABkQKIAYMQkgEDMi04mAEAoAEBqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwid0s2jztfqAhUnAGMBHeoHCOwQ4dUDCAw&uact=5"
    for i in name:
        if(name ==" "):
            p=p+"+"
        else:
            p=p+i
    print("start "+url1+p+url2)
    os.system("start "+url1+p+url2)



def timing():
    now = time.localtime()
    result=str(now.tm_hour)+" : "+str(now.tm_min)
    return(result)

   
