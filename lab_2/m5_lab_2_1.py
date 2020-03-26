import math


def sqrt_decomposition():
    while True:
        n = input('Введите размерность массива (P.S. Для выхода из программы введите слово "exit"): ')
        if n == "exit":  # Type "exit" to exit from the programme
            break
        while n.isalpha() or int(n) < 0:  # Validation of input data
            n = input("Введите размерность массива: ")
        n = int(n)

        arr = []
        for i in range(n):
            arr.append(int(input("Введите элемент массива: ")))
        print(arr)

        l, r = input("Введите левую, а затем правую границу суммы: ").split()
        if l == "exit" or r == "exit":
            break
        while l.isalpha() or r.isalpha() or int(l) < 0 or int(r) < 0 or int(l) > int(r) or int(l) >= int(n) or \
                int(r) >= int(n):
            l, r = input("Введите левую, а затем правую границу суммы: ").split()
        l, r = int(l), int(r)
        length = int(math.sqrt(n)) + 1  # Length of one subsection
        sum = [0] * length  # array for sum of subsections
        n_l, n_r = l // length, r // length  # block with lower and upper bound
        result = 0  # Final sum

        i = 0
        while i < n:  # Filling array "sum" with the sum of subsections
            sum[i // length] += arr[i]
            i += 1

        if n_l == n_r:  # Case for l and r in the same subsection
            i = l
            while i <= r:
                result += arr[i]
                i += 1
        else:
            i = l
            while i < (n_l + 1) * length:  # Loop for checking the left bound of the quantity
                result += arr[i]
                i += 1

            i = n_l + 1
            while i < n_r:  # If the part of the quantity belongs to any subsection
                result += sum[i]
                i += 1

            i = n_r * length
            while i <= r:  # Loop for checking the right bound of the quantity
                result += arr[i]
                i += 1
        print("Сумма элементов с ", l, "по", r, "равна: ", result)


def sqrt_from_file(file_name = "Считываемые данные.txt"):
    with open(file_name) as file:
        info = file.read()
        info = info.replace("\n", " ")
        info = info.split()
        array = info[:-2]
        amount = len(array)
        length = int(math.sqrt(amount)) + 1
        sum = [0] * length
        l, r = int(info[-2]), int(info[-1])
        n_l, n_r = l // length, r // length
        result = 0

        i = 0
        while i < len(array):
            sum[i // length] += int(array[i])
            i += 1

        if n_l == n_r:
            i = l
            while i <= r:
                result += int(array[i])
                i += 1
        else:
            i = l
            while i < (n_l + 1) * length:
                result += int(array[i])
                i += 1

            i = n_l + 1
            while i < n_r:
                result += sum[i]
                i += 1

            i = n_r * length
            while i <= r:
                result += int(array[i])
                i += 1
        print("Нужная вам сумма: ", result)


if __name__ == "__main__":
    sqrt_from_file()
