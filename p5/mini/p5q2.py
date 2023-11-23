myDict={}

teedad = int (input("tedad? : "))

def getNumbers():
  for i in range(teedad):
    number = float(input("addad "+str(i+1)+" om raa vaared konid: "))
    myDict[number]=""
    

def getOstans():
  for i in myDict:
    myDict[i]=input("ostane "+str(i)+" metri raa vaared konid: ")


if(teedad>32 or teedad < 1): print("error");
else:
  getNumbers();
  myDict = dict(sorted(myDict.items()))
  getOstans();

  # write into file
  myFile = open("myfile.txt","w")
  for i in myDict:
    myStr = myDict[i]+" "+str(i)+" \n"
    myFile.write(myStr)
  myFile.close()



