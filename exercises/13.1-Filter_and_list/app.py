
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:
def funcion(x):
    if x[0]=="R" or x[0]=="r":
        return x
resulting_names=list(filter(funcion,all_names))

print(resulting_names)




