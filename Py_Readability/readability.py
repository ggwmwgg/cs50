from cs50 import get_string


def main():

    text = get_string("Text: ")
    letter_count = 0
    word_count = 0
    sentence_count = 0

    for c in text:
        if is_word(c):
            word_count += 1
        elif is_sentence(c):
            sentence_count += 1
        elif is_letter(c):
            letter_count += 1
    word_count += 1

    index = c_l_index(letter_count, word_count, sentence_count)

    if index < 1:
        print("Before Grade 1")
    elif index > 16:
        print("Grade 16+")
    else:
        print(f"Grade {index}")


def is_word(c):
    return c == " "


def is_sentence(c):
    return c == "." or c == "!" or c == "?"


def is_letter(c):
    return c.isalpha()


def c_l_index(letter_count, word_count, sentence_count):
    kek = 100 * letter_count / word_count
    sek = 100 * sentence_count / word_count
    result = (0.0588 * kek) - (0.296 * sek) - 15.8
    return round(result)


main()