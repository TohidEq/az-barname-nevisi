myDict={}

# read file
myFile = open("myfile.txt","r")
myList = myFile.readlines()

for item in myList:
  strList = (item.split(" "))
  myDict[strList[1]]=strList[0]
myFile.close()


# print natayej
print("print natayej:")
for i in myDict:
    myStr = myDict[i]+" "+str(i)
    print(myStr)
