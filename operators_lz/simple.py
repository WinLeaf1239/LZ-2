n = int(input('Введите целое число от 1 до 25 включительно '))
if n == 1 :
    print("Y")
elif n%2 == 0 and n > 2 :
    print("N")
elif n%3 == 0 and n > 3 :
    print("N")
elif n%5 == 0 and n > 5 :
    print("N")
else :
    print("Y")