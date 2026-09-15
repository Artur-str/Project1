print('Введите год своего дня рождения:')
a=int(input())
print('Введите текущий год:')
b=int(input())
print('Введите месяц вашего дня рождения:')
c=int(input())
print('Введите текущий месяц:')
d=int(input())
if d>c:
    print(b-a)
else:
    print((b-a)-1)

a=3
b=4
c=5
p=(a+b+c)/2
s=((p*(p-a)*(p-b)*(p-c)))**0.5
print(s)
