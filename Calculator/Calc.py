print('''
                    BASIC CALCULATOR
''')

number_1 = int(input('Enter Operand 1: '))
number_2 = int(input('Enter Operand 2: '))

print('-' * 30)  # Separation

print("The value of", number_1, "+", number_2, "is: ", number_1 + number_2)
print("The value of", number_1, "-", number_2, "is: ", number_1 - number_2)
print("The value of", number_1, "*", number_2, "is: ", number_1 * number_2)
print("The value of", number_1, "/", number_2, "is: ", number_1 / number_2)
print("The value of", number_1, "//", number_2, "is: ", number_1 // number_2)
print("The value of", number_1, "**", number_2, "is: ", number_1 ** number_2)
