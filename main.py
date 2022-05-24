import math

n = int(input())
figury = []
def oblicz():
    pola = []
    for m in range(n):
        m = map(float, input().split())
        wymiary = list(m)
        
        if(len(wymiary) == 1):
            kolo=math.pi * (wymiary[0]**2)
            pola.append(kolo)

        elif(len(wymiary) == 2):
            prostokat=wymiary[0]*wymiary[1]
            pola.append(prostokat)

        elif(len(wymiary) == 3):
            pol_obw = 0.5*(wymiary[0]+wymiary[1]+wymiary[2])
            trojkat = math.sqrt(pol_obw*(pol_obw-wymiary[0])*(pol_obw-wymiary[1])*(pol_obw-wymiary[2]))
            pola.append(trojkat)

        elif(len(wymiary) >= 4):
            print("Błąd: można podać maksymalnie 3 liczby")
            return

    suma_pola = sum(pola)
    suma_wsz_pol = round(suma_pola, 2)
    print(suma_wsz_pol)
        
oblicz()