people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    #Your code go here:
    new_lista=[]
    for i in people:
        if i!=person_name:
            new_lista.append(i)
    return new_lista        
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))