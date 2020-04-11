from math import log
import argparse


def degree():
    try:
        while True:
            n = input('Введите нужное число (для выхода из программы введите "exit"):')
            if n == "exit":
                break
            while n.isalpha() or int(n) < 0:
                n = input('Введите нужное число: ')
            n = int(n)

            if n & (n - 1) == 0:  # Используем битовую операцию И для проверки
                print("Число", n, "является", int(log(n, 2)), "-ой степенью числа 2 ")
            else:
                print("Число", n, "не является точной степенью числа 2")
    except ValueError:
        degree()


def degree_by_command_line():
    parser = argparse.ArgumentParser(description="Defining the degree of the number")  # Creating of parser
    # to use with command line
    parser.add_argument("-number", "--number", type=int, required=True, help="Your number")
    args = parser.parse_args()
    if args.number & (args.number - 1) == 0:  # Используем битовую операцию И для проверки
        print("Число", args.number, "является", int(log(args.number, 2)), "-ой степенью числа 2 ")
    else:
        print("Число", args.number, "не является точной степенью числа 2")


if __name__ == "__main__":
    degree()
