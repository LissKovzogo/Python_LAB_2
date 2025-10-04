h = int(input("Введите часы (0-23): "))
m = int(input("Введите минуты (0-59): "))
s = int(input("Введите секунды (0-59): "))


if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
    print("Ошибка: некорректные значения времени")
else:
    adjusted_h = h % 12
    angle = adjusted_h * 30 + m * 0.5 + s * 0.5 / 60
    print(angle)