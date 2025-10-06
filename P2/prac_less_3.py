import math


a = (input()).split()
for i in range(0 , len(a)) :
    a[i] = int(a[i])
x = int(input(''))         
match x :
    case 0 : 
        minimum1 = min(a)
        print("Мин. эл-нт" , minimum1)
        minel = a.count(minimum1)
        if minimum1 >= 2 :
            print("Кол-во мин. эл-нтов" , minel)
    case 1 :
        maximum1 = max(a)
        print("Мах. эл-нт" , maximum1)
        maxel = a.count(maximum1)
        if maximum1 >= 2 :
            print("Кол-во мах. эл-нтов" , maxel)
    case 2: 
        minimum1 = min(a) # начало
        maximum1 = max(a) # шаг
        elem = maximum1 - minimum1 # сколько раз надо выполнить
        print("Кол-во эл-нтов арифм. прогрессии" , elem)
        listik = list(range(minimum1 , minimum1 + maximum1  * elem , maximum1) )
        print(listik)
    case 3 : 
        minimum1 = min(a) # начало
        maximum1 = max(a) # шаг
        a = list()
        elem = maximum1 - minimum1 # сколько раз надо выполнить                                                             #Доделать с геом. прогресс
        print("Кол-во эл-нтов геом. прогрессии" , elem)
        for i in range(minimum1 , minimum1 * maximum1 *elem , maximum1) :
            a.append(i)
        print(a)
    case _ :
        s = int(sum(a)/len(a))
        print(s)
        if s < 0 :
            print(0)
        else :
            s = math.factorial(s)
            print(s)