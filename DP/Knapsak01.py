p = [0,1,2,5,6]  # add 0 at the start for calculations
w = [0,2,3,4,5]  # add 0 at the start for calculations
max_weight = 8
# initializa table rows = items, colums = max weight, where the first row and column are 0s
rows = len(p)
columns = max_weight+1
tab = [[0] * columns for i in range(rows)]

# construct the table method
for i in range(1,rows):
    for j in range(1,columns):
        # if the item's weight is less than the bag's size
        if w[i] <= j:
            # maximiza the choice of taking the item and not taking it
                # profit of not taking the item, # profit of taking the item and the best profit of the remaining weight
            tab[i][j] = max(tab[i-1][j],      p[i] + tab[i-1][j-w[i]])
        else:
            tab[i][j] = tab[i-1][j]

# find maximum profit and corresponding items
max_profit = tab[rows-1][columns-1]
include = [0]*rows
i = rows-1; j = columns-1
while i>0 and j>0:
    if tab[i][j] == tab[i-1][j]: # do not include this item
        i-=1 # go to next item
    else:
        include[i] = 1 # include this item
        j-=w[i] # subtract the item's weight from the max weight
        i-=1 # go to next item

print(f'Max profit = {max_profit}')
print(include)