from random import choice
from random import shuffle

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_jokes, is_unique):
    """Функция возвращает заданное количество number_jokes шуточных фраз.
       Можно использовать ключ уникальности is_unique, чтобы слова не повторялись
       во фразах."""
    jokes_list = list()

    if is_unique:
        shuffle(nouns)
        shuffle(adverbs)
        shuffle(adjectives)
        nouns_list = nouns[:number_jokes]
        adverbs_list = adverbs[:number_jokes]
        adverbs_adjectives = adjectives[:number_jokes]

        for x in range(number_jokes):
            word_list = list()
            word_list.append(nouns_list[x])
            word_list.append(adverbs_list[x])
            word_list.append(adverbs_adjectives[x])
            jokes_list.append(" ".join(word_list))

    else:
        for x in range(number_jokes):
            word_list = list()
            word_list.append(choice(nouns))
            word_list.append(choice(adverbs))
            word_list.append(choice(adjectives))
            jokes_list.append(" ".join(word_list))

    return jokes_list


print(get_jokes(4, True))
print(get_jokes(4, False))
