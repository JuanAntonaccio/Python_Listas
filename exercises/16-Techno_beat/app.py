def lyrics_generator(lista):
    cont=0
    texto=""
    for i in lista:
        if i==0:
            texto=texto+"Boom "
        else:
            texto=texto+"Drop the base "
            cont+=1
            if cont==3:
                texto=texto+"!!!Break the base!!! "
                cont=0

    return texto
# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))