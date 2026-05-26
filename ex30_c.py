def solve(w):
    n = len(w)
    d = [0] * (n + 1)

    # d[i] — лучший вес, который можно получить из первых i вершин
    for i in range(1, n + 1):
        take = w[i - 1]

        # Если берем текущую вершину, предыдущую брать нельзя
        if i >= 2:
            take += d[i - 2]

        # Если не берем текущую вершину, остается лучший ответ для первых i - 1 вершин
        skip = d[i - 1]

        d[i] = max(skip, take)

    ans = []
    i = n

    # Идем с конца и восстанавливаем, какие вершины попали в ответ
    while i >= 1:
        take = w[i - 1]

        if i >= 2:
            take += d[i - 2]

        skip = d[i - 1]

        if take > skip:
            ans.append(i)

            # Перепрыгиваем через соседнюю вершину
            i -= 2
        else:
            i -= 1

    ans.reverse()
    return ans, d[n]

w = [1, 8, 6, 3, 6]

ans, total = solve(w)

print(ans)
print(total)
