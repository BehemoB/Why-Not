def find_missing_nums(nums):
    A = nums[1:-1]
    S = (A.split(','))
    i = iter(S)
    L = list(iter(lambda:int(next(i)),None))
    D = len(L)
    R = []
    for i in range (1,D+1):
        for j in L:
            if i == j:
                break
        else:
            R.append(i)
    return R
nums = []
print("Великие правила ввода: список ограничивать квадратными скобками, элементы писать без пробела и через запятую, иначе все сломается...")
nums = input("nums = ")
print(find_missing_nums(nums))
