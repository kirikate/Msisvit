import tkinter as tk
import math

from classes import *
import logic as l

main = tk.Tk()
main.title('Метрика Холстэда')
main.geometry("800x800")
file = open("D:\Msisvit\Lab1\Source.cpp")
text = file.read()
file.close()
print(text)
label = tk.Label(text="Операнд")
label.grid(row=0, column=0)
label = tk.Label(text="Количество")
label.grid(row=0, column=1)
res = l.analyze(text)
count = 1
lenOfProg = 0

for ops in res['operands']:
    label = tk.Label(text=ops)
    label.grid(row=count, column=0)
    label = tk.Label(text=res['operands'][ops])
    lenOfProg += res['operands'][ops]
    label.grid(row=count, column=1)
    count += 1

label = tk.Label(text='                                   ')
label.grid(row=0, column=2)
label = tk.Label(text="Оператор")
label.grid(row=0, column=3)
label = tk.Label(text="Количество")
label.grid(row=0, column=4)
count = 1
for ops in res['operators']:
    if res['operators'][ops] == 0:
        continue

    label = tk.Label(text=ops)
    label.grid(row=count, column=3)
    label = tk.Label(text=res['operators'][ops])
    lenOfProg += res['operators'][ops]
    label.grid(row=count, column=4)
    count += 1

label = tk.Label(text='Длина программы: ' + str(lenOfProg))
label.grid(column=2)
dOfProg = len(res['operators']) + len(res['operands'])
label = tk.Label(text='Словарь программы: ' + str(dOfProg))
label.grid(column=2)

label = tk.Label(text="Объем программы: " +
                 str(math.ceil(lenOfProg * math.log2(dOfProg))))
label.grid(column=2)
print(res)

main.mainloop()
