src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result_lst = [value for ind, value in enumerate(src) if ind > 0 and value > src[ind - 1]]

print(result_lst)
