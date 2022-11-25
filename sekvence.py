           #0     #1    #2
osoba = ["Marko", 25, "iOS"]
print(osoba)

print(osoba[0])
print(osoba[1])
print(osoba[2])


# for broj in range(5):
#     print(broj)

# for broj in range(5, 20):            - RANGE
#     print(broj)

# for broj in range(0, 31, 2):
#     print(broj)

kurs = "Python"

print(kurs[0])
print(kurs[1])
print(kurs[2])                     #- STRING
print(kurs[3])
print(kurs[4])
print(kurs[5])

print(len(kurs))  # BROJ CLANOVA

for indeks in range(len(kurs)-1):
   print(kurs[indeks])

ustanova = "IT Academy"
print(len(ustanova))

for slovo in range(len(ustanova)-1):    # Prvi nacin
    print(ustanova[slovo])


for slovo in ustanova:     # Drugi nacin
    print(slovo)

# tip_korisnika = "admin"               # STRING NIJE MUTABILAN
# tip_korisnika[0] = "A"

# korisnicko_ime = input("Unesite korisnicko ime: ")

# #Admin1 -> admin1 - LOWER           #amin -> ADMIN - UPPER

# if korisnicko_ime.lower() == "admin1":
#     print("Dobrodosli!")
# else:
#     print("Neispravni podaci")

tekst = "A*B#*C#D"

# VREDNOST

for slovo in tekst:
    if slovo != "*" and slovo != "#":
        print(slovo)

# INDEKS

for x in range(len(tekst)-1):
    if tekst[x] == "*":
        print("* je na poziciji", x)
    elif tekst[x] == "#":
        print("# je na poziciji", x)
    else:
        print(tekst[x])

slovo = "A"
print(slovo in tekst)

#LISTA

telefoni = ["iPhone X", "Samsung Galaxy A22", "Huawei Mate 50"]
print(telefoni[1])

telefoni[0] = "iPhone 12 PRO"

# Ponuda telefona 

for telefon in telefoni:
    print(telefon)

for indeks in range(len(telefoni)-1):
   #print(indeks)
    print(telefon[indeks])

# Sve dok je br indeksa mmanji od rednog broj poslednjeg clana
indeks = 0 
duzina_liste = len(telefoni) #2

while indeks < duzina_liste:
    print(telefoni[indeks])
    indeks+= 1


# ponuda_smerova = ["python", "php", "ios", "java"]
# zeljeni_smer = input("Unesite smer koji zelite: ")

# for smer in ponuda_smerova:
#     if zeljeni_smer == smer:
#         print("Uspesno ste upisani! ")
#         break
#     else:
#         print("Niste upisani...")

ponuda_smerova = ["python", "php", "ios", "java"]           # - Append (DODAVANJE U LISTU)
ponuda_smerova.append("c#")                                            

print(ponuda_smerova)

proba= []
proba.append(5)
proba.append("hello")
print(proba)

# proba.clear()                    # - Clear (BRISANJE SVIH CLANOVA)
# proba.remove(5)                  # - Remove (UKLANJA TU VREDNOST)
# proba.pop(0)                     # - Pop - (UKALADNJA VREDNOST NA TOM INDEKSU)
# del proba[0]                     # - Del - (UKLANJA VREDNOST NA TOM INDEKSU)
print(proba)

                #0      #1      #2       - Broj indeksa
laptopovi = ["acer", "dell", "macbook"]
        #        0     3 
for i in range(len(laptopovi)):                 # Indeks    
    print(laptopovi[i])                        


for vrednost in laptopovi:                      # Vrednost
    print(vrednost)


for i, v in enumerate(laptopovi):               # Indeks i Vrednost
    print("Indeks: ", i, "Vrednost: ", v)   #ili  - print(i, v)

termini =["ponedeljak", "sreda", "petak"]

for x in range(len(termini)):
    if "utorak" == termini[x]:
        print("Dodajte i utorak u spisak")                 
    print(termini[x])

if "utorak" in termini:
    print("Utorak je medju terminima ")
else:
    print("Dodajte i utorak")

# if not "utorak" in termini: Da li se ne nalazi

smerovi = ["python", "php", "ios", "java", "c#", "frontend", "android"]

                    # pocetak kraj i korak
promocija = smerovi[1:4:2]                   # Isto se pise kao "range", ali nije isto! "range (0, 10, 2)"
print(promocija)

korisnici = ["petar", "marija", "jovana", "milos", "vladimir", "katarina"]
pobednici = korisnici[0:3]
print(pobednici)                                            # - Kraci nacin(Skracenica)
pobednici.clear()
                                                            # - Isti je rezultat u oba primera!
for i in range(len(korisnici)):
    if i == 0 or i == 1 or i == 2:
        pobednici.append(korisnici[i])                      # - Duzi nacin

print(pobednici)

brojevi = [1, 10, 7, 2, 6, 3, 17, 30]

parni = []
neparni = []

# for petlja za proveru parnog ili neparnog broja
# if else
# % 2 == 0
# append

for broj in brojevi:
    parni.append(broj) if broj %2 == 0 else neparni.append(broj)    # Kraci nacin (Ispravno)
    #if else strukture 

    # if broj %2 == 0:
    #     parni.append(broj)                # - Duzi nacin (Ispavno)
    # else:
    #     neparni.append(broj)
    
print("Parni: ", parni)
print("Neparni: ", neparni)

# rec = input("Unesite rec: ")      
# pocetni_indeks = 0
# krajnji_indeks = len(rec)-1
# palindrom = True

# while pocetni_indeks < krajnji_indeks:
#     if rec[pocetni_indeks] != rec[krajnji_indeks]:
#         print("Nije palindrom")
#         palindrom = False
#         break
#     pocetni_indeks +=1
#     krajnji_indeks -=1 
# else:
#     print("Jeste palindrom")

# print("Rec", rec, ("Jeste" if palindrom else "Nije"), "palindrom")



'''
rec[0] == rec[14]
rec[1] == rec[13]
rec[2] == rec[12]

'''

kursevi = ["python", "ios", "design"]

#unos kursa
#provera da li postoji u listi kursevi (in)
# append ako ne postoji 
#while true
#svaki put nakon unosa ili poruke ispisati listu kurseva


while True:
    zeljeni_kurs = input("Unesite rec ")

    if zeljeni_kurs in kursevi: 
        print("Vec postoji")
    else:
        kursevi.append(zeljeni_kurs)
    print(kursevi)

# in proverava da  li se nesto na  lazi u sekvenci