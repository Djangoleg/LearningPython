# Вариант 1
list_word = [[[1], "процент"], [list(range(5, 21)), "процентов"], [list(range(2, 5)), "процента"]]

for check_number in range(1, 21):
    for item in list_word:
        if check_number in item[0]:
            print(check_number, item[1])

# Вариант 2
for percent in range(40):
    if percent % 10 == 1 and percent % 100 != 11:
        print(percent, "процент", end=" ")
    elif 1 < percent % 10 < 5 and not 11 < percent % 100 < 15:
        print(percent, "процента", end=" ")
    else:
        print(percent, "процентов", end=" ")
