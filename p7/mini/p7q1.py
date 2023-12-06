import requests as req
from datetime import date, timedelta, datetime

def tabdilTarikh():
    saal = (input("saal: "))
    maah = (input("maah: "))
    rooz = (input("rooz: "))


    myQuery = f"https://api.ineo-team.ir/DateConvert.php?method=shamsi&day={rooz}&month={maah}&year={saal}"

    myreq = req.get(myQuery).json()

    print(myreq["result"]["convert"]["georgian"]["info"])
    print(myreq["result"]["convert"]["georgian"]["date"])

    print(myreq["result"]["convert"]["lunar"]["info"])
    print(myreq["result"]["convert"]["lunar"]["date"])



def tabdilSaat():
    saat = int(input("saat: "))
    daghighe = int(input("daghighe: "))
    # datetime.time(15, 8, 24, 78915)
    # tehran +3:30
    myQuery = f"{saat}:{daghighe}"
    myDate  = datetime.strptime(myQuery,"%H:%M")

    gmt = myDate - datetime.strptime("3:30","%H:%M")
    # paris +1:0
    print("paris: ")
    print(gmt+ datetime.strptime("1:00","%H:%M"))
    # zhohans... +2
    print("zhohansborg: ")
    print(gmt+ datetime.strptime("2:00","%H:%M"))
    # seol +9:0
    print("seol: ")
    print(gmt+ datetime.strptime("9:00","%H:%M"))








while(True):
    menuControl = input("1. tabdil taarikh\n2. saat haye jahan\n>> ")
    match menuControl:
        case "1":
            tabdilTarikh();
            break;
        case "2":
            tabdilSaat()
            break;
        case _:
            print("invalid choose")
            break;
