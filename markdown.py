__author__='edinkelspiel'

import numpy

# inline modifiers

def bold(input_string):
    return "**" + input_string + "**"

def italics(input_string):
    return "*" + input_string + "*"

def link(hyperlink, text):
    return "[" + text + "]" + "(" + hyperlink + ")"

def subscript(input_string):
    return "^(" + input_string + ")"

def strikethrough(input_string):
    return "~~" + input_string + "~~"

def inline_code(input_string):
    return "`" + input_string + "`"

# blockquote & blockcode

def blockquote(input_string):
    return ">" + input_string + "\n"

# TODO: Block code

# Headers

def header(level, input_string): # base
    return ("#" * level) + input_string + "\n"

def h1(input_string):
    return header(1, input_string)

def h2(input_string):
    return header(2, input_string)

def h3(input_string):
    return header(3, input_string)

def h4(input_string):
    return header(4, input_string)

def h5(input_string):
    return header(5, input_string)

def h6(input_string):
    return header(6, input_string)

# lists

def bullet_list(input_list):
    output_string = ""
    for line in input_list:
        output_string += ("* " + line + "\n")
    return output_string

def numbered_list(input_list):
    output_string = ""
    for x in range(len(input_list) - 1):
        output_string += (str(x + 1) + ". " + input_list[x] + "\n")
    return output_string

# tables

def table_constructor(number_of_rows, number_of_columns, column_titles=None):
    output = numpy.empty(shape=(number_of_rows, number_of_columns), dtype=numpy.unicode_) # uses numpy
    if column_titles is not None:
        if len(column_titles) != number_of_columns:
            print "column_titles does not have the accurate number of titles. \
            The program will return a multidimensional array with zeros."
        else:
            output[0] = column_titles

    # TODO: Find out why last item of array sometimes contains random characters, rather than simply staying empty
    # For now, using numpy.unicode_ instead
    return output





