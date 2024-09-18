from functools import reduce


result = reduce((lambda x, y: (x + '  ' + y).lower()), ['Privet', 'mir'] )
print(result)

# нахождение четных элементов списка и формирования нового списка из этих элементов
my_lst = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(filter(lambda x: (x%2 == 0) , my_lst))
print(new_list)

# удвоение всех элементов списка
current_list = [1, 3, 4, 6, 10, 11, 15, 12, 14]
new_list = list(map(lambda x: x*2 , current_list))
print(new_list)