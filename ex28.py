def best_torg(prices):
    n = len(prices)
    min_price = prices[0]
    min_day = 1
    money = 0
    buy_day = -1
    sell_day = -1

    for day in range(2, n + 1):
        price = prices[day - 1]

        profit = price - min_price

        if profit > money:
            money = profit
            buy_day = min_day
            sell_day = day

        if price < min_price:
            min_price = price
            min_day = day

    if money == 0:
        return "Перепродажа с прибылью невозможна"

    return buy_day, sell_day, money


prices = [9, 1, 5, 4, 10]

print(best_torg(prices))
