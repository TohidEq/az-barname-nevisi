from datetime import datetime, timedelta

hazineOtaghBase = {
  "1T":890,
  "2T":1620,
  "3T":2100,
  "0T":3720 #VIP
}

# rooms>takht>roomId>(res?, userIds>userId)
rooms = {
  "1T":{
    "1":{
      "res":True,
      "userIds":["2581510900"] #code e melli
    },
    "2":{
      "res":False,
      "userIds":[]
    },
    "3":{
      "res":False,
      "userIds":[]
    },
    "4":{
      "res":False,
      "userIds":[]
    },
    "5":{
      "res":False,
      "userIds":[]
    }
  },
  "2T":{
    "1":{
      "res":False,
      "userIds":[""]
    },
    "2":{
      "res":False,
      "userIds":[""]
    },
    "3":{
      "res":False,
      "userIds":[""]
    },
    "4":{
      "res":False,
      "userIds":[""]
    },
    "5":{
      "res":False,
      "userIds":[""]
    },
    "6":{
      "res":False,
      "userIds":[""]
    },
    "7":{
      "res":False,
      "userIds":[""]
    },
    "8":{
      "res":False,
      "userIds":[""]
    },
    "9":{
      "res":False,
      "userIds":[""]
    },
    "10":{
      "res":False,
      "userIds":[""]
    },
    "11":{
      "res":False,
      "userIds":[""]
    },
    "12":{
      "res":False,
      "userIds":[""]
    },
    "13":{
      "res":False,
      "userIds":[""]
    },
    "14":{
      "res":False,
      "userIds":[""]
    },
    "15":{
      "res":False,
      "userIds":[""]
    },
    "16":{
      "res":False,
      "userIds":[""]
    },
  },
  "3T":{
    "1":{
      "res":False,
      "userIds":[""]
    },
    "2":{
      "res":False,
      "userIds":[""]
    },
    "3":{
      "res":False,
      "userIds":[""]
    },
    "4":{
      "res":False,
      "userIds":[""]
    },
    "5":{
      "res":False,
      "userIds":[""]
    },
    "6":{
      "res":False,
      "userIds":[""]
    },
    "7":{
      "res":False,
      "userIds":[""]
    },
    "8":{
      "res":False,
      "userIds":[""]
    },
  },
  "0T":{
    "1":{
      "res":False,
      "userIds":[""]
    },
    "2":{
      "res":False,
      "userIds":[""]
    },
  }
}

# users>takht>roomId>userId>(firstName, lastName, phone, taahol, otaghId, start, finish, hazine(0 = mehman, * = mizban(kasi ke pardakht mikonad)))
users = {
  "1T":{
    #user id as Key in dictionary
    "2581510900":{
      "firstName":"توحید",
      "lastName":"اقدامی",
      "phone":"09307827788",
      "taahol":"mojarad",  # mojarad, motahel
      "otaghId":"1",
      "start":datetime(2023, 11, 8),
      "finish":datetime(2023, 11, 10),
      "hazine":890*3 #8'om 9'om 10'om  mishavand 3 rooz
    }
  },
  "2T":{

  },
  "3T":{

  },
  "0T":{

  }
}

# gets
def getUserData(takht:int ,userId:str):
  myUserData = users[str(takht)+"T"][userId]
  return myUserData

def getFreeRooms(takht:int):
  myList = []
  mySelectedRooms = rooms[str(takht)+"T"]

  for roomId in mySelectedRooms:
    if(mySelectedRooms[roomId]["res"] == False):
      myList.append(roomId)
  return myList

def getUsersOfRoom(takht:int, roomId:int):
  myArr = rooms[str(takht)+"T"][str(roomId)]["userIds"]
  return myArr;

def getHazine(takht:int, days:int):
  myHazineBase = hazineOtaghBase[str(takht)+"T"]
  return days*myHazineBase

# sets
def setNewRoom(takht:int, otaghId:int, userId:str):
  rooms[str(takht)+"T"][str(otaghId)]["res"] = True;
  rooms[str(takht)+"T"][str(otaghId)]["userIds"].append(userId)
  return

# otagh = 0 -> free otagh,   otagh = * -> * room
def setNewUser(takht:int, otagh:int, firstName, lastName, userId, phone, taahol, start, finish, hazine): #return otagh id
  # if u give this func (otagh=0) it will find first free room and select it
  otagh = getFreeRooms(str(takht)+"T")[0] if otagh == 0 else str(otagh)

  users[str(takht)+"T"][otagh][userId]={
    "firstName":firstName,
    "lastName":lastName,
    "phone":phone,
    "taahol":taahol,
    "otaghId":otagh,
    "start":start,
    "finish":finish,
    "hazine": hazine
  }
  
  return otagh

def removeUser(userId:str):
  myTakht = ""
  roomId="0"
  # find user in rooms, get takht and remove user
  for takhtRooms in rooms:
    for room in rooms[takhtRooms]:
      if(userId in rooms[takhtRooms][room]["userIds"]):
        myTakht = takhtRooms
        # remove user in rooms
        rooms[takhtRooms][room]["userIds"].remove(userId)
        roomId = room

  # if user user had paid (not 0 hazine)
  if users[myTakht][userId]["hazine"] != 0:
    print("user "+
      str(users[myTakht][userId]["hazine"]*90/100)+
      " hezar tuman daryaft kard(90 darsad az "
      + str(users[myTakht][userId]["hazine"])+ " )")

    if(rooms[myTakht][roomId]["userIds"]!=[]):
      print("This users will remove too(Because of the paying person who canceled the room):")
      for userRemoveId in rooms[myTakht][roomId]["userIds"]:
        print("userId: "+ userRemoveId, end="")
        removeUser(userRemoveId)
        print(" removed")
      print("End")

  # we have takht, so ez remove user
  # remove user in users:
  users[myTakht].pop(userId)
  return

#  to show to the users
def printFreeRooms(takht:int):
  print("RoomId")
  for room in rooms[str(takht)+"T"]:
    if(rooms[str(takht)+"T"][room]["res"]==True):
      print(room)
  return
  
def printResRooms(takht:int):
  print("RoomId\tUsers(s)")
  for room in rooms[str(takht)+"T"]:
    if(rooms[str(takht)+"T"][room]["res"]==True):
      thisRoomUsers = ' va '.join(map(str, rooms[str(takht)+"T"][room]["userIds"]))
      print("{0}\t{1}".format(room, thisRoomUsers))
  return

def printUsers(takht:int):
  takht = str(takht)+"T"
  print("Name(F+L)\tRoomId\tHazine\tUserId")
  for userId in users[takht]:
    myUser = users[takht][userId]
    print(myUser["firstName"]+" "+
        myUser["lastName"]+"\t"+
        myUser["otaghId"]+"\t"+
        str(myUser["hazine"])+"\t"+
        userId
        )

def printHazineBase():
  print("Takht\t\tHazine har nafar baraye 1 shab")
  for takht in hazineOtaghBase:
    if(takht == "0T"):
      print("4T(VIP)\t\t"+str(hazineOtaghBase[takht]))
    else:
      print(takht+"\t\t"+str(hazineOtaghBase[takht]))


# main menu(mm) Functions
def mmShowUsers():
  print("\n\n\n\nShow Users Section")
  print("\n>>>---1 Takhte---<<<")
  printUsers(1)

  print("\n>>>---2 Takhte---<<<")
  printUsers(2)

  print("\n>>>---3 Takhte---<<<")
  printUsers(3)
  
  print("\n>>>---VIP---<<<")
  printUsers(0)

  input("\nBack to main menu")

def mmShowResRooms():
  print("\n\n\n\nShow Res Rooms Section")
  print("\n>>>---1 Takte---<<<")
  printResRooms(1)

  print("\n>>>---2 Takte---<<<")
  printResRooms(2)

  print("\n>>>---3 Takte---<<<")
  printResRooms(3)
  
  print("\n>>>---VIP---<<<")
  printResRooms(0)

  input("\nBack to main menu")

def mmCancelRoom():
  print("\n\n\n\nCancel Room Menu")
  print("Nokte: \tagar user kasi bashad ke hazine ra pardakht karde ast, hameye kasani k toye aan otagh budand niz remove mishavand\n\tagar user kasi bashad ke pardakht nemikonad, moshkeli nadarim, remove mishavad :D")
  userId = input("pls enter your user id(0 to return to main menu): ")

  # back to menu (user enter 0)
  if(userId == "0"): return;

  removeUser(userId)

  input("\nBack to the main menu")

def mmResRoom():
  myDict = {} # to add all users and insert them in dictionary

  print("\n\n\n\nRes Room Menu\n")
  printHazineBase()
  userTakht = int(input("""
              \rchand takhte mikhaiid?(1~3 ya 4(vip))
              \r0 to return to main menu
              \r>> """))

  # back to menu (user enter 0)
  if(userTakht == "0"): return;
  

  teedad = 1 if userTakht==1 else int(input("faqat baraye khodet mikhaii ya chand nafar dige ham hastid?\nteedad nafarat ra vared konid be adad(1=faghat shoma)\n>> "))
  

  if teedad > userTakht: print("invalid value");return

  # change userTakht value 4->0 to use it in our dictionaries
  userTakht = 0 if userTakht == 4 else userTakht
  freeRooms = getFreeRooms(userTakht)
  print("otagh khali "+("nadarim" if freeRooms == [] else "darim"))
  if(freeRooms==[]): input("\nBack to main menu");return ;


  # get day, month, year (start, finish)
  print("Taarikh shoro:")
  myStartDay=int(input("day: "))
  myStartMonth=int(input("month(number): "))
  myStartYear=int(input("year(miladi[->2023]): "))
  myStartDate = datetime(myStartYear, myStartMonth, myStartDay)

  print("Taarikh payan:")
  myFinishDay=int(input("day: "))
  myFinishMonth=int(input("month(number): "))
  myFinishYear=int(input("year(miladi[->2023]): "))
  myFinishDate = datetime(myFinishYear,myFinishMonth,myFinishDay)
  
  daysStartToFinish = (myFinishDate - myStartDate).days + 1 #(+1 baraye avalin roze rezerv)
  if(daysStartToFinish<=0):print("invalid dates");return ;
  mainHazine = teedad*getHazine(userTakht,daysStartToFinish)

  for i in range(teedad):
    userId = input("code melli {0} ra vared kon: ".format("khodet" if i==0 else "shakse baadi"))
    firstName = input("first name:")
    lastName = input("last name:")
    phone = input("phone:")
    taahol = input("taahol(mojarad/motahel):")
    userhazine = mainHazine if i==0 else 0
    myDict[userId]={
      "firstName":firstName,
      "lastName":lastName,
      "phone":phone,
      "taahol":taahol,  # mojarad, motahel
      "otaghId":freeRooms[0],
      "start":myStartDate,
      "finish":myFinishDate,
      "hazine":userhazine
    }
  userTakht=str(userTakht)+"T"

  # insert Data into rooms
  rooms[userTakht][freeRooms[0]]["res"] = True;
  rooms[userTakht][freeRooms[0]]["userIds"]=list(myDict.keys())

  # insert Data into users
  for userId in myDict:
    users[userTakht][userId]=myDict[userId]


  input("\nBack to main menu")

def main():
  mainMenu = """\n>> Main Menu <<
            \r1.Res a room
            \r2.Cancel room res
            \r3.Users List
            \r4.Rooms List
            \r0.Exit
            \rPls Enter Number >> """
  menuCotroller = ""
  while(menuCotroller!="0"):
    menuCotroller = input(mainMenu)
    match menuCotroller:
      case "1":
        mmResRoom()

      case "2":
        mmCancelRoom()
        
      case "3":
        mmShowUsers()
        
      case "4":
        mmShowResRooms()

      case "0":
        print("Bye")

      case _:
        print("Pls Enter Valid Number")

if __name__ == "__main__":
    main()