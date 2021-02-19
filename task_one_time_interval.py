# Вариант 1
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

# Вариант 2
duration = 400153
time_place = [duration // 86400, duration // 3600 % 24, duration // 60 % 60, duration % 60]

print(f"duration = {duration} сек\n{time_place[0]} дн {time_place[1]} час {time_place[2]} мин {time_place[3]} сек")
