chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    nueva=[]
    for i in list1:
        nueva.append(i)
    for i in list2:
        nueva.append(i)
    return nueva        
    
print(merge_list(chunk_one, chunk_two))
