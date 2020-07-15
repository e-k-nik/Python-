import pygame as pg

pg.init()  # инициализация программы
w = int(input())  # размер окна
n = int(input())  # количество клеток в строке
v = w // n  # размер одной клетки
win = pg.display.set_mode((w, w))  # параметры окна программы

for i in range(n ** 2):  # перебор клеток
    if ((i % n) + (i // n)) % 2:  # формула вычисления координат клетки
        pg.draw.rect(win, (255, 255, 255),
                         (v * (i % n), v * (i // n), v, v))  # закрашивание клеток с нечётными координатоми белым цветом
pg.display.update()  # обновление окна

while True:  # инициализация выхода через проверку нажтия на крестик в углу окна
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
pg.quit()
