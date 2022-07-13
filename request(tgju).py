import struct
import requests
import ctypes
from datetime import datetime

def Mbox(title, text, style):
    ##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel 
##  6 : Cancel | Try Again | Continue
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
#Mbox('Your title', 'Your text', 1)


nameticket= " "
urlticket = " "

x =  int(input('0=Gold_18 1=Gold_24 2=dollar 3=custom  ? Enter') or "2")

if (x==3):
    nameticket= input('Name : ?')
    urlticket = str(input('URL history : ?'))
 
if (x==2):
    nameticket= input('Name : ?')
    urlticket = input('URL history : ?')
 
if (x==1):
    nameticket= "GOLD_24_GOLD"
    urlticket = "https://platform.tgju.org/fa/tvdata/history?symbol=GERAM24&resolution=1D&from=0&to=2240275019"
 
if (x==0):
    nameticket= "GOLD_18_GOLD"
    urlticket = "https://platform.tgju.org/fa/tvdata/history?symbol=GERAM18&resolution=1D&from=0&to=2240275019"
 




# اطلاعات قیمتی نماد ها

#_____ رکویست دادن
res = requests.get(urlticket)

#   با دستور ترای بررسی می کنم که رسپانس 200 داده و نت مشکلی مداشته باشه
#if res = 200 : true


#سکشن های مختلف را جدا می کنیم ----
res=res.text
res=res.replace('{"' , '')
res=res.replace('"s":"ok"}' , '')
res=res.replace('"' , '')
res=res.replace(':[' , ',')
res=res.replace('],' , ';')


res=res.split(";")

#____ سطر و ستون بندی دیتا
rows, cols = (len(res)+1, len(res[0].split(',')))

arr = [[0]*cols]*rows
for i in range(len(res)):
      arr[i] = (res[i].split(','))

for i in range(len(arr[0])):
    if(i>0):
        timestamp = arr[0][i]
        dt_obj = datetime.fromtimestamp(int(timestamp)).strftime('%Y%m%d')
        arr[0][i]=int(dt_obj)

textmake=""
for i in range(len(arr[0])):
    if not i in arr[5]:
        arr[5].append(0)

    textmake =textmake + nameticket +','+ str(arr[0][i]) +','+ str(arr[2][i]) +','+ str(arr[3][i]) +','+ str(arr[4][i]) +','+ str(arr[1][i]) +','+ str(arr[5][i])+ "\n"


with open( nameticket +".CSV" , "w") as p:
    p.write(str(textmake))



# پایان دیتای قیمت