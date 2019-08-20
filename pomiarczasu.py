from random import randint
from time import perf_counter
chronos=[]
saturn=[]
for p in range(0,200):
    def losuj(ile):
        dzikizgon=[]

        for i in range(0,ile):
            dzikizgon.append(randint(-1000,1000))
        return dzikizgon

    sauron=losuj(500)
    aragorn=sauron[:]
   
    z = len(sauron)


    druzyna_pierscienia=perf_counter()
    for x in range(z):
        min=x
        for y in range (x+1, z):
             if sauron[min]>sauron[y]:
                 min=y
        sauron[x], sauron[min]=sauron[min], sauron[x]           
    powrot_krola=perf_counter()

    tolkien=powrot_krola-druzyna_pierscienia
    chronos.append(tolkien)



    black_album=perf_counter()

    for i in range(z):
        for j in range(i+1,z):
            if aragorn[i]>aragorn[j]:
               aragorn[i], aragorn[j]=aragorn[j], aragorn[i]

    killem_all=perf_counter()

    mettalica=killem_all-black_album
    saturn.append(mettalica)
         

pitagoras=sum(chronos)/len(chronos)
gauss=sum(saturn)/len(saturn)
print("średni czas sortowania przez wstawianie",pitagoras)
print("średni czas sortowania babelkowego",gauss)
