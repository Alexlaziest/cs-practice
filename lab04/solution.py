names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(n, s):
    maxx=0
    maxid=0
    if len(s)==0: return 'no one'
    for i in range(0 , len(s)):
        if maxx<s[i]:
            maxx=s[i]
            maxid=i
    return n[maxid]

def average(s):
    if len(s)==0: return 0.0
    return round(sum(s)/len(s), 2)

def ranking(n,s):
    lis = [[nam, num]  for nam, num in zip(n, s)]
    lis = sorted(lis, key= lambda p: p[1], reverse= True)
    return [i[0]  for i in lis]

