# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

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

def GenerujTabliceGeometrii(x_0,x_p,n):

    val = (x_p-x_0)/(n-1)
    tablica_w = np.array([x_0])

    for indeks1 in range(1,n,1):
        tablica_w = np.block([tablica_w, indeks1* val + x_0])

    tablica_e = np.zeros((n-1,2))

    for indeks2 in range(0, n-1, 1):
        tablica_e[indeks2][0] = indeks2+1
        tablica_e[indeks2][1] = indeks2+2


    return indeks1,tablica_w,tablica_e


def Rysuj_geometrie(tablica_w,tablica_e, n):
    tab=np.zeros((n))
    l1 = plt.plot(tablica_w,tab)
    for indeks in range(0,n,1):
        plt.text(tablica_w[indeks], -0.01, str(i+1))
        plt.text(tablica_w[indeks], 0, "|")
        plt.text(tablica_w[indeks+1]/2+tablica_w[indeks]/2, 0.005 ,str(indeks+1))




Wezly, Tablica1, Tablica2 = GenerujTabliceGeometrii(0,1,4)
Rysuj_geometrie(Tablica1, Tablica2, Wezly+1)