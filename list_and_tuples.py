# Створи послідовність інструкцій, яка отримує рядок від користувача та друкує кожне третє слово з цього рядка.
# Цикли не використовувати
while 1 == 1:
    s = input("")
    l = s.split()
    print(l[2::3] , type(l))

# Створи генератор списка
# Вхідний список [1, 2.1, "f", "2", 3, "1", 18, "df"]
# Вихідний список [1, 2.1, -1, '6', 9, '3', 18, -1]

my_list = [1, 2.1, "f", "2", 3, "1", 18, "df"]
my_list = [ i if type(i) == float
          else i if (type(i) == int and i % 2 == 0)
          else i ** 2 if (type(i) == int and i % 2 != 0)
          else (str(int(i) * 3)) if (i.isdigit() and type(i) == str)
          else -1 for i in my_list ]
print(my_list)