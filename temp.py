# -*- coding: utf-8 -*-
import numpy as np

wezly = np.array([[1, 0],
                  [2, 1],
                  [3, 0.5],
                  [4, 0.75]])

elementy = np.array([[1, 3],
                     [4, 2],
                     [3, 4]])

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1

def generujTabliceGeometrii(x_p, x_k, n):
    temp = (x_k - x_p) / (n - 1)
    wezly = np.array([x_p, x_k])

    for i in range(1, n-1, 1):
        wezly = np.block([wezly, i * temp + x_p])

    elementy = np.array([])
    n = n-1

    return wezly