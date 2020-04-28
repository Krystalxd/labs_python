import argparse


def multiplication_of_matrices(first_matrix, second_matrix):  # function for matrix multiplication
    first_element = first_matrix[0][0] * second_matrix[0][0] + first_matrix[0][1] * second_matrix[1][0]
    second_element = first_matrix[0][0] * second_matrix[0][1] + first_matrix[0][1] * second_matrix[1][1]
    third_element = first_matrix[1][0] * second_matrix[0][0] + first_matrix[1][1] * second_matrix[1][0]
    fourth_element = first_matrix[1][0] * second_matrix[0][1] + first_matrix[1][1] * second_matrix[1][1]
    first_matrix[0][0] = first_element
    first_matrix[0][1] = second_element
    first_matrix[1][0] = third_element
    first_matrix[1][1] = fourth_element


def power(first_matrix, n):  # function for exponentiation
    matrix = [[1, 1], [1, 0]]
    for i in range(2, n + 1):
        multiplication_of_matrices(first_matrix, matrix)


def fib(n):  # function for finding fibonacci numbers
    matrix = [[1, 1], [1, 0]]
    if n == 0:
        return 0
    power(matrix, n - 1)
    return matrix[0][0]


def leonardo():
    try:
        while True:
            n = input('Введите номер нужного числа Леонардо (для выхода из программы введите "exit"): ')
            if n == "exit":
                break
            while n.isalpha() or int(n) < 0:
                n = input("Введите номер нужного числа Леонардо: ")
            n = int(n)

            if n == 0 or n == 1:
                print(1)
            else:
                print("Ваше число: ", 2 * fib(n + 1) - 1)
    except ValueError:
        leonardo()


def leonardo_by_command_line():
    parser = argparse.ArgumentParser(description="Defining n Leonardo number")  # Creating of parser
    # to use with command line
    parser.add_argument("-number", "--number", type=int, required=True, help="Number of Leonardo number")
    args = parser.parse_args()
    try:
        if args.number == 0 or args.number == 1:
            print("Ваше число: ", 1)
        else:
            print("Ваше число: ", 2 * fib(args.number + 1) - 1)
    except ValueError:
        leonardo_by_command_line()


if __name__ == "__main__":
    leonardo()
