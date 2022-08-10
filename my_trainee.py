# number = 0
# while number < 30:
#     print('Stop calculation')
#     number += 1
# print(number)

# number = 0
# while number < 30:
#     print('Stop calculation')
#     number += 1
#     break
# print(number)

# number = 0
# while True:
#     print('Stop calculation')

# number = 0
# while True:
#     number +=1
#     if number > 5:
#         break
#     print('Hello Ukraine')
# print(number)

# number = 1
# while number < 10:
#     if number == 3:
#         print('opa')
#         number += 1
#         continue
#     print("got")
#     number += 1
# print(number)

#
# number = 10
# while number > 6: number -= 1
# print(number)


# a = 1
# n = int(input())
# while a <= n + 1:
#     print('Hello')
#     a += 3

#
# number = 20
# while number >= 10:
#     print('OK')
#     number -= 1
#     print(number)

# number = int(input())
# while number!= 0:
#     print('Enter data again')
#     number = int(input())

# guess = input()
# password = 'qwerty'
# count = 0
# while guess != password:
#     count += 1
#     print('Enter your log again')
#     guess = input()
# print("you ve spent", count , "attempts")


# a = [1,2,3,4,5] * 3
# # print(a)
# # a.remove(3)
# print(a)
# while 3 in a:
#     a.remove(3)
# print(a)


# # ПЕРЕМЕННАЯ СО СТРОКАМИ
#
# s = 'HeLLo HiLlel school!!. ThIS is - the fifTh homeWoRk 10.08.22'
# # print(s[-1])
# # print(s[3:])
# while len(s) > 0:
#     # print(s[0]) #s[1:]) чтоб был срез при удалении каждоый буквы
#     letter = s[0]
#     if letter >= 'A' and letter <= 'Z':
#         print(letter, 'big')
#     # elif letter >= 'a' and letter <= 'z':
#     #     print(letter, 'small')
#
#     # elif letter.isdigit():
#     #     print(letter, 'digit')
#     # else:
#     #     print('знаки препинания')
#     s = s[1:]
#
#
#
#
#
#
# input_data = input("Enter your data ")
# digits = []
# spaces = []
# vowels = []
#
# for index, letter in enumerate(input_data):
#     if letter == " ":
#         print(f"space index: {index}")
#
#     if letter >= 'A' and letter <= 'Z':
#         print(letter, 'big')
#
#     if letter in "oeau" or letter in "OEAU":
#         print("vowel")
#
#
#     try:
#         if letter.isdigit():
#             if input_data[index + 1].isdigit() and input_data[index + 2].isdigit():
#                 digits.append(input_data[index])
#                 digits.append(input_data[index + 1])
#                 digits.append(input_data[index + 2])
#                 print("Found 3 digits in raw")
#                 break
#     except IndexError as error:
#         print(f"{error}")





