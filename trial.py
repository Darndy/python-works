def get_number(prompt):
    count = input(prompt)
    while True:
        try:
            count = int(count)
            break
        except:
            count = input("please enter a valid number: ")
    return count
number1 = get_number("Enter first number:")
number2 = get_number("Enter second number:")
print(number1 + number2)