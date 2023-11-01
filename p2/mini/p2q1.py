myNumber = int(input("lotfan adade 3 raghami khod ra vaared konid: "))
x = myNumber;
y = ""; #mabnaye 2
while x!=0:
  y = str(x%2)+str(y)
  x = x//2

print(myNumber, " => be mabnaye 2 => ", y)

x = myNumber;
y = ""; #mabnaye 8
while x!=0:
  y = str(x%8)+str(y)
  x = x//8

print(myNumber, " => be mabnaye 8 => ", y)

