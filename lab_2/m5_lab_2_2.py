from random import randint
from string import ascii_letters
import argparse

parser = argparse.ArgumentParser(description="Spamming file")  # Creating of parser to use with command line
parser.add_argument("-mb", "--mb", type=int, required=True, help="Size of the file")
parser.add_argument("-file", "--file", type=str, required=True, help="Name of the file")
parser.add_argument("-word_tuple_str", "--word_tuple_str", type=str, default="3,10", help="Amount of word symbols")
parser.add_argument("-line_tuple_str", "--line_tuple_str", type=str, default="10,100", help="Size of the file")
args = parser.parse_args()


def filespam():
    try:
        while True:
            mb, name = input("Введите размер файла и его название через символ '/' : ").split("/")
            if mb == "exit" or name == "exit":
                break  # Type "exit" to stop programme
            while mb.isalpha() or int(mb) < 0 or name[-4:] == ".txt":
                mb, name = input("Введите размер файла и его название через символ '/' : ").split("/")
            mb, name = int(mb), str(name)
            file = name + ".txt"

            word_tuple_str, line_tuple_str = input("Введите кол-во букв в слове и кол-во слов в строке (введите 0,0 для"
                                                   " значения по умолчанию) через знак '/': ").split("/")
            if word_tuple_str == "exit" or line_tuple_str == "exit":
                break
            if word_tuple_str == "0,0":
                word_tuple_str = "3,10"
            if line_tuple_str == "0,0":
                line_tuple_str = "10,100"
            while word_tuple_str.split(",")[0].isalpha() or int(word_tuple_str.split(",")[0]) < 0 or \
                    word_tuple_str.split(",")[1].isalpha() or int(word_tuple_str.split(",")[1]) < 0 or \
                    line_tuple_str.split(",")[0].isalpha() or int(line_tuple_str.split(",")[0]) < 0 or \
                    line_tuple_str.split(",")[1].isalpha() or int(line_tuple_str.split(",")[1]) < 0 or \
                    int(word_tuple_str.split(",")[0]) > int(word_tuple_str.split(",")[1]) or \
                    int(line_tuple_str.split(",")[0]) > int(line_tuple_str.split(",")[1]):  # Validation of input data
                word_tuple_str, line_tuple_str = input("Введите кол-во букв в слове и кол-во слов в строке "
                                                       "(введите 0,0 для значения по умолчанию) через знак ',': ") \
                    .split(",")
            word_tuple, line_tuple = tuple(map(int, word_tuple_str.split(","))), \
                                     tuple(map(int, line_tuple_str.split(",")))

            result = ''
            size = 0
            alphabet = list(ascii_letters)

            with open(file, "w") as f:
                while size < mb * (1024 ** 2):
                    word_amount = randint(int(line_tuple[0]), int(line_tuple[1]))  # Generation of random word amount
                    # in line
                    for i in range(word_amount):
                        word = ''
                        symbols_amount = randint(int(word_tuple[0]), int(word_tuple[1]))  # Generation of random
                        # letter amount in one word
                        for x in range(symbols_amount):
                            letter = alphabet[randint(0, 51)]  # Filling word with random letters
                            if size < mb * (1024 ** 2):
                                size += 1  # One symbol weights 1 byte
                                result += letter
                                word += letter
                            else:
                                break
                        if size < mb * (1024 ** 2):
                            size += 1
                            result += ' '
                        else:
                            break
                    if size < mb * (1024 ** 2):
                        size += 2  # One new line weights 2 bytes
                        result += '\n'
                    else:
                        break
                    print("\r", "Прогресс программы: ", round((size * 100) / (mb * 1048576), 1), "%", end="")  #
                    # Status bar
                f.write(result)
            print("\n")
    except ValueError:
        filespam()


def file_spam_by_args(mb, file, word_tuple_str, line_tuple_str):  # Using with command line
    word_tuple, line_tuple = tuple(map(int, word_tuple_str.split(","))), \
                             tuple(map(int, line_tuple_str.split(",")))
    result = ''
    size = 0
    alphabet = list(ascii_letters)
    with open(file, "w") as f:
        while size < mb * (1024 ** 2):
            word_amount = randint(int(line_tuple[0]), int(line_tuple[1]))
            for i in range(word_amount):
                word = ''
                symbols_amount = randint(int(word_tuple[0]), int(word_tuple[1]))
                for x in range(symbols_amount):
                    letter = alphabet[randint(0, 51)]
                    if size < mb * (1024 ** 2):
                        size += 1
                        result += letter
                        word += letter
                    else:
                        break
                if size < mb * (1024 ** 2):
                    size += 1
                    result += ' '
                else:
                    break
            if size < mb * (1024 ** 2):
                size += 2
                result += '\n'
            else:
                break
            print("\r", "Прогресс программы: ", round((size * 100) / (mb * 1048576), 1), "%", end="")
        f.write(result)
    print("\n")


if __name__ == "__main__":
    file_spam_by_args(args.mb, args.file, args.word_tuple_str, args.line_tuple_str)
