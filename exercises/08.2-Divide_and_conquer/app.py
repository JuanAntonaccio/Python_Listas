list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(lista):
    odd=[]
    even=[]
    for i in lista:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    nueva=[odd,even]
    return nueva          


print(merge_two_list(list_of_numbers))

