"""
    Module with selection problem
"""


import random


def select_ith_min(arr, ith):
    """
        Select i-th minimal element in the array
    """
    def partition(left, right, ith):
        """
            Partition array
        """
        if left == right:
            return arr[left]
        elif left < right:
            median = random.randint(left, right)
            arr[median], arr[right] = arr[right], arr[median]
            j = left - 1
            for i in range(left, right):
                if arr[i] <= arr[right]:
                    j += 1
                    arr[j], arr[i] = arr[i], arr[j]
            arr[right], arr[j + 1] = arr[j + 1], arr[right]
            k = j - left + 1
            if ith == k:
                return arr[j + 1]
            elif ith < k:
                return partition(left, j, ith)
            return partition(j + 1, right, ith - k)
    return partition(0, len(arr) - 1, ith)


def main():
    """
        Module entry point
    """
    arr = [int(random.random()*10000) for i in range(15)]
    print(f'Array: {arr}')
    print(f'Sorted array: {sorted(arr)}')
    for i in range(6):
        print(f'{i}-th minimal element: {select_ith_min(arr, i)}')


if __name__ == '__main__':
    main()
