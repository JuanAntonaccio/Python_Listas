#Import random

#Create the function below:

def matrixBuilder(num):
    matriz=[]
    for i in range(num):
        matriz.append([1]*num)
    return matriz        

dato=matrixBuilder(4)
print(dato)