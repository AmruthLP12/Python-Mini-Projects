def get_number(number):
    while True:
        operand = input("Number " + str(number) + ": ")
        try:
            return float(operand)

        except:
            print("Invalid Number!,try again")

operand = get_number(1)
operand2 = get_number(2)

operator = input("Operator (+, -, *, /): ")

result = 0
if operator == "+":
    result = operand + operand2
elif operator == "-":
    result = operand - operand2
elif operator == "*":
    result = operand * operand2
elif operator == "/":
    if operand2 != 0:
        result = operand / operand2
    else:
        print("Division by zero!")
else:
    print("Invalid Operator!")

print("Result: " + str(result))
