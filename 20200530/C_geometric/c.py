s = input().split()

A = int(s[0])
R = int(s[1])
N = int(s[2])

if N > 32 and R > 1:
    print("large")
else:
    c = A * (R ** (N - 1))
    if c <= 10**9:
        print(c)
    else:
        print("large")
