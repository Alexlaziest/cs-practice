names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(n, s):
    t = 0
    for i in range(1,len(s)):
        if s[i] > s[i-1]:
            t = i
    return n[t]
def average(s):
    if len(s)
    t=0.0
    summ=sum(s)
    k=len(s)
    if k > 0:
        t=summ/k
    return float(f'{t:.2f}')
def ranking(n, s):
    ans = []
    odin = sorted(list(set(s)))[::-1]
    for best in odin:
        for i in range(len(scores)):
            if scores[i] == best:
                ans.append(names[i])
    return ans

def above_average(n, s):
    sr = average(s)
    ans=''
    for i in range(0,3):
        if s[i]>sr:
            ans+=f'{n[i]}  '
    return ans
print(winner(names, scores))
print(average(scores))
print(ranking(names, scores))
print(above_average(names, scores))
