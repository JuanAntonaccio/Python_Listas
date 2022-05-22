import datetime


people = [
	{ "name": 'Joe', "birthDate": datetime.datetime(1986,10,24) },
	{ "name": 'Bob', "birthDate": datetime.datetime(1975,5,24) },
	{ "name": 'Erika', "birthDate": datetime.datetime(1989,6,12) },
	{ "name": 'Dylan', "birthDate": datetime.datetime(1999,12,14) },
	{ "name": 'Steve', "birthDate": datetime.datetime(2003,4,24) }
]


def calculateAge(birthDate):
    today = datetime.date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age


		
def funcion(name):
	for i in people:
		for k,v in i.items():
			#print(k,v)
			if k=="name":
				if name in v:
					edad = calculateAge(i.get(birthDate))
					texto=f'Hello, my name is {name} and I am {edad} years old'
					print(texto)
					return texto
		
		


person = lambda name: funcion(name)
name_list = list(map(funcion , people))
print(name_list)

