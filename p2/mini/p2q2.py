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