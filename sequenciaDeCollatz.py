def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 == 1:
        return 3 * number + 1


try:
    number = int(input("\n\tInforme o número: "))
    print("\n")
    print(number)
    while number != 1:
        number = collatz(number)
        print(number)
except ValueError:
    print('\n\tError: Invalid Value. You must enter an integer.')
