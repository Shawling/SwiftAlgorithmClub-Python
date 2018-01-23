""" 插入排序。从堆中抽取一个元素，插入到一个有顺序的队列中。
实际实现中并不需要两个数组。
插入排序：
从左到右依次取出元素，然后将它与左侧已经排好序的数组进行比较，直到插入合适的位置，是个稳定的排序。O(n2)
冒泡排序：
遍历所有未排序元素，直到找到最大（小）的元素。重复这个过程，直到所有当前最大（小）的元素都被找到。
"""

import copy

def insertion_sort(unsorted):
    # 不修改原来的数组
    array = copy.deepcopy(unsorted)
    for x in range(1, len(array)):
        # 只将插入值插入一次到目标位置
        temp = array[x]
        y = x
        while y > 0 and temp < array[y - 1]:
            array[y] = array[y - 1]
            y = y - 1
        array[y] = temp
    return array

if __name__ == '__main__':
    unsorted = [ 10, -1, 3, 9, 2, 27, 8, 5, 1, 3, 0, 26 ]
    print(insertion_sort(unsorted))
    print(unsorted)