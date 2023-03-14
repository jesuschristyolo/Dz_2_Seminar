#Требуется вывести все
#целые степени двойки(т.е.числавида2 k), не превосходящие числа N.
N = int(input("Введите число N: "))
Step = 1
k = 2

while Step <= N:
    Step = 2**k
    k+=1
    if Step > N:
        break
    print(f"2 ^ {k} = {Step}")


