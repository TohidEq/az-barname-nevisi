n = int(input("tedaade dars ha: "))
nmreha = 0
for i in range(n):
  qmsg = "nomreye "+str(i+1)+" om ra vaared konid:"
  nmreha += float(input(qmsg))
print("moaddel: ",nmreha/n)