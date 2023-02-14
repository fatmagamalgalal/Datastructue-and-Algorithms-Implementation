str1 = 'abcdefgzh'
str2 = 'ackghefhlmn'
# find longest common sub string
# the idea that you try to take the letter or leave it

mem = [[-1] * (len(str2)) for i in range(len(str1))]

def LCS(i, j): # two iterators over the 2 strings
    if i == len(str1) or j == len(str2) :
        return 0

    # check if the number has been already calculated before
    if mem[i][j] != -1:
        return mem[i][j]

    if str1[i] == str2[j]: # the two letters are the same, take them and find the next
        return 1 + LCS(i+1, j+1)

    choice1 = LCS(i+1, j)
    choice2 = LCS(i, j+1)

    mem[i][j] = max(choice1, choice2) # take maximum of including or not including the letter
    return mem[i][j]


print(LCS(0,0))
print(include)