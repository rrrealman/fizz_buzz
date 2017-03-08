'''
    Routine gets m, n which is the dimensions of chocolate
    bar and the number of cells to snap down at once k.
    If it is possible to snap off k cells from the bar at once
    it returns True, unless False.
'''


def possible_snap_off(m, n, k):

    if (k % n == 0 or k % m == 0) and k <= m * n:
        return True

    return False

test_sets = [(1, 1, 1, True),
             (1, 5, 1, True),
             (1, 5, 5, True),
             (2, 2, 3, False),
             (2, 2, 8, False)]

for test_set in test_sets:
    assert possible_snap_off(*test_set[:-1]) == test_set[3]
