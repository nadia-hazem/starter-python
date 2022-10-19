
def mySort(myList) :
    print("Ordre croissant")
    for i in range(len(myList)):                                #Pour inième dans la longueur de la liste
        for j in range(i + 1, len(myList)):                     #Pour jinième dans la longueur de la liste

            if myList[i] > myList[j]:                           #Condition : si i > j
                myList[i], myList[j] = myList[j], myList[i]     #inverser l'ordre
    print(myList)

def myDisplay (display) :
    print("Ordre de saisie")
    print(display)

s = [3, 66, 15, 33, 28, 45, 62, 14, 18]
d = [66, 46, 23, 15, 29, 31, 27, 12, 77]

mySort(s)          #Appel de la fonction
myDisplay(d)