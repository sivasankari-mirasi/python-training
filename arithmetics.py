print("Arithmetic Operations ")
number1 = raw_input("Enter first number ")
number2 = raw_input("Enter second number ")


if (number1.isdigit() and number2.isdigit()):
    number1 = int(number1)
    number2 = int(number2)

    ans = number1 + number2
    print "Addition of numbers      : ", ans
    ans = number1 - number2
    print "Subraction of numbers    : ", ans
    ans = number1 * number2
    print "Multiplication of numbers: ", ans
    ans = number1 / number2
    print "Division of numbers      : ", ans
else:
    print("Entered numbers are not integers")

