a = "11"
b = "1"

print(str(int(f"{sum([int('0b' + a, 2), int('0b' + b, 2)]):08b}")))
