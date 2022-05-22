all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

#Your code go here:
def filter_colors(ele):
	for k,v in ele.items():
		if k=="sexy" and v:
			return ele

def funcion(ele):
	for k,v in ele.items():
		if k=="label":
			texto="<li>"+v+"</li>"
			return texto
nlista = list(filter(filter_colors,all_colors))
print(nlista)
nlista2 = list(map(funcion,nlista))
print(nlista2)