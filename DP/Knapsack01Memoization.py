max_weight = 8
p = [1, 2, 5, 6]
w = [2, 3, 4, 5]
# max_weight = 50
# p = [60, 100, 120]
# w = [10, 20, 30]

mem = [[-1] * (max_weight+1) for i in range(len(p))]

def kanpsak(i, w_remainder):
    if i < 0 or w_remainder == 0:
        return 0

    # check if the number has been already calculated before
    if mem[i][w_remainder] != -1:
        return mem[i][w_remainder]

    choice1 = kanpsak(i-1, w_remainder)  # do not include this item
    choice2 = 0
    if w[i] <= w_remainder:
        choice2 = kanpsak(i - 1, w_remainder-w[i]) + p[i]  # include this item

    mem[i][w_remainder] = max(choice1, choice2)  # take maximum of including or not including the item
    return mem[i][w_remainder]


print(kanpsak(len(p)-1, max_weight))


