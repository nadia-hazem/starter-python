def tri(*args) :
    myList = []                             #Crée liste vide myList
    
    for i in args :
        myList.append(i)                    #Ajoute le ième argument à la liste (à la suite)
    myList.sort()                           #'sort' fait un tri croissant par défaut
    print(myList)                           #Afficher liste croissante

tri(66, 46, 23, 15, 29, 31, 27, 12, 77)     #Appel de la fonction