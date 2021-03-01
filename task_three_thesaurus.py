def thesaurus(*args):
    names_dict = dict()

    for x in args:
        if x[0] in names_dict:
            tmp_list = names_dict[x[0]]
            tmp_list.append(x)
            names_dict[x[0]] = tmp_list
        else:
            names_dict[x[0]] = [x]

    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья", "Михаил", "Инга", "Павел", "Николай"))
