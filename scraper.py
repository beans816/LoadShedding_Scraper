#Importrequired libraries
import requests
from bs4 import BeautifulSoup

url = "https://loadshedding.eskom.co.za/"
req = requests.get(url)
status = BeautifulSoup(req.text, "html.parser")


loadshedStage = status.find("span", class_= "loadshedStageTitle").text
lsstatus = status.find("span" , attrs={"id": "lsstatus"}).text

#determine status
if lsstatus == " not Load Shedding":
    lsLVL = "0"
elif lsstatus == " Level 1":
    lsLVL = "1"
elif lsstatus == " Level 2":
    lsLVL = "2"
elif lsstatus == " Level 3":
    lsLVL = "3"
elif lsstatus == " Level 4":
    lsLVL = "4"
elif lsstatus == " Level 5":
    lsLVL = "5"
elif lsstatus == " Level 6":
    lsLVL = "6"

print(loadshedStage)
print(lsLVL)