
def count_max_substr(string):

    '''
        This routine returns the longest sequences
        of character founded in string
    '''

    res = {}

    if len(string) == 0:
        return res

    def update_res(res, char, counter):
        if char not in res:
            res[char] = counter
        elif res[char] < counter:
            res[char] = counter

    char_counter = 1
    prev_char = string[0]
    for char in string[1:]:
        if char != prev_char:
            update_res(res, prev_char, char_counter)
            char_counter = 1
        else:
            char_counter += 1
        prev_char = char
    update_res(res, prev_char, char_counter)
    return res


test_string = 'bbbaaaaabsssssssssddddddffffffffeeeeew'
print(count_max_substr(test_string))
# {'d': 6, 's': 9, 'b': 3, 'e': 5, 'a': 5, 'w': 1, 'f': 8}