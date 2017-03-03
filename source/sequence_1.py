def count_seq(x, epsilon = 0.0001):

    '''
        Routine counts approximate value of infinite sum
        sum from k=0 to infinity: (x**(2*k))/(2**k*k!) for given x and [epsilon].
        Counting is processing till the current term of series is bigger than
        [epsilon].
    '''

    k = 1
    term = 1
    res_sum = term
    fact = 1

    while term > epsilon:
        term = term * x * x / 2 / fact
        res_sum += term
        k += 1
        fact *= k

    return res_sum


print(count_seq(x=1, epsilon=0.0001))
