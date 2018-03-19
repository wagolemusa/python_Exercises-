from enum import Enum
class country(Enum):
     Afghanian = 93
     Albania   = 355
     Algeria   = 123
     Andorra   = 375
     Angola    = 243

print ('\nMember name: {}'.format(country.Albania.name))
print ('Member value: {}'.format(country.Albania.value))
