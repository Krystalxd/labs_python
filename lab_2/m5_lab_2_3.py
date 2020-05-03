import argparse
from tempfile import TemporaryFile
import os


def merge_sort(arr):  # main function for words and lines merging
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]

        merge_sort(L)
        merge_sort(R)
        i, j, k = 0, 0, 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def sorted_by_words(file):  # getting file sorted by words in line
    global final_progress
    with open(file, 'r') as f:
        result = ""
        info = f.readlines()
        lines_amount = len(info)
        for i in range(len(info)):
            info[i] = info[i].split()
            merge_sort(info[i])
            info[i] = " ".join(info[i])
            info[i] += "\n"
            result += info[i]
            final_progress += 1
            print("\r", "Прогресс программы: ", round(50 * i / lines_amount, 1), "%", end="")  # progress bar
    with open(file, "w") as f:
        f.write(result)


def dividing_file_and_sorting_by_lines(file):  # dividing file on temporary smaller files and then
    # merge sorting them by lines
    file.seek(0)
    size = os.path.getsize(file.name)

    if size > 26214400:  # temporary files weight is 25mb

        first_help_file, second_help_file = TemporaryFile(mode="w+t"), TemporaryFile(mode="w+t")

        for line in file:
            if os.path.getsize(first_help_file.name) <= size // 2:
                first_help_file.write(line)
            else:
                second_help_file.write(line)

        dividing_file_and_sorting_by_lines(first_help_file)
        dividing_file_and_sorting_by_lines(second_help_file)

        file.seek(0)
        first_help_file.seek(0)
        second_help_file.seek(0)

        first_file_line = first_help_file.readline()
        second_file_line = second_help_file.readline()

        while (first_file_line != "") and (second_file_line != ""):  # merge sort of lines
            if first_file_line > second_file_line:
                file.write(second_file_line)
                second_file_line = second_help_file.readline()  # step of your loop
            else:
                file.write(first_file_line)
                first_file_line = first_help_file.readline()
        while first_file_line != "":
            file.write(first_file_line)
            first_file_line = first_help_file.readline()  # step of your loop
        while second_file_line != "":
            file.write(second_file_line)
            second_file_line = second_help_file.readline()  # step of your loop

    else:  # when our temporary file is less than 25mb finally sorting it by lines
        global current_progress
        info = file.readlines()
        merge_sort(info)
        file.seek(0)
        current_progress += len(info)
        info = "".join(info)
        file.write(info)
        print("\r", "Прогресс программы: ", 50 + round((current_progress / final_progress) * 50), "%", end="")
        # progress bar


def final_sorting(file="sorted_file.txt"):  # for saving RAM using external merge sorting instead of basic merge sorting
    try:
        sorted_by_words(file)
        with open(file, "r+") as f:
            dividing_file_and_sorting_by_lines(f)
    except ZeroDivisionError:
        print("Your file is probably empty")


def final_sorting_by_args():  # using command line
    parser = argparse.ArgumentParser(description="External merge sort")  # Creating of parser to use with command line
    parser.add_argument("-file", "--file", type=str, required=True, help="file needed to be sorted")
    args = parser.parse_args()
    file = args.file
    try:
        sorted_by_words(file)
        with open(file, "r+") as f:
            dividing_file_and_sorting_by_lines(f)
    except ZeroDivisionError:
        print("Your file is probably empty")


if __name__ == "__main__":
    current_progress = 0
    final_progress = 0
    final_sorting()
