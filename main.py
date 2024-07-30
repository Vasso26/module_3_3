def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params(3)
print_params(3, 5)
print_params()
print_params(b = 25)
print_params([1, 2, 3])

values_list = [False, 5, 'строка']
values_dict = {'a': True, 'b': 25, 'c': "строка"}

print()
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32 , 'строка']

print()
print_params(*values_list_2, 42)