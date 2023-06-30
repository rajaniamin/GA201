def fibonacci(n):
    seq = [0, 1]

    if n <= 2:
        return seq[:n]

    for _ in range(2, n):
        nxt = seq[-1] + seq[-2]
        seq.append(nxt)

    return seq

num =4
ans = fibonacci(num)
print(ans)
