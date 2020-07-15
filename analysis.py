check = {}  # словарь принимающиц слово и отсылающий к числу его упоминаний
rever = {}  # словарь принимающиц число и отсылающий к словам упоминающимся это число раз
a = open('text.txt').read().split()  # считывание файла пословно
c = []  # финальный список
for i in a:  # заполнение первого словаря числами
    if i in check:
        check[i] += 1
    else:
        check[i] = 1

for i in check:  # переворот словаря(заполнение второго словаря списсками из слов)
    if check[i] in rever:
        rever[check[i]].append(i)
    else:
        rever[check[i]] = [i]

for i in reversed(sorted(rever)):  # сортировка по убыванию частоты, и в лексеграфическом порядке внутри одной частоты
    c.extend(sorted(rever[i]))
print(*c, sep="\n")