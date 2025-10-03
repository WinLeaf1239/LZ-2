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
if Z <= 1_000_000 :
    print("Итоговое кол-во шагов " , Z)

    """
    a = (input()).split()
b = 0
for i in range(0 , len(a)) :
    a[i] = int(a[i])
x = int(input(''))
match x :
    case 0 :
        for i in range(0 , len(a)) :
            a[i] = 0
    case 1 :
        for i in range(0,len(a)):
            a[i] = a[i] *2
    case 2 :
        for i in range(0, len(a) , 2) :
            a[i] = a[i] +10
    case 3 :
        for i in range(0,len(a),3):
            if a[i] >= 0:
                a[i] = a[i] **0.5
            else : 
                a[i] = 0
    case _:
        b = sum(a)
print(a)
print(b)
    """






