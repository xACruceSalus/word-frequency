def read_file(a_file):
    """This function's job is to read the file, clean the file,
    produce a count of the top twenty most used words,
    and plot them on a histogram."""

    output = []

    with open(a_file) as file:
        all_lines = file.readlines()

        for a_string in all_lines:
            a_string = a_string.lower().split()
            output.extend(a_string)

        output = word_frequency(output)
        print(output)
        output = top_twenty_pretty(output)

    return output


def word_frequency(a_string):
    """Ingests a list and returns a count
    of the top 20 most used words."""

    new_dict = {}
    clean_list = []

    for word in a_string:
        word = word_cleanup(word)
        clean_list.append(word)

    for word in clean_list:
        if word == '':
            continue
        if word in new_dict:
            new_dict[word] += 1
        else:
            new_dict[word] = 1

    new_dict = sorted(new_dict.items(), key= lambda x: x[1], reverse = True)

    return new_dict[:20]

def word_cleanup(a_string):
    """Cleans up a string, by removing the specified characters"""

    bad_chars = [".", ",", "?", "!", "@", "&", "%",
                "$", "' ", " - ", " '"]

    for char in bad_chars:
        if char in ["' ", " - ", " '"]:
            a_string = a_string.replace(char, ' ')
        else:
            a_string = a_string.replace(char, '')
    return a_string

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

read_file("sample.txt")
