def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


from art import logo

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}


def calculator():
    print(logo)

    num1 = float(input("Enter the first number:"))
    should_continue = True
    while should_continue:

        operation_symbol = input(
            "Which operation would you like to use, type, '+' or '-' or '*' or '/' "
        )
        num2 = float(input("Enter the next number:"))
        operation_function = operations[operation_symbol]
        answer = operation_function(num1, num2)
        print(f" {num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Would you like to continue with {answer}? Type 'Y' for yes and 'N' for new calculation: "
        ) == "Y":
            num1 = answer
        else:
            should_continue = False
            calculator()


calculator()
