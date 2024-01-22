input_arr = [1, 2, 3]


def sub_array(arr):
    window_size = 1
    result = []
    while window_size <= len(arr):
        for i in range(0, len(arr) - window_size + 1):
            result.append(arr[i:window_size+i])
        window_size += 1
    return result


print(sub_array(input_arr))
