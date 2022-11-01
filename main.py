import requests
import sys
from bs4 import BeautifulSoup
import wget

def findAndGet(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    elements = soup.find_all('a')

    for element in elements:
        try:
            wget.download(url+"/"+element['href'], "read/"+element['href'])
        except:
            pass
        if(element['href'][-1] == '/'):
            findAndGet(url+element['href'])    

findAndGet(sys.argv[1])

