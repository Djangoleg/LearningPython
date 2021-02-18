# Количество секунд. Можно поставить любое.
duration = 400153

seconds = duration % 60

duration = duration - seconds

days = int(duration / (24 * 60 * 60))

duration = duration - (days * 24 * 60 * 60)

hours = int(duration / (60 * 60))

duration = duration - (hours * 60 * 60)

minutes = int(duration / 60)

date = [[days, "дн"], [hours, "час"], [minutes, "мин"], [seconds, "сек"]]

summary = str()

for d in date:
    if d[0] > 0:
        summary += str(d[0]) + " " + d[1] + " "

print(summary)
