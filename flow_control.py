operand_1 = (input("Enter first data "))
operand_2 = (input("What calculation you like to do? "))
operand_3 = (input("Enter your second data "))

operand_1 = int(operand_1) if operand_1.isdigit() else float(operand_1)
operand_3 = int(operand_3) if operand_3.isdigit() else float(operand_3)

if operand_2 == '-':
    print(operand_1 - operand_3)
elif operand_2 == '+':
    print(operand_1 + operand_3)
elif operand_2 == '/':
    print(operand_1/operand_3)
elif operand_2 == '*':
    print(operand_1 * operand_3)
else:
    print("Error")
