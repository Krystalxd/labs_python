import argparse


def merge_sort(arr):  # main function for line and words merging
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


def sorting_file(file="sorted_file.txt"):
    with open(file, 'r') as f:
        text = f.readlines()
        final_word_result = []

        for i in range(len(text)):
            word_result = []
            text[i] = text[i].split()
            word_array = []
            for k in range(len(text[i])):
                word_array.append(text[i][k][0])
            for j in range(len(word_array)):
                word_array[j] = int(ord(word_array[j]))
            word_indexed = list(zip(word_array, text[i]))
            merge_sort(word_indexed)  # merge sorting first letters in words
            for x in range(len(word_indexed)):
                word_result.append(list(word_indexed[x]))
            for x in range(len(word_indexed)):
                del word_result[x][0]
            for x in range(len(word_indexed)):
                word_result[x] = "".join(word_result[x])
            final_word_result.append(word_result)
            print("\r", "Прогресс программы: ", round(100 * i / (len(text)), 1), "%", end="")  #
            # Status bar
        for x in range(len(final_word_result)):
            final_word_result[x].append("\n")
            final_word_result[x] = ", ".join(final_word_result[x])

        line_array, final_line_result = [], []

        for i in range(len(final_word_result)):
            line_array.append(final_word_result[i][0])
        for i in range(len(line_array)):
            line_array[i] = int(ord(line_array[i]))

        line_indexed = list(zip(line_array, final_word_result))
        merge_sort(line_indexed)  # merge sorting first letters in each line

        for i in range(len(line_indexed)):
            final_line_result.append(list(line_indexed[i]))
        for i in range(len(line_indexed)):
            del final_line_result[i][0]
        for i in range(len(final_line_result)):
            final_line_result[i] = "".join(final_line_result[i])  # file sorted by lines and words
        final_line_result = ",".join(final_line_result)
        final_line_result = final_line_result.replace(",", '')

    with open(file, 'w') as f:
        final_line_result = final_line_result[0:-2]
        f.write(final_line_result)


def sorting_file_by_command_line():
    parser = argparse.ArgumentParser(description="Sorting file")  # Creating of parser to use with command line
    parser.add_argument("-file", "--file", type=str, default="sorted_file.txt", help="Name of the file")
    args = parser.parse_args()
    with open(args.file, 'r') as f:
        text = f.readlines()
        final_word_result = []

        for i in range(len(text)):
            word_result = []
            text[i] = text[i].split()
            word_array = []
            for k in range(len(text[i])):
                word_array.append(text[i][k][0])
            for j in range(len(word_array)):
                word_array[j] = int(ord(word_array[j]))
            word_indexed = list(zip(word_array, text[i]))
            merge_sort(word_indexed)  # merge sorting first letters in words
            for x in range(len(word_indexed)):
                word_result.append(list(word_indexed[x]))
            for x in range(len(word_indexed)):
                del word_result[x][0]
            for x in range(len(word_indexed)):
                word_result[x] = "".join(word_result[x])
            final_word_result.append(word_result)
            print("\r", "Прогресс программы: ", round(100 * i / (len(text)), 1), "%", end="")  #
            # Status bar
        for x in range(len(final_word_result)):
            final_word_result[x].append("\n")
            final_word_result[x] = ", ".join(final_word_result[x])

        line_array, final_line_result = [], []

        for i in range(len(final_word_result)):
            line_array.append(final_word_result[i][0])
        for i in range(len(line_array)):
            line_array[i] = int(ord(line_array[i]))

        line_indexed = list(zip(line_array, final_word_result))
        merge_sort(line_indexed)  # merge sorting first letters in each line

        for i in range(len(line_indexed)):
            final_line_result.append(list(line_indexed[i]))
        for i in range(len(line_indexed)):
            del final_line_result[i][0]
        for i in range(len(final_line_result)):
            final_line_result[i] = "".join(final_line_result[i])  # file sorted by lines and words
        final_line_result = ",".join(final_line_result)
        final_line_result = final_line_result.replace(",", '')
    with open(args.file, 'w') as f:
        final_line_result = final_line_result[0:-2]
        f.write(final_line_result)


if __name__ == "__main__":
    sorting_file_by_command_line()
