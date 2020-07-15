def depth(key):
    global tree
    if tree[key] in tree:  # проверка является ли отец чьим-то сыном
        depth(tree[key])
    global height
    height[key] = 1 + height[tree[key]]  #при возврате по рекурсии повышаем глубину, глубина родословной сына на 1 больше глубины родословной отца
    return

tree = {}  # словарь принимающий сына и отсылающий к отцу
height = {}  # словай принимающий имя и отсылающий к глубине его родословной
for i in range(int(input()) - 1):  # заполнение словарей
    son, father = input().split()
    tree[son] = father
    height[father] = 0  # заполнение нулями, для избежания ошибки типа
for key in tree:  # применение вычисления глубины к каждому имени
    depth(key)

for i in sorted(height):  # вывод через сортировку
    print(i, height[i])
