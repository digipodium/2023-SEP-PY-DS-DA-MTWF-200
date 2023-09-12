from turtle import *

dis = [100, 200, 150, 50, 120]
ngl = [90, 72, 144, 36, 60]


for d, a in zip(dis, ngl):
    fd(d)
    lt(a)

hideturtle()
mainloop()