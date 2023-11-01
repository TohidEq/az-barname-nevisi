def app1():
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



def app2():
  x = []
  x.append(int(input("zel'e 1: ")))
  x.append(int(input("zel'e 2: ")))
  x.append(int(input("zel'e 3: ")))
  x.sort()

  zel = x[1];
  ghaede = 0;
  # agar tedade mohtavaye andise 0 dar Arr == 1 bashad =>  yani andis 0 mishavad ghaedeye mosalas
  if x.count(x[0]) == 1:
    ghaede = x[0]
  # dar gheyre in sorat, andis 2 mishavad ghaede (estesna, har se zel ba ham barabar bashad, NP, moshkeli nadarim)
  else: 
    ghaede = x[2]


  mohitMosalas = zel+zel+ghaede
  print("mohit Mosalas:\t",mohitMosalas)
  mohitMosalasZiri = ghaede*3
  print("mohit MosalasZiri:\t",mohitMosalasZiri)
  mohitHeram = mohitMosalas*3 + mohitMosalasZiri
  print("mohit Heram:\t",mohitHeram)





myHandler = input("q = exit\n1 = barnameye 1\n2 = barnameye 2\n>> ").upper()
while myHandler !="Q":
  match myHandler:
    case "1":
      print("\n")
      app1();
      print("\n")

    case "2":
      print("\n")
      app2();
      print("\n")

    case "Q":
      print("\n")
      print("bye")
      break;
  myHandler = input("q = exit\n1 = barnameye 1\n2 = barnameye 2\n>> ").upper()

