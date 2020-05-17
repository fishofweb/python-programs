def find_outlier(integers):
    result_even = []
    result_odd = []
    for i in integers:
        if i % 2 == 0:
            result_even.append(i)
        elif i % 2 != 0:
            result_odd.append(i)
    if len(result_even) == 1:
        return int(result_even[0])
    if len(result_odd) == 1:
        return int(result_odd[0])
        
integers = [2, 4, 6, 8, 10, 3]
print(find_outlier(integers))

