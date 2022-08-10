

input_data = input("Enter your data ")
digits = []
spaces = []
vowels = []

for index, letter in enumerate(input_data):
    if letter == " ":
        print(f"space index: {index}")

    if letter >= 'A' and letter <= 'Z':
        print(letter, 'big')

    if letter in "qeuio" or letter in "QEUIO":
        vowels.append(letter)


    try:
        if letter.isdigit():
            if input_data[index + 1].isdigit() and input_data[index + 2].isdigit():
                digits.append(input_data[index])
                digits.append(input_data[index + 1])
                digits.append(input_data[index + 2])
                print("Found 3 digits in raw")
                break
    except IndexError as error:
        print(f"{error}")







