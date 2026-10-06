names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(n, s):
    t = 0
    for i in range(1,3):
        if s[i] > s[i-1]:
            t = i
    return n[t]
