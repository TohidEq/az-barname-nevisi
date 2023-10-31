import  math;
def zojofard(x):
  if not x%2:
    return "zoj"
  else: 
    return "fard"

def avval(x):
  if(x<2): 
    return 0
  if(x==2): 
    return 1
  
  for i in range(2,x):
    if(x%i==0):
      return 0
  return 1


print("adad:\t | \t zoj o fard:\t | \tavval:")
for i in range(1,50):
  print(i,"\t | \t",zojofard(i),"\t\t | \t",avval(i))
