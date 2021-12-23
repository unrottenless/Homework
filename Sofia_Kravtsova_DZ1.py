# list
покупки = ['молоко', 'хлеб', 'яйца', 'колбаса', 'сыр']
print(покупки)
покупки.append('мука')
del покупки [3]
print(покупки)

#tuple
weapon = ('sword', 'bow', 'gun', 'disc', 'axe')
print(weapon[-1])

#dict
Mr = {'O':16.0, 'H':1.0, 'Cl':36.0, 'Na':23.0}
Mr ['O'] = 35.5
print(Mr)

#set
ноты = {'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'}
print(ноты)

# UPD8
avaible = list (weapon)
print(avaible)

avaible_2 = tuple (покупки)
print(type(avaible_2))

for notes in ноты:
    print(notes)

H2 = Mr.setdefault('H', 1.0)
print(H2*2)