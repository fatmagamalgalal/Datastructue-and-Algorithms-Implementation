class Obj:
    def __init__(self, value, weight):
        self.w = weight
        self.v = value
        self.vperw = value / weight

class Knapsack:
    def __init__(self, arr, Wmax):
        # sort by value per weight
        arr.sort(key = lambda x: x.vperw, reverse = True)
        max_profit = 0
        for item in arr:
            # add the whole item if its weight is smaller than the max weight
            if item.w <= Wmax:
                max_profit += item.v
                Wmax -= item.w
            else:
                # fractional for divisible items
                max_profit += item.v *(Wmax/item.w)
                Wmax -= item.w *(Wmax/item.w)
            if Wmax <=0: break
        print(max_profit)


arr = [Obj(10, 2), Obj(5, 3), Obj(15, 5), Obj(7, 7), Obj(6, 1), Obj(18, 4), Obj(3, 1)]
Knapsack(arr, 15)