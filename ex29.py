from bisect import bisect_left


def solve(xs, rs, d=5):
    """
    xs — координаты точек
    rs — прибыли
    d  — минимально запрещённое расстояние 
    """

    pts = sorted(zip(xs, rs))
    xs = [x for x, _ in pts]
    rs = [r for _, r in pts]

    dp = [0]

    for x, r in zip(xs, rs):
        k = bisect_left(xs, x - d)
        dp.append(max(dp[-1], r + dp[k]))

    return dp[-1]


xs = [6, 7, 12, 14]
rs = [5, 6, 5, 1]

print(solve(xs, rs))  # 10(5+5)
