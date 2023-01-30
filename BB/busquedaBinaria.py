from math import floor #metodo que te ayudara a redondear el promedio hacia abajo

def binariSearch(primos,target):
    min=0
    max=len(primos)-1
    guess=int()
    while True:
        if min>max:
            print("target no esta en el array")
            return -1
            pass

        guess=floor((min+max)/2)

        if primos[guess]==target:
            print("numero encontrado")
            print(primos[guess]," | ",target,": ",primos)
            return guess
            pass
        elif primos[guess]<target:
            min=guess+1
            pass
        else:
            max=guess-1
            pass
        pass
    return 0

primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
print(binariSearch(primos,7))