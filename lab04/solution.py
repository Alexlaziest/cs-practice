names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(n, s):
    t = 0
    for i in range(1,3):
        if s[i] > s[i-1]:
            t = i
    return n[t]
def average(s):
    t=0.0
    summ=sum(s)
    k=len(s)
    if k > 0:
        t=summ/k
    return float(f'{t:.2f}')
def above_average(n, s):
    sr = average(s)
    ans=''
    for i in range(0,3):
        if s[i]>sr:
            ans+=f'{n[i]}  '
    return ans
