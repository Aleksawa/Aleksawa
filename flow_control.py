print ("Exit from program press enter e ")

while True:
    num_1 = (input("Enter first data "))
    if num_1 == 'e':
        break
    calculation = (input("What calculation you like to do? "))
    num_2 = (input("Enter your second data "))



    num_1 = int(num_1) if num_1.isdigit() else float(num_1)
    num_2 = int(num_2) if num_2.isdigit() else float(num_2)

    if calculation == '-':
        print(num_1 - num_2, type(num_1 - num_2))
        continue

    elif calculation == '+':
        print(num_1 + num_2,  type(num_1 + num_2))
        continue

    elif calculation == '/':
        if num_2 == 0:
            print("ZeroDivisionError")
            continue

        else:
            answer = num_1 / num_2
        print(num_1/num_2,  type(num_1/num_2))
        continue

    elif calculation == '*':
        print(num_1 * num_2,  type(num_1 * num_2))
        continue
    else:
        print("Error")







# бесконечный цикл
# while True:
#     num_1 = (input("Enter first data "))
#     calculation = (input("What calculation you like to do? "))
#     num_2 = (input("Enter your second data "))
#
#     num_1 = int(num_1) if num_1.isdigit() else float(num_1)
#     num_2 = int(num_2) if num_2.isdigit() else float(num_2)
#
#     if calculation == '-':
#         print(num_1 - num_2, type(num_1 - num_2))
#         continue
#     elif calculation == '+':
#         print(num_1 + num_2,  type(num_1 + num_2))
#         continue
#     elif calculation == '/':
#         if num_2 == 0:
#             print("ZeroDivisionError")
#             continue
#         else:answer = num_1 / num_2
#         print(num_1/num_2,  type(num_1/num_2))
#         continue
#     elif calculation == '*':
#         print(num_1 * num_2,  type(num_1 * num_2))
#         continue
#     else:
#         print("Error")