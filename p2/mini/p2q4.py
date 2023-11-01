myHotelDB = {
  "agha":[{
    "username":"tohid",
    "sans":"14"
  },{
    "username":"ali",
    "sans":"15"
  }],
  "khanum":[{
    "username":"kokab",
    "sans":"7"
  },{
    "username":"zahra",
    "sans":"7"
  }]
}

def checkFreeSansAgha(mySans:str):
  # print(myStr)
  checker = 0
  for i in myHotelDB["agha"]:
    if(i["sans"]==mySans):
      checker+=1

  print("sans check tedaad: ", checker)
  if(checker>=15):
    return 0
  else:
    return 1
# ----end checkFreeSansAgha()----

def checkFreeSansKhanum(mySans:str):
  # print(myStr)
  checker = 0
  for i in myHotelDB["khanum"]:
    if(i["sans"]==mySans):
      checker+=1

  print("sans check tedaad: ", checker)
  if(checker>=15):
    return 0
  else:
    return 1
# ----end checkFreeSansKhanum()----

# add usere  aaghaa
def addAgha():
  name = input("name: ")
  sans = input("sans (14~22)[har sans 1 saat ast, az 14 ta 23 mitavanid varzesh konid]: ")
  
  # sans dar baazeye [14,22] nabashad -> end(return 0)
  if(not(int(sans) in range(14,23))):
    print("sans eshtebah ast")
    return 0

  if(checkFreeSansAgha(sans)):
    print("free is sans")
  else:
    print("sans is not free");
    return 0
  # daryaft hazine o sabt e naam
  hazine = int(input("hazine mahiane 350, movafegh hastid?: (1=yes,0=no)"))
  if(hazine == 1):
    myHotelDB['agha'].append({"username": name, "sans": sans})
# ----end addAgha()----

# add usere khaanum
def addKhanum():
  name = input("name: ")
  sans = input("sans (7~12)[har sans 1 saat ast, az 7 ta 13 mitavanid varzesh konid]: ")

  # sans dar baazeye [7,12] nabashad -> end(return 0)
  if(not(int(sans) in range(7,13))):
    print("sans eshtebah ast")
    return 0

  if(checkFreeSansAgha(sans)):
    print("free sans")
  else:
    print("sans is not free");
    return 0

  # daryaft hazine o sabt e naam
  hazine = int(input("hazine mahiane 350, movafegh hastid?: (1=yes,0=no)"))
  if(hazine == 1):
    myHotelDB['khanum'].append({"username": name, "sans": sans})
# ----end addKhanum()----

# print kardane kolle varzeshkaran + sanse anha
def printJadval():
  print("\nAghayoun: ")
  print("name\t|\tsans")
  
  for i in myHotelDB["agha"]:
    print(i["username"],"\t|\t",i["sans"])

  print("\nKhanuma: ")
  print("name\t|\tsans")

  for i in myHotelDB["khanum"]:
    print(i["username"],"\t|\t",i["sans"])
  print("\n")
# ----end printJadval()----

# menu handler
myHandler = input("q = exit\n1 = add agha\n0 = add khanum\n3 = show all\n>> ").upper()

# menu
while myHandler !="Q":
  match myHandler:
    case "1":
      addAgha();

    case "2":
      addKhanum();

    case "3":
      printJadval();

    case "Q":
      print("\n")
      print("bye")
      break;
  myHandler = input("q = exit\n1 = add agha\n0 = add khanum\n3 = show all\n>> ").upper()

