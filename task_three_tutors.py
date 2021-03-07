tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_tutors():
    for idx, tutor in enumerate(tutors):
        if idx < len(klasses):
            f_cort = (tutor, klasses[idx])
        else:
            f_cort = (tutor, None)

        yield f_cort


# Проверка.
tutor_generator = gen_tutors()
print(type(tutor_generator))

for x in range(len(tutors)):
    print(next(tutor_generator), sep=", ")
