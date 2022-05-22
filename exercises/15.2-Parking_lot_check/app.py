parking_state = [
  [1,1,1],
  [0,0,0],
  [1,1,2]
]

#Your code go here:
def get_parking_lot():
  dispo=0
  ocupados=0
  
  for i in range(len(parking_state)):
    for j in range(len(parking_state[i])):
      if parking_state[i][j]==1:
        ocupados+=1
      elif parking_state[i][j]==0:
        dispo+=1
  dictio={}
  dictio['total_slots']=ocupados+dispo
  dictio['available_slots']=dispo
  dictio['occupied_slots']=ocupados
  return dictio

print(get_parking_lot())         
