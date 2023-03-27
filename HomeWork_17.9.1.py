def sort_nums(list_of_nums):
    for i in range(0, len(list_of_nums) - 1):
        for j in range(0, len(list_of_nums) - 1):
            if list_of_nums[j] > list_of_nums[j + 1]:
                list_of_nums[j], list_of_nums[j + 1] = list_of_nums[j + 1], list_of_nums[j]

    return list_of_nums

def bi_search(a: int, list_of_nums: list) -> int:
    left, right = 0, len(list_of_nums)
    while left < right:
        middle = (left + right) // 2
        if list_of_nums[middle] < a:
            left = middle + 1
        else:
            right = middle
    return left


try:
    list_of_nums = list(map(int, input('Введите последовательность целых чисел через пробел: ').split()))

    if len(list_of_nums) >= 2 or list_of_nums is int:

        try:
            a = int(input('\nВведите любое целое число, которое больше наименьшего числа последовательности: '))

        except ValueError:
            print("\nВы не выполнили условия ввода!")

        else:
            sort_list_of_nums = sort_nums(list_of_nums)
            if sort_list_of_nums[0] < a <= sort_list_of_nums[-1]:
                print("\nПоследовательность чисел, отсортированная по возрастанию: ", list_of_nums)
                print("\nИндекс элемента, который меньше, чем введённое число =", bi_search(a - 1, list_of_nums))

            else:
                print("Вы не выполнили условия ввода!")

    else:
        print("Вы нарушили условия ввода! Последовательность предполагает хотя бы два числа!")

except ValueError:
    print("Вы ввели не числа!")
    
