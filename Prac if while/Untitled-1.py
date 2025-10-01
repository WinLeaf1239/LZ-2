import math
Z = 0
n = int(input('Введите n '))
while n != 0 :
    if (n%3) == 0 :
        n = int((n-10) / 2)
        Z += 1
    elif (n%2) == 0 :
        n = int(n * 3)
        Z += 1
    elif (n%5) == 0 :
        n = int(math.sqrt(n))
        Z += 1
    elif (n%7) == 0 :
        n = int(n ** (1/3))
        Z += 1
    else :
        n = int(n-1)
        Z += 1
    if Z > 1_000_000 :
        print("Бесконеч")
        break
if Z < 1_000_000 :
    print("Итоговое кол-во шагов " , Z)






