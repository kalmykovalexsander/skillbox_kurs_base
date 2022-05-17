#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}


def distance(x1, y1, x2, y2):
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return dist

for i in sites:
    for city in sites:
        print(sites[i], sites[city])
        # print(real)

# for city in sites:
#     print(sites[city])



print(len(sites))



# print(distances)
