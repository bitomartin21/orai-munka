import random

szam=[]
osszeg=0
db=0
for x in range(10):
    szam.append(random.randrange(1,100))
print(szam)
print("átlag ",sum(szam) / 10)
print("minimum ",min(szam))
print("maximum ",max(szam))
paros=False
for x in szam:
    if (x%2 == 0):
        paros=True
if paros is True:
    print("van páros szám")
else:
    print("nincs páros szám")

for x in szam:
    if x>50:
        osszeg=osszeg+x
print("50-nél nagyobb számok összege ", osszeg)


for x in szam:
    if x==9:
        db=db+1
print("hány 9 van: " ,db)