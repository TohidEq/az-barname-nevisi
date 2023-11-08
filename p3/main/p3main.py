from datetime import datetime, timedelta

hazineOtaghBase = {
  "1T":890,
  "2T":1620,
  "3T":2100,
  "VIP":3720
}

# rooms>takht>roomId>(res?, userIds)
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
  "VIP":{
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
      "hazine":890
    }
  },
  "2T":{

  },
  "3T":{

  },
  "VIP":{

  }
}

# gets
def getUserData(takht:int ,userId:string):
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
def setNewRoom(takht:int, otaghId:int, userId:string):
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






def removeUser(userId:string):
  myTakht = ""
  # find user in rooms, get takht and remove user
  for takhtRooms in rooms:
    for room in rooms[takhtRooms]:
      if(userId in rooms[takhtRoom][room]["userIds"]):
        myTakht = takhtRooms
        # remove user in rooms
        rooms[takhtRoom][room]["userIds"].remove(userId)

  # if user user had paid (not 0 hazine)
  if users[myTakht][userId]["hazine"] != 0:
    print("user "+
      users[myTakht][userId]["hazine"]*90/100+
      " hezar tuman daryaft kard(90 darsad az "
      + users[myTakht][userId]["hazine"]*90/100+ " )")

  # we have takht, so ez remove user
  # remove user in users:
  users[myTakht].pop(userId)
  return




#  to show to the users
def printFreeRooms(takht:int):
  return
def printResRooms(takht:int): 
  return



# date1 = datetime(2022, 1, 1)
# date2 = datetime(2022, 2, 15)
# difference = date2 - date1

# print(difference.days)

