num1 = int(input("adad 1: "))
num2 = int(input("adad 2: "))

for i in range(num1+1,num2):
  print("mazaarebe adade ",i)
  for j in range(1,i+1):
    if(i%j==0):
      print(j)

