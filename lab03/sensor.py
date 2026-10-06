porog = float(input())
n =int(input())
er=0
verh=0
summ=0
k=0
maxx=-float("inf")
for i in range(n):
    t=input()
    if t == "error":
        er+=1
    else:
        t=float(t)
        summ+=t
        k+=1
        if t > porog:
            verh+=1
        if maxx < t:
            maxx=t
print(n)
print(er)
print(verh)
print(f'{maxx:.1f}')
if k != 0:
    print(f'{summ/k:.1f}')
else:
    print('Ошибка')
