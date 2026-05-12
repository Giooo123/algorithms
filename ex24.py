def max_edge_on_path(tree, start, finish):
    seen = {start}
    stack = [(start, -1, None)]

    while stack:
        v, cur_max, max_edge = stack.pop()

        if v == finish:
            return cur_max, max_edge

        for to, cost in tree[v]:
            if to not in seen:
                seen.add(to)

                if cost > cur_max:
                    stack.append((to, cost, (v, to, cost)))
                else:
                    stack.append((to, cur_max, max_edge))


def same_edge(e1, e2):
    a, b, c = e1
    x, y, z = e2

    return c == z and ((a == x and b == y) or (a == y and b == x))


def solution_a(tree, v, w, c):
    max_cost, _ = max_edge_on_path(tree, v, w)

    return c >= max_cost


def solution_b(edges_T, tree, v, w, c):
    max_cost, bad_edge = max_edge_on_path(tree, v, w)

    if c >= max_cost:
        return edges_T

    new_T = []

    for edge in edges_T:
        if not same_edge(edge, bad_edge):
            new_T.append(edge)

    new_T.append((v, w, c))

    return new_T


# пример
edges_T = [
    (0, 1, 2),
    (1, 2, 4),
    (2, 3, 6),
    (3, 4, 3)
]

tree = {
    0: [(1, 2)],
    1: [(0, 2), (2, 4)],
    2: [(1, 4), (3, 6)],
    3: [(2, 6), (4, 3)],
    4: [(3, 3)]
}

v = 0
w = 3
c = 5


# (a)
print(solution_a(tree, v, w, c))


# (b)
print(solution_b(edges_T, tree, v, w, c))
