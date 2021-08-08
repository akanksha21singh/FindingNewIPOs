import requests 
from bs4 import BeautifulSoup
from datetime import datetime
from tkinter import *

#fetching the website
url='https://www.chittorgarh.com/report/mainboard-ipo-list-in-india-bse-nse/83/'

req = requests.get(url)
content = BeautifulSoup(req.content,"html5lib")

new=[]
tbodyVal = content.find("tbody")

#code to get new ipos list
for i in tbodyVal.find_all("tr"):
    l = []
    cols = i.find_all("td")
    l.append(cols[0].text)
    l.append(cols[2].text)
    d=cols[2].text
    try:
        if datetime.strptime(d,'%b %d, %Y')>datetime.now():
            new.append(l)
    except:
        pass

#GUI implementation. 
window = Tk()
window.geometry('450x120')
for i in new:
    label = Label(window, text= i[0]+' , '+i[1])
    label.pack()     

window.mainloop()

    