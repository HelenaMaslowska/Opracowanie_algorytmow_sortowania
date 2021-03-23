# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
#                   ------   Helena Masłowska, 148182  ------
#                   ------   2 sem, Informatyka        ------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

import time
import sys
from random import randint
import random

sys.setrecursionlimit(90000)

def posortowane_rosnaco(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 1000))
    tab = sorted(tab)
    return tab

def posortowane_malejaco(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 1000))

    max_wart = tab[0]
    if max(tab):
        max_wart = max(tab)
    pom_tab = [0 for _ in range(max_wart + 1)]
    for i in range(n):
        pom_tab[tab[i]] = pom_tab[tab[i]] + 1
    x = 0
    for i in range(max_wart, -1, -1):
        for j in range(pom_tab[i]):
            tab[x] = i
            x = x + 1
    return tab

def posortowane_stale(n):
    tab = []
    for i in range(n):
        tab.append(50)
    return tab

def posortowane_nie(n):
    tab = []
    for i in range(n):
        tab.append(random.randint(1, 1000))
    return tab

def posortowane_V(n):
    tab = []
    m = n // 2
    for i in range(m):
        tab.append(random.randint(1, 1000))

    for i in range(m - 1):
        for j in range(i + 1, m):
            if tab[i] < tab[j]:
                tab[i], tab[j] = tab[j], tab[i]

    tab2 = []
    for i in range(n - m):
        tab2.append(random.randint(1, 1000))
    for i in range(n - m - 1):
        for j in range(i + 1, n - m):
            if tab2[i] > tab2[j]:
                tab2[i], tab2[j] = tab2[j], tab2[i]

    for i in range(n - m):
        tab.append(tab2[i])
    return tab

def posortowane_A(n):
    tab = []
    m = n // 2
    for i in range(m):
        tab.append(random.randint(1, 1000))

    for i in range(m - 1):
        for j in range(i + 1, m):
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j], tab[i]

    tab2 = []
    for i in range(n - m):
        tab2.append(random.randint(1, 1000))
    for i in range(n - m - 1):
        for j in range(i + 1, n - m):
            if tab2[i] < tab2[j]:
                tab2[i], tab2[j] = tab2[j], tab2[i]

    for i in range(n - m):
        tab.append(tab2[i])
    return tab


def Bubble_Sort(n, tab):
    start_time = time.time()
    for i in range(n - 1):
        for j in range(i + 1, n):
            if tab[i] > tab[j]:
                tab[i], tab[j] = tab[j], tab[i]
    print(", %s " % (time.time() - start_time))

def Selection_Sort(n, tab):
    start_time = time.time()
    for i in range(n - 1):
        p_min = i
        for j in range(i + 1, n):
            if tab[j] < tab[p_min]:
                p_min = j
        tab[p_min], tab[i] = tab[i], tab[p_min]
    print(", %s " % (time.time() - start_time))

def podziel_tablice(pocz, kon, tab):
    i = pocz - 1
    pivot = tab[kon]
    for j in range(pocz, kon):
        if tab[j] <= pivot:
            i = i + 1
            tab[i], tab[j] = tab[j], tab[i]
    tab[i + 1], tab[kon] = tab[kon], tab[i + 1]
    return i + 1

def quick(pocz, kon, tab):
    if len(tab) == 1:
        return tab
    if pocz < kon:
        piw = podziel_tablice(pocz, kon, tab)
        quick(pocz, piw - 1, tab)
        quick(piw + 1, kon, tab)

def Quick_Sort(n, tab):
    start_time = time.time()
    pocz = 0
    kon = n - 1
    quick(pocz, kon, tab)
    print(", %s " % (time.time() - start_time))

def glowny_merge(pocz, sr, kon, tab, n):
    c_tab = [0 for _ in range(n)]
    for i in range(pocz, kon+1):
        c_tab[i] = tab[i]
    i = pocz
    j = sr+1
    q = pocz
    while i <= sr & j <= kon:
        if c_tab[i] < c_tab[j]:
            tab[q] = c_tab[i]
            q = q + 1
            i = i + 1
        else:
            tab[q] = c_tab[j]
            q = q + 1
            j = j + 1
        while i <= sr:
            tab[q] = c_tab[i]
            q = q + 1
            i = i + 1

def merge(pocz, kon, tab, n):
    if pocz < kon:
        sr = (pocz+kon) // 2
        merge(pocz, sr, tab, n)
        merge(sr+1, kon, tab, n)
        glowny_merge(pocz, sr, kon, tab, n)

def Merge_Sort(n, tab):
    start_time = time.time()
    pocz = 0
    kon = n-1
    merge(pocz, kon, tab, n)
    print(", %s " % (time.time() - start_time))

def Counting_Sort(n, tab):
    start_time = time.time()
    max_wart = tab[0]
    if max(tab):
        max_wart = max(tab)
    pom_tab = [0 for _ in range(max_wart+1)]
    for i in range(n):
        pom_tab[tab[i]] = pom_tab[tab[i]] + 1
    x = 0
    for i in range(max_wart+1):
        for j in range(pom_tab[i]):
            tab[x] = i
            x = x + 1
    print(", %s " % (time.time() - start_time))



def badanie_Bubble_Sort():
    for n in [10, 100, 1000, 2000, 5000, 10000]:
        tab = posortowane_nie(n)
        print("Bubble Sort, nieposortowane,", n, end="")
        Bubble_Sort(n, tab)
        tab = posortowane_rosnaco(n)
        print("Bubble Sort, rosnaco,", n, end="")
        Bubble_Sort(n, tab)
        tab = posortowane_malejaco(n)
        print("Bubble Sort, malejaco,", n, end="")
        Bubble_Sort(n, tab)
        tab = posortowane_stale(n)
        print("Bubble Sort, stale,", n, end="")
        Bubble_Sort(n, tab)
        tab = posortowane_V(n)
        print("Bubble Sort, V-ksztaltne,", n, end="")
        Bubble_Sort(n, tab)
        tab = posortowane_A(n)
        print("Bubble Sort, A-ksztaltne,", n, end="")
        Bubble_Sort(n, tab)

def badanie_Selection_Sort():
    for n in [10, 100, 1000, 2000, 5000, 10000]:
        tab = posortowane_nie(n)
        print("Selection Sort, nieposortowane,", n, end="")
        Selection_Sort(n, tab)
        tab = posortowane_rosnaco(n)
        print("Selection Sort, rosnaco,", n, end="")
        Selection_Sort(n, tab)
        tab = posortowane_malejaco(n)
        print("Selection Sort, malejaco,", n, end="")
        Selection_Sort(n, tab)
        tab = posortowane_stale(n)
        print("Selection Sort, stale,", n, end="")
        Selection_Sort(n, tab)
        tab = posortowane_V(n)
        print("Selection Sort, V-ksztaltne,", n, end="")
        Selection_Sort(n, tab)
        tab = posortowane_A(n)
        print("Selection Sort, A-ksztaltne,", n, end="")
        Selection_Sort(n, tab)

def badanie_Quick_Sort():
    for n in [10, 100, 1000, 2000, 5000]:
        tab = posortowane_nie(n)
        print("Quick Sort, nieposortowane,", n, end="")
        Quick_Sort(n, tab)
        tab = posortowane_rosnaco(n)
        print("Quick Sort, rosnaco,", n, end="")
        Quick_Sort(n, tab)
        tab = posortowane_malejaco(n)
        print("Quick Sort, malejaco,", n, end="")
        Quick_Sort(n, tab)
        tab = posortowane_stale(n)
        print("Quick Sort, stale,", n, end="")
        Quick_Sort(n, tab)
        tab = posortowane_V(n)
        print("Quick Sort, V-ksztaltne,", n, end="")
        Quick_Sort(n, tab)
        tab = posortowane_A(n)
        print("Quick Sort, A-ksztaltne,", n, end="")
        Quick_Sort(n, tab)

def badanie_Merge_Sort():
    for n in [10, 100, 1000, 2000, 5000, 10000]:
        tab = posortowane_nie(n)
        print("Merge Sort, nieposortowane,", n, end="")
        Merge_Sort(n, tab)
        tab = posortowane_rosnaco(n)
        print("Merge Sort, rosnaco,", n, end="")
        Merge_Sort(n, tab)
        tab = posortowane_malejaco(n)
        print("Merge Sort, malejaco,", n, end="")
        Merge_Sort(n, tab)
        tab = posortowane_stale(n)
        print("Merge Sort, stale,", n, end="")
        Merge_Sort(n, tab)
        tab = posortowane_V(n)
        print("Merge Sort, V-ksztaltne,", n, end="")
        Merge_Sort(n, tab)
        tab = posortowane_A(n)
        print("Merge Sort, A-ksztaltne,", n, end="")
        Merge_Sort(n, tab)

def badanie_Counting_Sort():
    for n in [10, 100, 1000, 2000, 5000, 10000]:
        tab = posortowane_nie(n)
        print("Counting Sort, nieposortowane,", n, end="")
        Counting_Sort(n, tab)
        tab = posortowane_rosnaco(n)
        print("Counting Sort, rosnaco,", n, end="")
        Counting_Sort(n, tab)
        tab = posortowane_malejaco(n)
        print("Counting Sort, malejaco,", n, end="")
        Counting_Sort(n, tab)
        tab = posortowane_stale(n)
        print("Counting Sort, stale,", n, end="")
        Counting_Sort(n, tab)
        tab = posortowane_V(n)
        print("Counting Sort, V-ksztaltne,", n, end="")
        Counting_Sort(n, tab)
        tab = posortowane_A(n)
        print("Counting Sort, A-ksztaltne,", n, end="")
        Counting_Sort(n, tab)


for w in range(15):
    badanie_Bubble_Sort()
    badanie_Selection_Sort()
    badanie_Quick_Sort()
    badanie_Merge_Sort()
    badanie_Counting_Sort()

print()

# ---------------------------------------------------------------------------------------------------------------------
#
