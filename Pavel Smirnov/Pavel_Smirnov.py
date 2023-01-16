

    from random import randint


    print("arvuti mõistab numbrit 1-10 ja sina üritab seda ära arvata.")
    a=randint(1,10)
    vastus=int(input("mis arv on mõistanud arvutit?: "))
    k=p=1
    while vastus!=a:
        print("ära sa ei avanud ära, proovi uuesti!: ")
        vastus=int(input("sisesta vastus: "))
        k+=1
        p+=1
        if k>2:
            print("püüdlused on lõppenud")
            b=input("kas sa tahad proovi veel kord?")
            if b.upper()=="JÄH":
                k=1
                continue
            else:
                break
     while True:
         print("palju õnne, sa arvasid ära!")
         break
     def new_func():
     print()

new_func()

from math import *
from random import *
#16/01/23

katsed=0
answer=""
while answer!="komm":
    answer=input("tahan kommi!")
    katsed+=1
print(f"katsed: (katsed)")
print()