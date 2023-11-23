myNumber = int(input("adade sahihe mosbat: "))

x = myNumber;
y = ""; #mabnaye 16
while x!=0:
  y = str(x%16)+str(y)
  x = x//16

print(myNumber, " => be mabnaye 16 => ", y)

