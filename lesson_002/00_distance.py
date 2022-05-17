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
    return round(dist, 2)


distances['Moscow_London'] = distance(*sites['Moscow'], *sites['London'])
distances['Moscow_Paris'] = distance(*sites['Moscow'], *sites['Paris'])
distances['Paris_London'] = distance(*sites['Paris'], *sites['London'])

for i in distances:
    print(i, distances[i])
