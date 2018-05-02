def change_possibilities_top_down(amount, denominations):
    possibilities = []

    for denom in denominations:
        if amount % denom == 0:
            something = int(amount/denom)
            possibility = [denom for i in range(1,something+1)]
            possibilities.append(possibility)

    return possibilities

a = [1,2,3]
a_money = 4
print(change_possibilities_top_down(a_money, a))
