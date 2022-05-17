# -*- coding: utf-8 -*-

import simple_draw as sd

smile_size = 40
smile_color = sd.COLOR_YELLOW
oculus_color = sd.COLOR_WHITE
beard_color = sd.COLOR_BLACK

eyeball_radius = round(smile_size * 0.3)
eye_radius = round(smile_size * 0.1)
oculus_radius = eyeball_radius + 1


def blink_eye(left_eye_point, right_eye_point, blink_time=0):

    if right_eye_point:
        sd.circle(center_position=right_eye_point, radius=eyeball_radius, color=smile_color, width=0)
        sd.circle(center_position=right_eye_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)
        sd.sleep(blink_time)

    if left_eye_point:
        sd.circle(center_position=left_eye_point, radius=eyeball_radius, color=smile_color, width=0)
        sd.circle(center_position=left_eye_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)


def draw_smile(x, y, game_tick=0):

    # рисуем тело
    body_list_point = (sd.get_point(x - smile_size*1.4, y - smile_size*1.75),
                       sd.get_point(x + smile_size*1.4, y - smile_size*1.75),
                       sd.get_point(x+smile_size//2, y-smile_size//2),
                       sd.get_point(x-smile_size//2, y-smile_size//2))

    sd.polygon(body_list_point, sd.COLOR_DARK_PURPLE, width=0)

    # рисуем лицо
    face_point = sd.get_point(x=x, y=y)
    sd.circle(center_position=face_point, radius=smile_size, color=smile_color, width=0)

    # рисуем глаза
    oculus_distance = eyeball_radius * 1.3
    right_oculus_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_oculus_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)

    sd.circle(center_position=right_oculus_point, radius=eyeball_radius, color=oculus_color, width=0)
    sd.circle(center_position=left_oculus_point, radius=eyeball_radius, color=oculus_color, width=0)

    right_eye_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_eye_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)

    sd.circle(center_position=right_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)
    sd.circle(center_position=left_eye_point, radius=eye_radius, color=sd.COLOR_BLACK, width=0)

    # рисуем очки
    sd.circle(center_position=right_oculus_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)
    sd.circle(center_position=left_oculus_point, radius=oculus_radius, color=sd.COLOR_BLACK, width=1)

    # рисуем душки очков
    # центральная часть
    point1 = sd.get_point(round(right_oculus_point.x - smile_size / 4), right_oculus_point.y)
    point2 = sd.get_point(round(left_oculus_point.x + smile_size / 4), left_oculus_point.y)
    sd.line(point1, point2, sd.COLOR_DARK_ORANGE, width=3)

    # левая часть
    point1 = sd.get_point(left_oculus_point.x-oculus_radius, left_oculus_point.y)
    point2 = sd.get_point(left_oculus_point.x-oculus_radius*2, left_oculus_point.y)
    sd.line(point1, point2, sd.COLOR_DARK_ORANGE, width=3)

    # правая часть
    point1 = sd.get_point(right_oculus_point.x+oculus_radius, right_oculus_point.y)
    point2 = sd.get_point(right_oculus_point.x+oculus_radius*2, right_oculus_point.y)
    sd.line(point1, point2, sd.COLOR_DARK_ORANGE, width=3)

    # рисуем бороду
    step = smile_size // 10
    beard_step = 0
    beard_y_pos = y
    beard_length = (smile_size - round(smile_size * (3 / 7)))

    for i in range(x - smile_size - 1, x + smile_size + 1, step):

        if i < x:
            beard_step += step
        else:
            beard_step -= step

        point_start = sd.get_point(i, beard_y_pos)
        point_end = sd.get_point(i, beard_y_pos-beard_length-beard_step)
        sd.line(point_start, point_end, beard_color, width=step)

    # рисуем улыбку
    step = smile_size // 10
    smile_step = smile_size // 10
    smile_y_pos = y-5
    smile_length = (smile_size - round(smile_size * (6 / 7)))

    for i in range(x-smile_length-1, x+smile_length+1, step):

        if i < x:
            smile_step += step
        else:
            smile_step -= step

        point_start = sd.get_point(i, smile_y_pos-smile_length)
        point_end = sd.get_point(i, smile_y_pos-smile_length-smile_step)
        sd.line(point_start, point_end, sd.COLOR_RED, width=step)

    # рисуем волосы
    sd.vector(sd.get_point(x - 30, y + smile_size - 3), 0, 60, sd.COLOR_BLACK, width=5)
    sd.vector(sd.get_point(x - 30, y + smile_size - 7), 10, 60, sd.COLOR_BLACK, width=5)
    sd.vector(sd.get_point(x - 30, y + smile_size + 7), -10, 60, sd.COLOR_BLACK, width=5)

    if game_tick % 40 <= 3:
        blink_eye(left_eye_point, right_eye_point)


if __name__ == '__main__':

    tick = 0
    while True:

        tick += 1
        start_point = sd.get_point(300, 300)
        draw_smile(start_point.x, start_point.y, tick)
        sd.sleep(0.07)
        if tick >= 60:
            tick = 0

        if sd.user_want_exit():
            break