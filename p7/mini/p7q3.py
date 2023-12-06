import sys


tedad = int(input("chand adad data darim?: "))

resault = ""

for i in range(tedad):

    myinput = input("enter your value pls: ")
    if myinput.isnumeric():
        myinput = int(myinput)
    resault = resault+str(myinput)+" : "+str(sys.getsizeof(myinput))+" byte \n"

print(resault)
