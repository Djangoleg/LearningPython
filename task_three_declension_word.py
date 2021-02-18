list_word = [[[1], "процент"], [list(range(5, 21)), "процентов"], [list(range(2, 5)), "процента"]]

for check_number in range(1, 21):
    for item in list_word:
        if check_number in item[0]:
            print(check_number, item[1])
