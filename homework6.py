my_dict = {'Artem': 2002,
           'Vanya': 1997,
           'Vasya': 2000,
           'Polina': 2001}
print(my_dict)
print(my_dict['Artem'])
print(my_dict.get('Musya'))
my_dict.update({'Gerasim': 1900,
                'Avdotya': 1434})
print(my_dict.pop('Avdotya'))
print(my_dict)

my_set = {3,0.5,True,3,0.5,True,3,0.5,True}
print(my_set)
my_set.add(7)
my_set.add(9)
my_set.discard(3)
print(my_set)