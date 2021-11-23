# калькулятор v1
what = input("что делаем? (+, -, *, /): ")

a = float(input("Введи первое число: "))
b = float(input("Введи первое число: "))

if what == "+":
	c = a + b
	print("Результат: " + str(c))
elif what == "-":
	c = a - b
	print("Результат: " + str(c))
elif what == "*":
	c = a * b
	print("Результат: " + str(c))
elif what == "/":
	c = a / b
	print("Результат: " + str(c))
else:
	print("выбрана не верная операция")
	input()