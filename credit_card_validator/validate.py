import string


def isNumberString(s):
    length = len(s)
    for ch in s:
        if (ch < '0' or ch > '9'):
            return False
    return True


def validate():

    print("\n\t-->This program uses the Luhn Algorigthm to validate a Credit Card number.")
    print("\t-->You can enter 'exit' anytime to quit.\n")

    while True:

        ccNumber = input("Please enter a Credit Card number to validate: ")

        if (ccNumber == "exit"):
            break

        if (not isNumberString(ccNumber)):
            print("Bad input! try again")
            continue

        length = len(ccNumber)
        doubleEvenSum = 0

        # Step 1 is to double every second digit, starting from the right. If it
        # results in a two digit number, add both the digits to obtain a single
        # digit number. Finally, sum all the answers to obtain 'doubleEvenSum'.

        for i in range(length - 2, -1, -2):

            dbl = (ord(ccNumber[i]) - 48) * 2
            # dbl = (dbl / 10) + (dbl % 10) if dbl > 9 else dbl

            if (dbl > 9):
                dbl = (dbl / 10) + (dbl % 10)

            doubleEvenSum += dbl

        # print("doubleEvenSum", doubleEvenSum)
        # Step 2 is to add every odd placed digit from the right to the value
        # 'doubleEvenSum'.

        for i in range(length - 1, -1, -2):
            doubleEvenSum += (ord(ccNumber[i]) - 48)

        # Step 3 is to check if the final 'doubleEvenSum' is a multiple of 10.
        # If yes, it is a valid CC number. Otherwise, not .

        if (doubleEvenSum % 10 == 0):
            print("Valid Credit Card Number :)")
        else:
            print("inValid Credit Card Number :(")


validate()
