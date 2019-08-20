from random import randint
from time import perf_counter
czasy_wstaw=[]
czasy_bomb=[]
for p in range(0,200):
    def losuj(ile):
        tab=[]

        for i in range(0,ile):
            tab.append(randint(-1000,1000))
        return tab
    tab=losuj(500)
    tab1=tab[:]
   
    z = len(tab)


    start_wstaw=perf_counter()
    for x in range(z):
        min=x
        for y in range (x+1, z):
             if tab[min]>tab[y]:
                 min=y
        tab[x], tab[min]=tab[min], tab[x]           
    koniec_wstaw=perf_counter()

    czas_wstaw=koniec_wstaw-start_wstaw
    czasy_wstaw.append(czas_wstaw)



    start_bomb=perf_counter()

    for i in range(z):
        for j in range(i+1,z):
            if tab1[i]>tab1[j]:
               tab1[i], tab1[j]=tab1[j], tab1[i]

    koniec_bomb=perf_counter()

    czas_bomb=koniec_bomb-start_bomb
    czasy_bomb.append(czas_bomb)
         

sr_wstaw=sum(czasy_wstaw)/len(czasy_wstaw)
sr_bomb=sum(czasy_bomb)/len(czasy_bomb)
print("średni czas sortowania przez wstawianie",sr_wstaw)
print("średni czas sortowania babelkowego",sr_bomb)
