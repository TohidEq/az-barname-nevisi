import numpy

# m*n   m = satr,  n = sotun
# tedad <soton> matris aval ba <satr> matris dovom barabar bayad bashad

matris_1_test = [[1, 2,  3,  4],
            [1, 2,  3,  4],
            [1, 2,  3,  4],
            [1, 2,  3,  4]]
            
matris_2_test = [[6, 8,  2,  5],
            [6, 8,  2,  5],
            [6, 8,  2,  5],
            [6, 8,  2,  5]]

matirs_1 = [];
matris_2 = [];


def input_matris(m,n):
  myMatris = []
  
  print("beyne item ha spase(' ') gharar dahid,\nmesaal: 12 32 54 65\n")
  for i in range(m):
    # daryaft vorodi
    myInput = input(f"radif {i+1} om ra vaared konid\n>> ").split(" ");

    # check kardane teedad
    if myInput.len != n:
      print("vorodi naadorost ast...")
      return -1; # khoroj az func

    # tabdil be int
    myRow = []
    for i in myInput:
      myRow.append( int(i) )
    myMatris.append(myRow)

  return myMatris



def zarbMatris(myMatris_1, myMatris_2):
  myMatris_1 = numpy.array(myMatris_1)
  myMatris_2 = numpy.array(myMatris_2)
  myArr = myMatris_1.dot(myMatris_2)

  return myArr;

def showMatris(myMatris):
  for i in myMatris:
    for j in i:
      print(j,end="\t")
    print("")



def newMatrisDot():
  print("""m*n   m = satr,  n = sotun
        \rtedad <soton> matris aval ba <satr> matris dovom barabar bayad bashad""")

  matris_1_m = input("matris 1 m(satr) \t>> ")
  matris_1_n = input("matris 1 n(sotun)\t>> ")

  matris_2_m = matris_1_n
  print(f"matris 2 m(satr) = {matris_2_m} = matris 1 n(sotun)")

  matris_2_n = input("matris 2 n(sotun)\t>> ")

  print("\ninput matris 1 data:")
  matirs_1 = input_matris(matris_1_m, matris_1_n)

  print("\ninput matris 2 data:")
  matirs_2 = input_matris(matris_2_m, matris_2_n)

  print("\n\n")

  print("matris 1:")
  showMatris(matris_1)
  print("matris 2:")
  showMatris(matris_2)


  print("zarb:")
  showMatris(zarbMatris(matris_1,matris_2))



def testMatrisDot():
  print("matris 1:")
  showMatris(matris_1_test)
  print("matris 2:")
  showMatris(matris_2_test)

  print("zarb:")
  showMatris(zarbMatris(matris_1_test,matris_2_test))


control = True;
while(control):
  myInput = input("\n\n1. zarb matris haye jadid\n2. zarb matris haye testi\n0. exit")

  match(myInput):
    case "1":
      newMatrisDot()
      break;
    case "2":
      testMatrisDot()
      break
    case "0":
      print("bye")
      control = False;
      break


