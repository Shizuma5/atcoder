import heapq

N = int(input())
v = list(map(int, input().split(' ')))

def nabe(v):
    
    if len(v) == 1:
        return v[0]

    smallests = heapq.nsmallest(2, v)

    for s in smallests:
        v.remove(s)
    v.append(sum(smallests) / 2)

    return nabe(v)

print(nabe(v))