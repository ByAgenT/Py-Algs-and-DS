
"""
    Qsort module
"""

import random


def qsort(arr):
    """
        Sort array using quicksort algorithm
    """

    def partition(left, right):
        if left < right:
            median = random.randrange(left, right + 1)
            arr[right], arr[median] = arr[median], arr[right]
            j = left - 1
            for i in range(left, right):
                if arr[i] <= arr[right]:
                    j += 1
                    arr[j], arr[i] = arr[i], arr[j]
            arr[right], arr[j + 1] = arr[j + 1], arr[right]
            partition(left, j)
            partition(j + 1, right)

    partition(0, len(arr) - 1)
    return arr


def main():
    """
        Module entry point
    """
    arr = [int(random.random()*10000) for i in range(100)]
    print("Input: ", arr)
    print("Result: ", qsort(arr))


if __name__ == '__main__':
    main()
