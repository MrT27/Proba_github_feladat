# #8pontos
# """
# Írj egy Python programot, amely bekér egy egész számot a felhasználótól és kiírja a képernyőre, hogy osztható-e a szám 3-mal vagy 5-tel, illetve kiírja a képernyőre azt a számot, amely az ennél a számnál nem nagyobb pozitív egész számok összege! 

# 1p Bekér egy int-et
# 1p oszthatóság feltételei jók
# 1p jól szervezte az elágazást
# 1p jók a kiírások
# 1p felvett egy gyűjtőváltozót 0 kezdőértékkel
# 1p ciklussal járja be a számokat
# 1p az összeg jó, amibe beleveszi a bekért számot is
# 1p kiírás a mintának megfelelő
# """

# be_szam=int(input("Kérek egy egész számot: ") or "23") 
 
# if be_szam%3==0 or be_szam%5==0:
#   print(f"{be_szam} osztható 3-mal vagy 5-tel.")
# else:
#   print(f"{be_szam} nem osztható 3-mal vagy 5-tel.")

# osszeg=0
# for i in range(1,be_szam):
#   osszeg+=i

# print(f"szum(1-{be_szam})={osszeg+be_szam}")


# #14pontos 
# """
# Írj egy Python programot, amelyben billentyűzetről feltöltesz egy listát, Enter végjelig, 1-10-ig számokkal, majd a program létrehoz egy másik listát, amelynek elemei megegyeznek az előbbi lista elemeivel ismétlődések nélkül! Írasd képernyőre a két rendezett listát!

# 1p 2db lista létrehozása
# 1p ciklus szervezése jó
# 1p bekér egy számot (stringbe is jó)
# 1p a listához adás jó (üres elemet kihagyja)

# 1p bejárja az eredeti listát
# 1p tud hivatkozni az egyes elemekre
# 1p jó a feltétel a tartalmazásvizsgálatnál
# 1p jól szervezte az elágazást
# 1p a módosított listához adás jó 

# 1p rendezte az eredeti listát
# 1p kiírja az eredeti listát
# 1p rendezte a módosított listát
# 1p kiírja a módosított listát
# 1p a listák kiírása a mintának megfelelő

# """

# lista_eredeti=[]
# be_szam=None
# while be_szam!="":
#   be_szam=input("Kérem a következő számot: ")
#   if be_szam!="":
#     lista_eredeti.append(int(be_szam))

# lista_modositott=[]
# #rossz: lista_modositott=[elem for elem in lista_eredeti if not (elem in lista_modositott)]
# #lista_modositott=list(set(lista_eredeti))
# for elem in lista_eredeti:
#    if not elem in lista_modositott:
#      lista_modositott.append(elem)


# lista_eredeti.sort()
# lista_modositott.sort()

# print("Eredeti lista: \n",", ".join(map(str, lista_eredeti)))
# print("\nMódosított lista: \n",", ".join(map(str, lista_modositott)))

#18pontos
"""
A rádióhallgatás ma már egyre inkább zene vagy hírek hallgatására korlátozódik. Ez a feladat három, folyamatosan zenét sugárzó adóról szól, azok egyetlen napi műsorát feldolgozva. Az adókat nevük helyett egyetlen számmal azonosítottuk. A musor.txt minden sora négy, egymástól pontosvesszővel elválasztott adatot tartalmaz: a rádió sorszámát, amit a szám hossza követ két egész szám (perc és másodperc) formában, majd a játszott szám azonosítója szerepel, ami a szám előadójából és címéből áll. A rádió sorszáma az 1, 2, 3 számok egyike. Az adás minden adón 0 óra 0 perckor kezdődik. Egyik szám sem hosszabb 30 percnél, tehát a perc értéke legfeljebb 30, a másodperc pedig legfeljebb 59 lehet. A szám azonosítója legfeljebb 50 karakter hosszú, benne legfeljebb egy kettőspont szerepel, ami az előadó és a cím között található. A számok az elhangzás sorrendjében szerepelnek az állományban, tehát a később kezdődő szám későbbi sorban található. Az állományban minden zeneszám legfeljebb egyszer szerepel.
a.	Hány adatsort tartalmaz a szövegfájl.
b.	Kérje be egy előadó nevét és írassa ki az általa játszott számok címeit!
c.	Melyik szám a legrövidebb!
d.	Írja ki egy musor_statisztika.txt szövegfájlba, hogy az egyes előadóknak hány zenéje lett lejátszva! 

1p Megnyitja olvasásra a fájlt
1p Beolvassa a fájl minden sorát
1p Megfelelő adatszerkezetet választ az adatok eltárolására
1p Jól olvassa be a fájl sorait az adatszerkezetbe
1p Lezárja a megnyitott fájlt
1p Meghatározza, hogy hány sort tartalmaz a fájl
1p Helyesen írja ki, hogy hány könyv adatait tartalmazza a fájl
1p Bekéri az előadó nevét
1p Jól szűr az előadó számaira
1p Kiírja az előadóhoz tartozó számokat
2p Kiválasztja a  legrövidebb számot
1p Kiírja a legrövidebb szám címét
1p Meghatározza, hogy melyik előadótól hány számot játszottak
1p Megnyitja írásra a statisztika.txt fájlt
1p Ír a fájlba
1p Minden adatot jól kiírja a fájlba
1p Lezárja a megnyitott fájlt

"""

zenek=[]
zene={}

with open("musor.csv","r",encoding="utf-8") as bemenet:
    for sor in bemenet:
        adatok=sor.strip().split(";")
        zene["radio_sorszama"]=adatok[0]
        zene["szam_hossza_perc"]=int(adatok[1])
        zene["szam_hossza_masodperc"]=int(adatok[2])
        zene["eloado"]=adatok[3].split(":")[0]
        zene["cim"]=adatok[3].split(":")[1]
        zenek.append(zene)
        zene={}

print(f"a. A fájl {len(zenek)} darab adatsort tartalmaz.")


be_eloado=input("\nb. Kérem egy előadó nevét: ") or "Frank Zappa"
print(f"{be_eloado} számai:")
for zene in zenek:
    if zene["eloado"]==be_eloado:
        print(f"\t{zene['cim']}")

def minkivalasztas(lista):
    min_index=0
    for i in range(1,len(lista)):
        if lista[i]["szam_hossza_perc"]*60+lista[i]["szam_hossza_masodperc"]<lista[min_index]["szam_hossza_perc"]*60+lista[min_index]["szam_hossza_masodperc"]:
            min_index=i
    return min_index

print(f"\nc. A legrövidebb szám címe: {zenek[minkivalasztas(zenek)]['cim']}")

statisztika={}
for zene in zenek:
    if zene["eloado"] in statisztika:
        statisztika[zene["eloado"]]+=1
    else:
        statisztika[zene["eloado"]]=1

with open("musor_statisztika.txt","w",encoding="utf-8") as kimenet:
    for kulcs in statisztika:
      print(f"{kulcs} - {statisztika[kulcs]}", file=kimenet) 


