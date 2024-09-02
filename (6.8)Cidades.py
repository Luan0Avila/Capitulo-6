cities = {'araçariguama': {
            'country' : 'Brazil',
            'state' : 'são Paulo'
},
  'são roque' : {
      'country': 'Brazil',
    'state': 'são Paulo'
},
  'rio de janeiro' : {
  'country': 'Brazil',
    'state': 'rio de janeiro'
},
          }

for citie, citie_info, in cities.items():
    country = citie_info['country']
    state = citie_info['state']
    print (f"A cidade de {citie} fica no estado de {state}, e no pais {country}")