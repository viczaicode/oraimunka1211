# csomagolopapir.py

def meghivas():
    print("A Mikulás manói csomagoló papírt készítenek.")
    szam1 = int(input("Kérem, adja meg az első számot: "))
    szam2 = int(input("Kérem, adja meg a második számot: "))
    keszit(szam1,szam2)


def keszit(szam1, szam2):
    if szam1 > szam2:
        szam1, szam2 = szam2, szam1

    eredmeny = ""
    elso_szam = True

    for szam in range(szam1, szam2+1):
        if not elso_szam:
            eredmeny += "*"
        elso_szam = False

        eredmeny += str(szam)

    print(f"\nA csomagoló papír: {eredmeny}")
    print("\bMegjegyzés: A negatív számokat a csillag (*) karakter választja el.")