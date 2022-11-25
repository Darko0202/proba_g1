# for sledeci in ["Mile", "Jovana", "Petar", "Marija", 1, 5, 7, 9]:
#     print("Hello", sledeci) 

# print("For petlja se zavrsila")



# for brojac in range(1, 101, 2):                                          # 1 - pocetak, 101 - kraj, 2 - broj uvecavanja
#     print("Hello...", brojac)

# print("*****Allowed years*****")
# for godine in range(2010, 2016):
#     print("Allowed year:", godine)           - Moj primer
# print("**************")

# pocetna_godina = 2000
# zavrsna_godina = 2020

# print("*****Allowed years*****")
# for godina in range(pocetna_godina, zavrsna_godina+1):
#     print(godina, end=", ")

# print("*****************") 
# zeljeni_broj = int(input("Unesite broj "))
# print("1\t2\t3")
# print("------------------")                     #tablica mnozenja


# for broj in range(1, zeljeni_broj+1):
#     print(broj *1, end="\t")
#     print(broj *2, end="\t")               #dinamicki menjanje brojeva od 1 do 6
#     print(broj *3)

# odstampaj samo parne brojeve iz opsega 1 do 100

# for broj in range(0, 101, 2):
#     print(broj)                                prvi primer

# for broj in range(1, 101):
#     if broj %2 == 0:             
#         print(broj)                            drugi primer
#     else:
#         print("Neparan broj")                 neparni brojevi


# for x in range(10):
#     print("Ovo je x:", x)
#     for y in range(10):
#         print("Ovo je y:", y)

'''
   # # # # # 
   # # # # # 
   # # # # # 
   # # # # #
'''
# vrednost = ". . ." if uslov else ". . ."
# for x in range(5):
#     for y in range(6):
#         print("*" if x == y else "#", end= " ")           -# i * u dijagonali
       
# #        # if x == y:
    
# #     #         print("*", end=" ")
# #     #     else: 
# #     #         print("#", end= " ")
#     print()

   
# visina = 10
# sirina = 10

# for x in range(visina):                      -trougao 
#     for y in range(sirina):
#             print("*", end="")
#     sirina +=1 
#     print()

# # # # # 
#       #
#       #
#       #
# # # # # 

x = 10
y = 5 

for x in range(10):
    for y in range(10):
        if x == 0 or x == 9 or y == 0 or y == 9:
            print("#", end=" ")
        # elif x == 5:
        #     print("A", end=" ")            - proveravamo gde se nalazi slovo "A"
        else:
            print(" ", end=" ")
    print()

