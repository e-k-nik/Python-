import pygame as pg

pg.init()
win = pg.display.set_mode((300, 300))
# начальные координаты и размер
x = 0
y = 0
w = 50

# начальное окна
win.fill((0, 0, 0))
pg.draw.rect(win, (255, 0, 0), (x, y, w, w))
pg.display.update()

while True:
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:  # проверка нажатия мыши
            if x < event.pos[0] < x + w and y < event.pos[1] < y + w:  #проверка попадания курсора в квадрат при нажатии
                # запоминание точки захвата
                dx = event.pos[0] - x
                dy = event.pos[1] - y
                hit = 1  # индикатор попадания при нажатии
            else:
                hit = 0  # промах
        press = pg.mouse.get_pressed()  # удержания кнопки мыши
        if press[0] and hit:  # проветка удержания левой кнопки и проверка попадания в квадрат
            # перерисовка квадрата в новые координаты и обновление экрана
            x, y = event.pos[0] - dx, event.pos[1] - dy
            win.fill((0, 0, 0))
            pg.draw.rect(win, (255, 0, 0), (x, y, w, w))
            pg.display.update()
            #не зависит от скорости перемещения мыши, так как проверка попадания в облость квадрата производится только 1 раз при нажатии

        if event.type == pg.QUIT:  # выход через крестик
            exit()
