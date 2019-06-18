number = float(input("Input a non-negative number: "))

number_iters = 500
if number > 0:
    a = float(number)
    for i in range(number_iters):
        number = 0.5 * (number + a / number)  # update
        # x_(n+1) = 0.5 * (x_n +a / x_n)
elif number == 0:
    number = 0
if number < 0:
    print("Cannot extract square root from a negative number.")
    exit()
print(number)
