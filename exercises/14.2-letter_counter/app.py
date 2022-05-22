par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
def count(par):
    for i in par:
        i = i.lower()
        print (counts.get(i))
        if i !=" ":
            if counts.get(i)==None :
                counts[i]=1
            else:
                counts[i]=counts[i]+1

print(count(par))
print(counts)

