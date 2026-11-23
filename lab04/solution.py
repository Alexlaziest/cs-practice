<<<<<<< HEAD
names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]

def winner(names, scores):
    if not scores: return ""
    best_score = max(scores)
    best_index = scores.index(best_score)
    return names[best_index]

def average(scores):
    if not scores: return 0.0
    return round(sum(scores) / len(scores), 2)

def ranking(names, scores):
    id = list(range(len(scores)))
    for i in range(len(id)):
        for j in range(i + 1, len(id)):
            if scores[id[j]] > scores[id[i]]:
                id[i], id[j] = id[j], id[i]
    res = []
    for i in id:
        res.append(names[i])
    return res

def above_average(names, scores):
    avg = average(scores)
    res = []
    for i in range(len(scores)):
        if scores[i] > avg: res.append(names[i])
    return res
if __name__ == '__main__':
    print(winner(names, scores))
    print(average(scores))
    print(ranking(names, scores))
    print(above_average(names, scores))
=======
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
>>>>>>> 1a5797978d175f8c5824c7d85a9af3b52881c698
