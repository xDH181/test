import random as random


def generate_example(min_lines, max_lines, min_length, max_length):
    """
    Generate Example File content (print to console)
    Copy and paste console output into file for testing
    :param min_lines: min number of lines to generate
    :param max_lines: max number of lines to generate
    :param min_length: min length of lines to generate
    :param max_length: max length of lines to generate
    :return: none
    """
    inputs = ['N', 'E', 'S', 'W']
    for words in range(random.randint(min_lines, max_lines)):
        destination = ''
        for letters in range(random.randint(min_length, max_length)):
            destination = destination + str(inputs[random.randint(0, len(inputs) - 1)])
        print(destination)


generate_example(5, 80, 5, 100)
