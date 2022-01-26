"""Lab5.1 Python 3.10.2"""

nums = []
print("end - конец ввода.")
while True:
    inp = input(f"{len(nums) + 1}-е число: ")
    if inp == "end": break
    try:
        nums.append(int(inp))
    except ValueError:
        print("Ошибка: Некорректный ввод.")

max_even_num = max([num for num in nums if num % 2 == 0], default=None)

if max_even_num:
    print(f"Наибольшее чётное число: {max_even_num}")
else:
    print("Нет чётных чисел.")
