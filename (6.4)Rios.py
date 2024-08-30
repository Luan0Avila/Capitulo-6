rivers = {'Nilo' : 'Egito',
          'Amazonas' : 'Brasil',
          'Ranges' : 'Índia'}

print ('Os rios são:\n')

for river in rivers.keys():
    print (river)

print ('\nOs paises são:\n')

for country in rivers.values():
    print (country)


for k, v in rivers.items():
    print (f"\nO {k} atravessa o(a) {v}")