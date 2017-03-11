
def binary_search(sorted_nums, target_num):

    length = len(sorted_nums)

    first = 0
    mid = length // 2
    last = length - 1

    while last != first:

        print(first, mid, last)

        if target_num < sorted_nums[mid]:
            last = mid
        elif target_num > sorted_nums[mid]:
            first = mid + 1

        mid = first + (last - first) // 2

        if target_num == sorted_nums[mid]:
            return mid


if __name__ == '__main__':
    print(binary_search([i for i in range(9)], -1))
    print('=================')
    print(binary_search([i for i in range(9)], 10))
    print('=================')
    print(binary_search([i for i in range(9)], 8))
    print('=================')
    print(binary_search([i for i in range(9)], 0))

