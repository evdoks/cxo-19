def sqr_root(number, number_iters = 500):
	if number > 0:
		a = float(number) # number to get square root of
		for i in range(number_iters): # iteration number
			number = 0.5 * (number + a / number) # update
			# x_(n+1) = 0.5 * (x_n +a / x_n)
	elif number == 0:
		number = 0
	if number < 0:
		print("Cannot extract square root from a negative number.")
		exit()
	return number

def quadratic_eq(a, b, c):
	d = b**2 - 4*a*c

	if d >= 0:
		num_roots = 2
		
		sqrt_d = sqr_root(d)

		x1 = (((-b) + sqrt_d)/(2*a))     
		x2 = (((-b) - sqrt_d)/(2*a))
	else:
		x1 = None
		x2 = None
	return x1, x2

