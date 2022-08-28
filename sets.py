

input_1 = set(input("Type some letters or digit: "))
input_2 = set(input("Try to type somthing again, f.e. digits and letters: "))


print([x for x in set(input_1) & set(input_2) if x.isalpha()])
print([x for x in set(input_1).symmetric_difference(input_2) if x.isdigit()])


set_1 = {1, 5, 7, 9, 'cool', 'true', 'this is updated'}
set_2 = {2, 4, 6, 10}
set_1.update(set_2)
print(set_1)


set_3 = {'hi', 6, 2, 4, 6, 10, 11, 'hello set', 'number'}
set_4 = {2, 4, 6, 'hello set', 7, 8, 9, 10, 'number'}
set_5 = {0, 1, 2, 3, 'hello set', 2, 4, 8, 11, 'number'}
set_6 = set_3 | set_4 | set_5
print(f'{set_6 = }')

intersection = set_3 & set_4 & set_5
print(f'{intersection = }')

difference = set_3 - set_4 - set_5
print(f'{difference = }')

sym_difference = set_3 ^ set_4 ^ set_5
print(f'{sym_difference = }')