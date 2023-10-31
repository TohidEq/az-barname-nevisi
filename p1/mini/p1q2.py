n = int(input("tedaade daneshjoo ha: "))
daneshjooha = {}
for i in range(n):
  qmsg = "esme daneshjoye "+str(i+1)+" om ra vaared konid:"
  esm = input(qmsg)

  qmsg = "nomreye daneshjoye "+str(i+1)+" om ra vaared konid:"
  nmre = float(input(qmsg))

  if(nmre<12):
    daneshjooha[esm] = nmre

if daneshjooha!={}:
  for i in daneshjooha:
    print(i,"\tmardood! \tnomre: ", daneshjooha[i])
else:
  print("hame ghabul shodan")

