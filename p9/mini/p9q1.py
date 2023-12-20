import hezlouli;







myMenu = """\r
          \r+ jam
          \r- menha
          \r/ taghsim
          \r* zarb
          \r** tavan
          \rj jazr
          \r0 exit
          \r>> """

def mashinHesab():
  
  myInput = "nothing :)"
  myControl = False;
  myResult = 0
  while(myInput != "0"):
    myInput = input(myMenu)
    match myInput:
      case "+":
        myResult = float(input("number 1:"))+float(input("number 2:"))
        myControl = True
      case "-":
        myResult = float(input("number 1:"))-float(input("number 2:"))
        myControl = True
      case "/":
        myResult = float(input("number 1:"))/float(input("number 2:"))
        myControl = True
      case "*":
        myResult = float(input("number 1:"))*float(input("number 2:"))
        myControl = True
      case "**":
        myResult = float(input("number 1:"))**float(input("number 2:"))
        myControl = True
      case "j":
        myResult = float(input("number :"))**0.5
        myControl = True
      case "0":
        print("bye")
        input("press anykey to exit")
        break;
      case _:
        print("invalid value")
        input("press anykey to run again")

    if(myControl == True):
      print(f"javab = {myResult}")


      # use hezlouli app:
      print(f"masahat hezlouli ba adade({myResult}) = {hezlouli.hezlouliS(myResult)}")


      input("press anykey to run again")








mashinHesab()
