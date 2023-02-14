# using dp => O(n)
def fib_dp(n):
    res = [0, 1]
    for i in range(2, n + 1):
        res.append(res[i - 1] + res[i - 2])
    return res[n]


# using memoization => O(n)
MAX = 100000  # initialize maximum number passed to fibonacci function
mem = [-1] * MAX  # initialize with a number that is never seen in the result
def fib_mem(n):
    if n <= 1:
        return n
    # check if the number has been already calculated before
    if mem[n] != -1:
        return mem[n]

    mem[n] = fib_mem(n - 1) + fib_mem(n - 2)
    return mem[n]


print(fib_dp(7))
print(fib_mem(7))
