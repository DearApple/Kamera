tablica = [8,2,16,23,1,0,4,9,-4,10,-9,5,2,-23,5,165,24,36,69,2]
tablica1 = [8,2,16,23,1,0,4,9,-4,10,-9,5,2,-23,5,165,24,36,69,2]
tab = [8,2,16,23,1,0,4,9,-4,10,-9,5,2,-23,5,165,24,36,69,2]



z = len(tablica)

for x in range(z):
    min=x
    for y in range (x+1, z):
         if tablica[min]>tablica[y]:
             min=y
    tablica[x], tablica[min]=tablica[min], tablica[x]           

print ("wstawianie", tablica)

for i in range(z):
    for j in range(i+1,z):
        if tablica1[i]>tablica1[j]:
            tablica1[i], tablica1[j]=tablica1[j], tablica1[i]

print ("bąbelkowe", tablica1)            





def quicksort(tab,h,r):

    
        if h<r:
            w = podziel(tab,h,r)
            quicksort(tab,h,w-1)
            quicksort(tab,w+1,r)

def podziel(tab,h,r):
        print(r)
        piv=round((h+(r-h))/2)
        wartosc=tab[piv]
        zmien(tab,piv,r)

        pozycja=0
        
        for g in range(r-h):
            if tab[g]<=wartosc:
                zmien(tab,g,pozycja)
                pozycja = pozycja + 1

        zmien(tab,pozycja,z)
        return pozycja


   
def zmien(tab,a,b):
  
    tab[a],tab[b]=tab[b], tab[a]
   

   
print(tab)
