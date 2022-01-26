"""Lab4.1 Python 3.10.2"""

resistances = []
print("end - конец ввода.")
while True:
    inp = input(f"Сопротивление {len(resistances) + 1}-го проводника: ")
    if inp == "end": break
    try:
        r = float(inp)
        if r <= 0: raise ValueError
        resistances.append(r)
    except ValueError:
        print("Ошибка: Некорректный ввод.")

# resistance_section = math.fsum(resistants)
resistance_section = 0
for resistance in resistances:
    resistance_section += resistance

print(f"Общее сопротивление цепи: {resistance_section:.3f}")
