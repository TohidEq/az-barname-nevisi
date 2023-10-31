numK = int(input("tedade karmandan: "))
mylist=[]

for i in range(numK):
  print("vorodi haye ",i," om:")
  username = input("esme kaarmand: ")
  daraamad = int(input("daraamad maahiane: "))
  hoghugh = daraamad
  
  if(daraamad<=600 and  300 <= daraamad):
    # 7%
    hoghugh = daraamad-(daraamad*7/100)
  if(daraamad > 800):
    # 12%
    hoghugh = daraamad-(daraamad*12/100)
  mylist.append({"username":username, 
    "daraamad kol":daraamad,
    "hoghugh daryafti":hoghugh})

print("username\t|\tdaraamad kol\t|\tthoghugh daryafti")
for item in mylist:
  print(item["username"],"\t\t|\t",item["daraamad kol"],"\t\t|\t",item["hoghugh daryafti"])

  
