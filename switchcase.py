def addition(num1, num2):
  num1 += num2
  return num1
def subtraction(num1, num2):
  num1 -= num2
  return num1
def multiplication(num1, num2):
  num1 *= num2
  return num1
def division(num1, num2):
  num1 /= num2
  return num1
def module(num1, num2):
  num1 %= num2
  return num1
def default(num1, num2):
  return "Неправильное действие"
switcher = {
    1: addition,
    2: subtraction,
    3: multiplication,
    4: division,
    5: module
}
def switch(operation, num1, num2):
  return switcher.get(operation, default)(num1, num2)
print('''Вы можете выполнить операцию
1. Сложение
2. Вычитание
3. Умножение
4. Деление
5. Модуль ''')

choice = int(input("Выберите операцию из 1,2,3,4,5: "))
num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второй номер: "))
print (switch(choice, num1, num2))
