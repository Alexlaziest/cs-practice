def winner(names, scores):
    maxx=-10000
    maxid=0
    if len(scores)==0: return 'no one'
    for i in range(0 , len(scores)):
        if maxx<scores[i]:
            maxx=scores[i]
            maxid=i
    return names[maxid]

def average(scores):
    if len(scores)==0: return 0.0
    return round(sum(scores)/len(scores), 2)

def ranking(names,scores):
    lis = [[nam, num]  for nam, num in zip(names, scores)]
    lis = sorted(lis, key= lambda p: p[1], reverse= True)
    return [i[0]  for i in lis]

def above_average(names,scores):
    lis = [[nam, num]  for nam, num in zip(names, scores)]
    return [i[0] for i in lis if i[1]> average(scores)]
