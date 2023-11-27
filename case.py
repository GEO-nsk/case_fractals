from turtle import *

def branch_3(n, size):
    if n == 0:
        left(180)
        return

    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch_3(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch_3(n-i-1, 0.5*x*(n-i-1))
        right(135)

    forward(x)
    left(180)
    forward(size)

def minkovsi_6(n, size):
    if n == 0:
        forward(size)
        return

    else:
        minkovsi_6(n-1, size/2)
        left(90)
        minkovsi_6(n-1,size/2)
        right(90)
        minkovsi_6(n-1,size/2)
        right(90)
        minkovsi_6(n-1, size)
        left(90)
        minkovsi_6(n-1,size/2)
        left(90)
        minkovsi_6(n-1,size/2)
        right(90)
        minkovsi_6(n-1,size/2)

def ice_fractal_7(n, size):
    if n == 0:
        forward(size)
        return

    else:
        ice_fractal_7(n - 1,size)
        left(90)
        ice_fractal_7(n - 1, size / 2)
        right(180)
        ice_fractal_7(n - 1, size / 2)
        left(90)
        ice_fractal_7(n - 1, size)

def eg_10(n, size):
    if n == 0:
        forward(size)
        return

    else:
        eg_10(n - 1,size / 1.5)
        left(135)
        eg_10(n - 1,size / 4)
        right(135)
        eg_10(n - 1, (size/4) * 2 ** (1/2))
        right(135)
        eg_10(n - 1, size / 4)
        left(135)
        eg_10(n - 1, size / 1.5)



fractal = str(input('выберите фрактал, из представленных ниже:\n'
                    '1 - Ветка\n'
                    '2 - Кривая Минковского\n'
                    '3 - Ледяной фрактал 7\n'
                    '4 - Свой фрактал (Егор)\n'
                    ': '))
n = int(input('Глубина рекурсии: '))
size = int(input('Длина стороны: '))


if fractal == '1':
    up()
    goto(-400,-100)
    left(90)
    down()
    branch_3(n,size)

if fractal == '2':
    up()
    goto(-400, 0)
    down()
    minkovsi_6(n,size)

if fractal == '3':
    up()
    goto(-400, 0)
    down()
    ice_fractal_7(n,size)

if fractal == '4':
    up()
    goto(-400, 0)
    down()
    eg_10(n,size)


done()