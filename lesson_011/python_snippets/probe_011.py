from collections import OrderedDict

my_pets = OrderedDict()
my_pets['собака'] = 'Жучка'
my_pets['мышка'] = 'Норушка'
my_pets['кошка'] = 'Мурка'
my_pets['попугай'] = 'Кеша'
my_pets['рыбка'] = 'Геннадий'
my_pets['таракан'] = 'Виссегауд'
my_pets['кролик'] = 'Савелий'
print(my_pets)
for k, v in my_pets.items():
    print(k, v)