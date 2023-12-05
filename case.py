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

def ev_10(n, size):
    if n == 0:
        turtle.forward(size)

    else:
        ev_10(n - 1, size / 2)
        turtle.left(90)
        ev_10(n - 1, size / 2)
        turtle.right(180)
        ev_10(n - 1, size / 2)
        turtle.left(90)
        ev_10(n - 1, size / 2)

def tree(n, size):
  if n == 0:
    turtle.forward(size)
    turtle.back(size)

  else:
    turtle.forward(size)
    turtle.right(30)
    tree(n - 1, size * 0.65)
    turtle.left(60)
    tree(n - 1, size * 0.65)
    turtle.right(30)
    turtle.back(size)

def koch_5(n, size):
    if n == 0:
        turtle.forward(size)

    else:
        koch_5(n - 1, size / 3)
    if n == 0:          
        turtle.forward(size)
    else:
        koch_5(n - 1, size / 3)
        turtle.left(60)
        koch_5(n - 1, size / 3)
        turtle.right(120)
        koch_5(n - 1, size / 3)
        turtle.left(60)
        koch_5(n - 1, size / 3)

def ice_fractal_8(order, size):
    if order == 0:
        turtle.forward(size)

    else:
        ice_fractal_8(order-1, size/2)
        turtle.left(120)
        ice_fractal_8(order-1, size/4)
        turtle.right(180)
        ice_fractal_8(order-1, size/4)
        turtle.left(120)
        ice_fractal_8(order-1, size/4)
        turtle.right(180)
        ice_fractal_8(order - 1, size / 4)
        turtle.left(120)
        ice_fractal_8(order - 1, size / 2)

def koch_4(order, size):
    if order == 0:
        turtle.forward(size)

    else:
        koch_4(order-1, size/3)
        turtle.left(60)
        koch_4(order-1, size/3)
        turtle.right(120)
        koch_4(order-1, size/3)
        turtle.left(60)
        koch_4(order-1, size/3)

def kol_10(order, size):
    if order == 0:
        turtle.forward(size)

    else:
        kol_10(order-1, size/3)
        turtle.left(90)
        kol_10(order-1, size/3)
        turtle.right(60)
        kol_10(order-1, size/3)
        turtle.right(60)
        kol_10(order-1, size/3)
        turtle.right(60)
        kol_10(order - 1, size / 3)
        turtle.left(90)
        kol_10(order - 1, size / 3)


fractal = str(input('выберите фрактал, из представленных ниже:\n'
                    '1 - Ветка\n'
                    '2 - Кривая Минковского\n'
                    '3 - Ледяной фрактал 7\n'
                    '4 - Свой фрактал (Егор)\n'
                    '5 - Свой фрактал (Евгений)\n'
                    '6 - Дерево\n'
                    '7 - Кривая Коха 5\n'
                    '8 - Ледяной фрактал 8\n'
                    '9 - Кривая Коха\n'
                    '10 - Свой фрактал (Николай)\n'
                    ': '))
n = int(input('Глубина рекурсии: '))
size = int(input('Длина стороны: '))


if fractal == '1':
    turtle.up()
    turtle.goto(-400,-100)
    turtle.left(90)
    turtle.down()
    branch_3(n, size)

if fractal == '2':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    minkovsi_6(n, size)

if fractal == '3':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    ice_fractal_7(n, size)

if fractal == '4':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    eg_10(n, size)

if fractal == '5':
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(-400, 0)
    turtle.pendown()
    ev_10(n, size)

if fractal == '6':
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(-100,-200)
    turtle.pendown()
    turtle.left(90)
    tree(n, size)

if fractal == '7':
    turtle.speed(0)
    turtle.up()
    turtle.setposition(-100,0)
    turtle.down()
    for i in range(3):
        koch_5(n, size)
        turtle.right(120)

if fractal == '8':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    ice_fractal_8(n, size)

if fractal == '9':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    koch_4(n, size)

if fractal == '10':
    turtle.up()
    turtle.goto(-400, 0)
    turtle.down()
    kol_10(n, size)


turtle.done()
