
# 18pontos
# A rádióhallgatás ma már egyre inkább zene vagy hírek hallgatására korlátozódik. Ez a feladat három, folyamatosan zenét sugárzó adóról szól, azok egyetlen napi műsorát feldolgozva. Az adókat nevük helyett egyetlen számmal azonosítottuk. A musor.txt minden sora négy, egymástól pontosvesszővel elválasztott adatot tartalmaz: a rádió sorszámát, amit a szám hossza követ két egész szám (perc és másodperc) formában, majd a játszott szám azonosítója szerepel, ami a szám előadójából és címéből áll. A rádió sorszáma az 1, 2, 3 számok egyike. Az adás minden adón 0 óra 0 perckor kezdődik. Egyik szám sem hosszabb 30 percnél, tehát a perc értéke legfeljebb 30, a másodperc pedig legfeljebb 59 lehet. A szám azonosítója legfeljebb 50 karakter hosszú, benne legfeljebb egy kettőspont szerepel, ami az előadó és a cím között található. A számok az elhangzás sorrendjében szerepelnek az állományban, tehát a később kezdődő szám későbbi sorban található. Az állományban minden zeneszám legfeljebb egyszer szerepel.

# a.	Hány adatsort tartalmaz a szövegfájl.
# b.	Kérje be egy előadó nevét és írassa ki az általa játszott számok címeit!
# c.	Melyik szám a legrövidebb!
# d.	Írja ki egy musor_statisztika.txt szövegfájlba, hogy az egyes előadóknak hány zenéje lett lejátszva!

# 1p Megnyitja olvasásra a fájlt
# 1p Beolvassa a fájl minden sorát
# 1p Megfelelő adatszerkezetet választ az adatok eltárolására
# 1p Jól olvassa be a fájl sorait az adatszerkezetbe
# 1p Lezárja a megnyitott fájlt
# 1p Meghatározza, hogy hány sort tartalmaz a fájl
# 1p Helyesen írja ki, hogy hány könyv adatait tartalmazza a fájl
# 1p Bekéri az előadó nevét
# 1p Jól szűr az előadó számaira
# 1p Kiírja az előadóhoz tartozó számokat
# 2p Kiválasztja a  legrövidebb számot
# 1p Kiírja a legrövidebb szám címét
# 1p Meghatározza, hogy melyik előadótól hány számot játszottak
# 1p Megnyitja írásra a statisztika.txt fájlt
# 1p Ír a fájlba
# 1p Minden adatot jól kiírja a fájlba
# 1p Lezárja a megnyitott fájlt

zenek = []
zene = {}

with open("musor.csv", "r", encoding="utf-8") as bemenet:
    for sor in bemenet:
        adatok = sor.strip().split(";")
        zene["radio_sorszama"] = adatok[0]
        zene["szam_hossza_perc"] = int(adatok[1])
        zene["szam_hossza_masodperc"] = int(adatok[2])
        zene["eloado"] = adatok[3].split(":")[0]
        zene["cim"] = adatok[3].split(":")[1]
        zenek.append(zene)
        zene = {}
# Itt fejeztük be
