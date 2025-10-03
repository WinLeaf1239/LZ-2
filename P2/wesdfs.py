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
        b = sum(a) #for i in range(0,len(a)):
                    # b += a[i]
print(a)
print(b)