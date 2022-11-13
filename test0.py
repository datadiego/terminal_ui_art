from blessed import Terminal

from random import randint, choice
from time import sleep
from symbols_sets import sets, codex, lines_double_set


def create_top(len):
    top = lines_double_set[0]+lines_double_set[4]*(len-2)+lines_double_set[1]
    return top
def create_bottom(len):
    bottom = lines_double_set[2]+lines_double_set[4]*(len-2)+lines_double_set[3]
    return bottom
def create_mid(len):
    set_mid = choice(sets)
    mid = lines_double_set[5]
    for i in range(len-2):
        mid+=choice(set_mid)
    mid+=lines_double_set[5]
    return mid
def create_box(len, height):
    top = create_top(len)
    bottom = create_bottom(len)
    mid = []
    for i in range(height-2):
        mid.append(create_mid(len))
    return top, mid, bottom

term = Terminal()
print(term.home + term.clear)

width = 100
height = 10
ventana = create_box(width, height)
while True:
    mid = create_mid(width)
    ventana[1].remove(ventana[1][0])
    ventana[1].append(mid)
    print(term.home)
    print(term.move_right(10)+ventana[0])
    for i in ventana[1]:
        print(term.move_right(10)+i)
    print(term.move_right(10)+ventana[2])
    sleep(0.1)




