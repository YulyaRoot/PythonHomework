#Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
#Программа должна возвращать сумму и произведение* дробей. 
#Для проверки своего кода используйте модуль fractions.

import fractions

a = int(input("a: "))
b = int(input("b: "))
a1 = int(input("a1: "))
b1 = int(input("b1: "))

f1 = fractions.Fraction(a, b)
print(f1)
f2 = fractions.Fraction(a1, b1)
print(f2)

print('Сумма дробей', f1 + f2)
print('Произведение дробей', f1 * f2) 