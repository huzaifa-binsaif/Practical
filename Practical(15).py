# n = 7
# a = [-10,0,10,10,-2,10,10]
# larg1= min(a)
# for i in range(0,n):
#     for h in a:
#         if h == larg1:
#             a.remove(larg1)
# print(min(a))

name = []
score = []
for _ in range(int(input())):
    name.append(input())
    score.append(float(input()))

    def lowest(score, a):
        lowest = 1000
        for i in range(0, a+1):
            for h in score:
                if h < lowest:
                    lowest = h
        return lowest

    lowest1 = lowest(score, _)

    for i in range(0, _+1):
        for h in score:
            if h == lowest1:
                score.remove(h)
                name.remove(name[i+2])

    lowest2 = lowest(score, _-1)
    new_name = []

    for i in range(0, len(score)):
        if score[i] == lowest2:
            try:
                new_name.append(name[i])
            except:
                break
    if len(new_name) > 1:
        new_name.sort()
        for i in new_name:
            print(i)
    else:
        print(new_name[0])