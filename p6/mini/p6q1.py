
aamozeshDB={}

daneshjooDB={}










def printVaahedHa():
  for i in aamozeshDB:
    if(aamozeshDB[i]["pishniaz"]=="0"):
      print ("name: ", aamozeshDB[i]["name"], "\t code dars: ", i, "\t node dars: ", aamozeshDB[i]["type"], "\t vahed dars: ", str(aamozeshDB[i]["vaahed"]))



def Daneshjoo():
  codeDanshjoii = input("code danshjoii: ")
  print("list vaahed ha")
  printVaahedHa()
  vaahedHa = input("vaahed haye khood ra vaared konid(just numbers): ").split(" ")
  numberOfVaheds = 0
  for i in vaahedHa:
    numberOfVaheds += aamozeshDB[i]["vaahed"]

  if(numberOfVaheds>20):
    print("error, vaahed ha ziad hastand")

  daneshjooDB[codeDanshjoii]=vaahedHa




def Aamoozesh():
  numberOfInputs = int(input("chand taa dars vaared shavand? "))

  for i in range(numberOfInputs):
    codeDars = input("code dars: ")
    naameDars = input("naame dars: ")
    noeDars = input("noe dars(1.omomi,  2.takhasosi,  3.ekhtiari)")
    tedadVaahed = input("tedad vahed: ")
    pishniaz = input("pishniaz daarad (1/0)")

    aamozeshDB[codeDars]={
      "name":naameDars,
      "type":noeDars,
      "vaahed":int(tedadVaahed),
      "pishniaz":pishniaz
    }



def showResaults():
  print("code daneshjoii\t--\t code vaahed haa \t--\t jaame vaahed haa")
  for i in daneshjooDB:
    numberOfVaheds = 0
    vaahedHa = daneshjooDB[i]
    for k in vaahedHa:
      numberOfVaheds += aamozeshDB[k]["vaahed"]

    nameVahedHa = " ";
    for j in daneshjooDB[i]:
      nameVahedHa+= aamozeshDB[j]["name"]+" "
      

    print(i,"\t--\t", ' '.join(daneshjooDB[i]), nameVahedHa , "\t--\t", str(numberOfVaheds) )













menuText="""
        \r1. Aamozesh
        \r2. Daneshjoo
        \r3. list daneshjooha o vaahed haa
        \r0. Exit
        \r>> """

menuControl = ""


while(menuControl != "0"):
  menuControl = input(menuText)
  match menuControl:
    case "1":
      print("Aamoozesh:")
      Aamoozesh()
    case "2":
      print("Daneshjoo:")
      Daneshjoo()
    case "3":
      print("list daneshjooha o vaahed haa:")
      showResaults()
    case "0":
      print("\n\nBye\n\n")
    case _:
      print("wrong number")

  

