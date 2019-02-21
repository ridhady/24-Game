import time

def init_numbers(angkaAwal):
    listAngka = []
    for x1 in range(0,4):
        for x2 in range(0,4):
            for x3 in range(0,4):
                for x4 in range(0,4):
                    if ((x1 != x2) and (x1 != x3) and (x1 != x4) and (x2 != x3) and (x2 != x4) and (x3 != x4)):
                        urutanAngka = str(angkaAwal[x1]) + ' ' + str(angkaAwal[x2]) + ' ' + str(angkaAwal[x3]) + ' ' + str(angkaAwal[x4])
                        listAngka.append(urutanAngka)
    return set(listAngka)

def init_ops():
    listOperator =[]
    ops = '+-*/'
    for o1 in range(0,4):
        for o2 in range (0,4):
            for o3 in range(0,4):
                urutanOp = ops[o1] + ops[o2] + ops[o3]
                listOperator.append(urutanOp)
    return set(listOperator)

def solve(listAngka):
    listOperator = init_ops()
    count = 0
    for angkaHitung in listAngka:
        angka = ''.join(angkaHitung).split(' ')
        for op in listOperator:
            '''
            try:
                ekspresi = '((' + angka[0] + op[0] + angka[1] + ')' + op[1] + angka[2] + ')' + op[2] + angka[3]
                if (eval(ekspresi) == 24):
                    count = count + 1
                    print(ekspresi)
            except ZeroDivisionError:
                pass
            try:
                ekspresi = '(' + angka[0] + op[0] + angka[1] + ')' + op[1] + '(' + angka[2] + op[2] + angka[3] + ')'
                if (eval(ekspresi)== 24):
                    count = count + 1
                    print(ekspresi)
            except ZeroDivisionError:
                pass
            try:
                ekspresi = angka[0] + op[0] + '((' + angka[1] + op[1] +  angka[2] + ')' + op[2] + angka[3] + ')'
                if (eval(ekspresi) == 24):
                    count = count + 1
                    print(ekspresi)
            except ZeroDivisionError:
                pass
            try:
                ekspresi = '(' + angka[0] + op[0] + '(' + angka[1] + op[1] + angka[2] + '))' + op[2] + angka[3]
                if (eval(ekspresi) == 24):
                    count = count + 1
                    print(ekspresi)
            except ZeroDivisionError:
                pass
            try:
                ekspresi = angka[0] + op[0] + '(' + angka[1] + op[1] + '(' + angka[2] + op[2] + angka[3] + '))'
                if (eval(ekspresi) == 24):
                    count = count + 1
                    print(ekspresi)
            except ZeroDivisionError:
                pass
            '''
    print("%d Solusi ditemukan" %count)

#Main Program
from tkinter import *

top = Tk()
L1 = Label(top, text="User Name")
L1.pack( side = LEFT)
E1 = Entry(top, bd =5)
E1.pack(side = RIGHT)
s = E1.get()

print(s)
top.mainloop()