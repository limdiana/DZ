"""
Напишите генератор выводящий все символы строки на печать, но только в том случае, если они являются буквами (остальные игнорируются).
"""
def e(a):
    for i in a:
        if i.isalpha():
            yield i
w = e('ajb#bj0 0')
for i in w:
    print(w)