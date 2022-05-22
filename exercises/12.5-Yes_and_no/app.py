theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:
def funcion(x):
    dato='woko'
    if x==0:
        dato='wiki'
    return dato

resultado = list(map(funcion,theBools))
print(resultado)

