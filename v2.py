# калькулятор v1
from colorama import init
from colorama import Fore, Back, Style

init()
print( Fore.BLACK )
print( Back.GREEN )

what = input("что делаем? (+, -, *, /): ")

print( Back.CYAN )

a = float(input("Введи первое число: "))
b = float(input("Введи первое число: "))
print( Back.YELLOW )

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