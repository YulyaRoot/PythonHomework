#Напишите программу, которая получает целое число и возвращает его 
#шестнадцатеричное строковое представление. 
#Функцию hex используйте для проверки своего результата.

number = int(input("Введите число: "))
result = ""
print(hex(number))

while number > 0:
    double_num = number % 16
    result = str(double_num) + result
    number = number // 16
print(result)    

