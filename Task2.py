"""
������� sorted ��������� � �������� ��������������� ��������� key(������ �������� ������������).
� ������� lambda-������� ������������ ���� ������ �������� �� ������
Напишите программу которая будет спрашивать пользователя ввод имени пока пользователь не введет off.
Программа должна используя lambda-функцию добавлять к каждому имени надпись "гений".
"""
grades = [{'name': 'Jennifer', 'final': 95},
     {'name': 'David', 'final': 92},
    {'name': 'Aaron', 'final': 98}]

grades = [{'name': 'Jennifer', 'final': 95}, {'name': 'David', 'final': 92}, {'name': 'Aaron', 'final': 98}]
print(sorted(grades, key=lambda x: x['name']))