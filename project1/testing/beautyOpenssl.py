import requests
from bs4 import BeautifulSoup

def update():	
    httpdURL='https://www.openssl.org/'
    resp=requests.get(httpdURL)
    if resp.status_code==200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")
        
        soup=BeautifulSoup(resp.text,'html.parser')        
        l=soup.find("table",{"class":"newsflash"})
        # print(l)
        m = l.findAll("tr")[4]
        print(m.text)           
    else:
        print('Error: %s' % resp.status_code)   
        

		
update()
