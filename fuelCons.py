consum = 0 # Средний расход 10.5 л/100 км
dist = 0 # Расстояние, км

dist = float(input("Пройденное расстояние, км: "))
consum = float(input("Средний расход топлива л/100 км: "))

result = consum * dist / 100

print(f"Необходимо {result} л.")