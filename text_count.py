def count_text_string(search_for, search_in):
    """
    a function that takes a text to
be searched for and a text to be searched in
    :param search_for: word to be searched for
    :param search_in: file to be searched in
    :return:
    """
    character_check = 0
    if search_in == "":
        return 0
    else:
        if search_for[0] == search_in[0]: #conditional statement
            word = search_for
            line = search_in
            while word != "":
                character_check = character_check + check_head(word, line)
                word = word[1:]
                line = line[1:]
            if character_check == length_string(search_for):
                return 1 + count_text_string(search_for, search_in[1:])
            else:
                return 0 + count_text_string(search_for, search_in[1:])
        else:
            return 0 + count_text_string(search_for, search_in[1:])


def check_head(string_1, string_2):
    """
    to check if the word matches or not
    :param string_1:
    :param string_2:
    :return:
    """
    if string_1[0] == string_2[0]:
        return 1
    else:
        return 0


def length_string(string):
    """
    to calculate the length of the string
    :param string:
    :return:
    """
    length = 0
    for character in string:
        length = length + 1
    return length


def count_text_file(search_for, text_file_name):
    """
    a function that takes in the
text to be searched for and the name of the file to search for the text in
    :param search_for:
    :param text_file_name:
    :return:
    """
    file = open(text_file_name)
    total = 0
    for line in file:
        if count_text_string(search_for, line) > 0:
            print(line.strip())
        total = total + count_text_string(search_for, line)
    print(total)


def main():
    """
    main function to implement the program
    :return:
    """
    search_for = input("Enter search word:")
    text_file_name = input("Enter file name:")
    count_text_file(search_for, text_file_name)


main()