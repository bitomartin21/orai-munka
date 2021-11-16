szamok=[3,4,2,7,8,1,9,7,3]

#összegzés tétele
osszeg=0
for x in szamok:
    osszeg=osszeg+x
    print(osszeg)
print(osszeg)
print (sum(szamok))

#eldöntés tétele
vane =False
for x in szamok:
    if (x==1):
        vane=True
print(vane)

#megszámlálás
db=0
for x in szamok:
    if x==3:
        db=db+1
print(db)

#feltételes összegzés
osszeg=0
for x in szamok:
    if x%2==0:
        osszeg=osszeg+x
print("páros számok összege: ")
print(osszeg)

#minimum
print("minimum")
min=1000
for x in szamok:
    if x<min:
        min=x
print(min)

#maximum
print("maximum")
max=1
for x in szamok:
    if x>max:
        max=x
print(max)