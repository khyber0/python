w = input("введите знак (+, -, *, /): ")

a = float(input("введитие первое число: "))
b = float(input("введитие первое число: "))

if w == "+":
	c = a + b
	print("Результат: " + str(c))
elif w == "-":
	c = a - b
	print("Результат: " + str(c))
elif w == "*":
	c = a * b
	print("Результат: " + str(c))
elif w == "/":
	c = a / b
	print("Результат: " + str(c))
else:
	print("ERROR")