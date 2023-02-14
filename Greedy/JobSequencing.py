class Obj:
    def __init__(self, value, deadline):
        self.d = deadline
        self.v = value
        # self.vperw = value / weight

# we try to do the job with max profit in the latest time slot available
def job_sequencing(arr):
    # Sort all jobs according to decreasing order of profit
    arr.sort(key= lambda x: x.v, reverse = True)

    # get maximum deadline
    dmax = max(arr, key= lambda x: x.d)

    # To keep track of free time slots
    slot = [0] * dmax.d

    max_profit = 0
    for job in arr:
        d = job.d

        # loop over free slots starting from the deadline - 1
        for i in range(d-1, -1, -1):
            # if there is free slot -> allocate the job and go to the next job
            # if not -> the job is discarded
            if slot[i] == 0:
                slot[i] = 1
                max_profit += job.v
                break
    return max_profit

# arr = [Obj(10, 2), Obj(5, 3), Obj(15, 5), Obj(7, 7), Obj(6, 1), Obj(18, 4), Obj(3, 1)]
arr = [Obj(100, 2), Obj(19, 1), Obj(27, 2), Obj(25, 1), Obj(15, 3)]

print(job_sequencing(arr))



