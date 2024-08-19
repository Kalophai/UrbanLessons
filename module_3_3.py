def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b = 25)
print_params(c = [1,2,3])
##########
values_list = ['Бараш', 999, [1, 2, 3]]
values_dict = {'a': [1, 2, 3], 'b': 'Дмитрий', 'c': 999}
print_params(*values_list)
print_params(**values_dict)
##########
values_list_2 = ['Тифон', [4, 5, 6]]
print_params(*values_list_2, 42)