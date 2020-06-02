p = list(map(int, input().split()))

N_key = [i for i in range(1, p[0] + 1)]
N_value = [[] for j in range(1, p[0] + 1)]
N = dict(zip(N_key, N_value))

M_key = [k for k in range(1, p[1] + 1)]
M_value = [p[0] for l in range(1, p[1] + 1)]
M = dict(zip(M_key, M_value))

Q = p[2]

i = 0
put = []
while i < Q:
    src = list(map(int, input().split()))
    if src[0] == 2:
        M[src[2]] -= 1
        N[src[1]].append(src[2]) 
    if src[0] == 1:
        li = [x for x in N[src[1]]]
        out = [M[y] for y in li]
        put.append(sum(out))
    i += 1

[print(z) for z in put]
