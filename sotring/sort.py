import random
import time


def recursive_bubble_sort(data, index):
    if index == len(data) - 1:
        return False

    change = False
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:
            change = True
            data[i], data[i + 1] = data[i + 1], data[i]

    result = recursive_bubble_sort(data, index + 1)

    return result or change


count = 0


def recursive_quick_sort(data, level):
    if len(data) <= 1:
        return data

    # global count
    # if level > count:
    #     count = level
    #     print('--', count)

    pivot = data.pop(0)

    smaller_list = list()
    bigger_list = list()
    for n in data:
        if n <= pivot:
            smaller_list.append(n)
        else:
            bigger_list.append(n)
    # print(smaller_list)
    # print(bigger_list)
    smaller_result = recursive_quick_sort(smaller_list, level + 1)
    bigger_result = recursive_quick_sort(bigger_list, level + 1)

    return smaller_result + [pivot] + bigger_result


def merge_sort(data):
    if len(data) == 2:
        if data[0] > data[1]:
            data[0], data[1] = data[1], data[0]
        return data
    if len(data) < 2:
        return data

    mid_index = int(len(data) / 2)

    result_0 = merge_sort(data[:mid_index])
    result_1 = merge_sort(data[mid_index:])

    result = list()
    while result_0 and result_1:
        if result_0[0] < result_1[0]:
            target = result_0.pop(0)
        else:
            target = result_1.pop(0)
        result.append(target)

    if result_0:
        result.extend(result_0)

    if result_1:
        result.extend(result_1)

    # print(result)
    # print('================')

    return result


if __name__ == '__main__':
    data = [random.randint(0, 10000000) for _ in range(1000000)]

    print(data)

    start_time = time.time()
    # while recursive_bubble_sort(data, 0):
    #     pass

    data = recursive_quick_sort(data, 0)

    # data = merge_sort(data)
    end_time = time.time()
    print(data, len(data))
    print(f'耗費 {end_time - start_time} 秒')
