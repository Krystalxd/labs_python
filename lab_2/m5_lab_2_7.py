import argparse


def leonardo():
    try:
        while True:
            n = input('Введите номер нужного числа Леонардо (для выхода из программы введите "exit"): ')
            if n == "exit":
                break
            while n.isalpha() or int(n) < 0:
                n = input("Введите номер нужного числа Леонардо: ")
            n = int(n)

            psi = (1 + 5 ** 0.5) / 2
            result = int((2 / (5 ** 0.5)) * (psi ** (n + 1) - (1 - psi) ** (n + 1)) - 1)
            if n == 0 or n == 1:
                print(1)
            else:
                print("Ваше число: ", result)
    except ValueError:
        leonardo()


def leonardo_by_command_line():
    parser = argparse.ArgumentParser(description="Defining n Leonardo number")  # Creating of parser
    # to use with command line
    parser.add_argument("-number", "--number", type=int, required=True, help="Number of Leonardo number")
    args = parser.parse_args()
    psi = (1 + 5 ** 0.5) / 2
    result = int((2 / (5 ** 0.5)) * (psi ** (args.number + 1) - (1 - psi) ** (args.number + 1)) - 1)
    if args.number == 0 or args.number == 1:
        print(1)
    else:
        print(result)


if __name__ == "__main__":
    leonardo()
