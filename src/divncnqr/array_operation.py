from typing import List


def array_sum(arr: list):
    if not arr:  # empty array
        return 0
    else:
        return arr[0] + array_sum(arr[1:])


def array_count(arr: list):
    if not arr:
        return 0
    else:
        return 1 + array_count(arr[1:])
    pass


def array_max(arr: List[float]):
    if len(arr) < 2:
        return arr[0]
    else:
        if arr[0] >= array_max(arr[1:]):
            return arr[0]
        else:
            return array_max(arr[1:])


def array_binary_search(arr_sorted: List[int], value: int):
    if len(arr_sorted) < 2:
        if value == arr_sorted[0]:
            print(f'Value {arr_sorted[0]} found in given array.')
            return arr_sorted[0]
        else:
            print(f'Value {value} not found in given array.')
            return
    else:
        i = int(len(arr_sorted) / 2)
        if value < arr_sorted[i]:
            return array_binary_search(arr_sorted[:i], value)
        elif value > arr_sorted[i]:
            return array_binary_search(arr_sorted[i+1:], value)
        else:
            print(f'Value {arr_sorted[i]} found in given array.')
            return arr_sorted[i]


if __name__ == '__main__':
    test_arr = [3, 6, 1, 4, 9]
    print(array_sum(test_arr))
    print(sum(test_arr))
    print(array_count(test_arr))
    print(len(test_arr))
    print(array_max(test_arr))
    print(max(test_arr))
    print(array_binary_search(sorted(test_arr), 4))
    print(array_binary_search(sorted(test_arr), 5))

