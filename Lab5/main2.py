"""Lab5.2 Python 3.10.2"""

nums = []
print("end - конец ввода.")
while True:
    inp = input(f"{len(nums) + 1}-е число: ")
    if inp == "end": break
    try:
        nums.append(int(inp))
    except ValueError:
        print("Ошибка: Некорректный ввод.")

new_nums = [num for num in nums if num % 2 == 0 and num < 10]

if new_nums:
    new_nums.sort()
    print(new_nums)
else:
    print("Нет чётных чисел меньше 10.")
