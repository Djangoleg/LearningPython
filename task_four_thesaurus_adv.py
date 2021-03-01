def thesaurus_adv(*args):
    names_dict = dict()
    for x in args:
        n, s = x.split()
        if s[0] in names_dict:
            if n[0] in names_dict[s[0]]:
                temp_list = names_dict[s[0]][n[0]]
                temp_list.append(x)
            else:
                names_dict[s[0]][n[0]] = [x]
        else:
            names_dict[s[0]] = {n[0]: [x]}

    return names_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Андрей Сухов"))
