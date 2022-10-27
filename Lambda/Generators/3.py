"""
Напишите генератор выводящий все числа делящиеся на 11 в диапазоне от 0 до 100
"""

obj = (i for i in range(100) if i%11 == 0)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))