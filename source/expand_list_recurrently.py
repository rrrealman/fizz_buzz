
def expand_list(iterable):
    '''
        Routine expands nested list into the flat
        list in recurrent fashion
    '''

    res = []

    for item in iterable:

        if isinstance(item, list):
            res += expand_list(item)

        else:
            res.append(item)

    return res


if __name__ == '__main__':

    test_iter = [1, 'a',
                 {1: 2},
                 [1, 3, 4,
                  ['a', 'b', 'c'],
                  5],
                 6,
                 'str',
                 ['abc']]

    print(expand_list(test_iter))
