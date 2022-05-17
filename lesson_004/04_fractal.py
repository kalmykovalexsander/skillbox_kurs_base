# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с углом рисования равным углу ветви,
#   длиной ветви меньшей чем длина ветви с коэффициентом 0.75

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

sd.resolution = (1200, 800)


def draw_branches(point, angle, length=100):
    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()

    next_point = vector.end_point
    delta = 30
    length *= 0.75

    next_angle = angle - delta
    draw_branches(next_point, next_angle, length)

    next_angle = angle + delta
    draw_branches(next_point, next_angle, length)


root_point = sd.get_point(1000, 30)
draw_branches(point=root_point, angle=90, length=100)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()


def draw_branches(point, angle, length=100):
    if length < 10:
        return

    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()

    next_point = vector.end_point

    delta = 30
    delta_deviation = delta * 0.4
    delta += sd.random_number(-delta_deviation, delta_deviation)

    length = length * 0.75
    length_deviation = round(length * 0.2)
    length += sd.random_number(0, length_deviation)

    next_angle = round(angle + delta)
    draw_branches(next_point, next_angle, length)

    next_angle = round(angle - delta)
    draw_branches(next_point, next_angle, length)


root_point = sd.get_point(500, 30)
draw_branches(point=root_point, angle=90, length=100)

sd.pause()