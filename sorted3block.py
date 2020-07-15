def sorted2(data, key=lambda x: -x):#принимает список и ключ, который по умолчанию сортирует в обратном порядке
    sorted_data = []
    for element in data:#применяем сортировку по ключу к каждому подсписку
        sorted_data.append(sorted(element, key=key))
    return sorted(sorted_data, key=lambda i: i[-1])#применяем сортировку к списку по последним элементам подсписков

data = [[6, 5, 4], [3, 2], [1]]
key = lambda x: x #ключ сортировка
print(sorted2(data, key=key))
