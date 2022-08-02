#Виправ помилку у порівнянні 3 ! 5
x = 3
y = 5
print(bool(x == y))
print(bool(x > y))
print(bool(x < y))
print(bool(x != y))
print(bool(x >= y))
print(bool(x <= y))

# Наведи усі комбінації порівнянь для 5 _ 5, при яких результат буде True
c = 5
d = 5
print(bool(c==d),(c>=d),(c<=d),(c<=d and c>=d),(c>=d or c>=d))

#Наведи 5 комбінацій з логічних операторів (or, and, not) та дужок,
# так щоб результат у виразі True _ True _ False був True
is_true = True or True or False
print(f"{is_true = }")
is_true_1 = (True or True) or False
print(f"{is_true_1 = } ")
is_true_2 = (True and True) or False
print(f"{is_true_2 = }")
is_true_3 = (True or False) and True
print(f"{is_true_3 = }")
is_true_4 = (True or True) == (not False)
print(f"{is_true_4 = }")

# Порівняй логічні значення None та 7
non_object = None
number = 7

logical_1 = bool(non_object)
logical_2 = bool(number)
print(f"{logical_1=},{logical_2=}")

result = non_object or number
result_1 = (non_object) = (not number)
result_2 = non_object and number
print(f"{result=},{result_1=},{result_2=}")

#Порівняй логічні значення пустої строки та виразу 10 - 1

result_3 = bool(10-1)
result_4 = bool("")
print(f"{result_3 = }  ,{result_4 = }")
comparison_1 = result_3 or result_4
comparison_2 = result_3 and result_4
comparison_3 = (result_3) = (not result_4)
print(f"{comparison_1 = }, {comparison_2 = }, {comparison_3 = }")

