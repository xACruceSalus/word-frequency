from collections import Counter


def read_file(a_file):
    """This function's job is to read a file, clean the file,
    produce a count of the top twenty most used words,
    and plot them on a histogram."""

    with open(a_file) as file:
        all_lines = file.read()
        word_count = word_frequency(all_lines)

    return word_count


def word_frequency(a_string):
    """Ingests a string and returns a count
    of the top 20 most used words."""

    return_amount = 20
    dict_w_word_count = {}

    split_string = a_string.split()
    clean_list = [word_cleanup(word) for word in split_string]

    list_w_word_count = Counter(clean_list)
    list_w_word_count = sorted(list_w_word_count.items(),
                               key=lambda x: x[1], reverse=True)

    top_twenty_pretty(list_w_word_count[:return_amount])

    for name,num in list_w_word_count[:return_amount]:
        dict_w_word_count.update({name: num})

    return dict_w_word_count


def word_cleanup(a_string):
    """Cleans up a string by removing the specified characters"""

    bad_chars = [".", ",", "?", "!", "@", "&", "%",
                 "$", "' ", " - ", " '"]

    for char in bad_chars:
        if char in ["' ", " - ", " '"]:
            a_string = a_string.replace(char, ' ')
        else:
            a_string = a_string.replace(char, '')
    return a_string.lower()


def top_twenty_pretty(a_list):
    """Takes in a list of tuples and returns
    the results in a pretty histogram."""

    values_list = []

    for a, b in a_list:
        values_list.append(b)

    sum_list = sum(values_list)

    if max(values_list) > 50:
        scale = 50 / max(values_list)
        for a, b in a_list:
            print(a, int(b * scale) * '#')
    else:
        for i in a_list:
            print(i[0], i[1] * '#')

    return sum_list


print(read_file("sample.txt"))
