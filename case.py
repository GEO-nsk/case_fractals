import turtle

def branch_3(n, size):
    if n == 0:
        turtle.left(180)
        return

    x = size/(n+1)
    for i in range(n):
        turtle.forward(x)
        turtle.left(45)
        branch_3(n-i-1, 0.5*x*(n-i-1))
        turtle.left(90)
        branch_3(n-i-1, 0.5*x*(n-i-1))
        turtle.right(135)

    turtle.forward(x)
    turtle.left(180)
    turtle.forward(size)

def minkovsi_6(n, size):
    if n == 0:
        turtle.forward(size)
        return

    else:
        minkovsi_6(n-1, size/2)
        turtle.left(90)
        minkovsi_6(n-1,size/2)
        turtle.right(90)
        minkovsi_6(n-1,size/2)
        turtle.right(90)
        minkovsi_6(n-1, size)
        turtle.left(90)
        minkovsi_6(n-1,size/2)
        turtle.left(90)
        minkovsi_6(n-1,size/2)
        turtle.right(90)
        minkovsi_6(n-1,size/2)

def ice_fractal_7(n, size):
    if n == 0:
        turtle.forward(size)
        return

    else:
        ice_fractal_7(n - 1,size)
        turtle.left(90)
        ice_fractal_7(n - 1, size / 2)
        turtle.right(180)
        ice_fractal_7(n - 1, size / 2)
        turtle.left(90)
        ice_fractal_7(n - 1, size)

def eg_10(n, size):
    if n == 0:
        turtle.forward(size)
        return

    else:
        eg_10(n - 1,size / 1.5)
        turtle.left(135)
        eg_10(n - 1,size / 4)
        turtle.right(135)
        eg_10(n - 1, (size/4) * 2 ** (1/2))
        turtle.right(135)
        eg_10(n - 1, size / 4)
        turtle.left(135)
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
    turtle.up()
    turtle.goto(-400,-100)
    turtle.left(90)
    turtle.down()
    branch_3(n,size)

if fractal == '2':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    minkovsi_6(n,size)

if fractal == '3':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    ice_fractal_7(n,size)

if fractal == '4':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    eg_10(n,size)


turtle.done()