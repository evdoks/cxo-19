from my_math.quadratic import quadratic_eq

if __name__ == '__main__':
	print("quadratic function : (a * x^2) + b*x + c")
	a = float(input("a: "))
	b = float(input("b: "))
	c = float(input("c: "))
	
	x1, x2 = quadratic_eq(a, b, c)
	
	print("Root 1:", x1)
	print("Root 2:", x2)	