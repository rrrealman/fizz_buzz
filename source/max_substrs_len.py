from collections import namedtuple


def max_len_substr(string):

    '''
        This routine returns the longest sequences
        of character founded in string
    '''

    counter = 1
    prev_char = string[0]
    chars = {}

    for char in string[1:]:

        if char != prev_char:

            if prev_char not in chars or chars[prev_char] < counter:
                chars[prev_char] = counter

            counter = 1

        else:

            counter += 1

        prev_char = char

    if prev_char not in chars or chars[prev_char] < counter:
        chars[prev_char] = counter

    return chars


if __name__ == '__main__':

    TestCase = namedtuple('TestCase', ['data', 'ref'])

    test_cases = [TestCase('ababb', {'a': 1, 'b': 2}),
                  TestCase('abbab', {'a': 1, 'b': 2}),
                  TestCase('aababb', {'a': 2, 'b': 2}),
                  TestCase('abbaabba', {'a': 2, 'b': 2})]

    for test_case in test_cases:
        chars = max_len_substr(test_case.data)

        print(
            'Test data: {}\ttest reference: {}\ttest result: {}'.format(
                test_case.data, test_case.ref, chars))

        assert test_case.ref == chars