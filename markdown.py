__author__='edinkelspiel'

def bold(input_string):
    return "**" + input_string + "**"

def italics(input_string):
    return "*" + input_string + "*"

def h1(input_string):
    return "#" +input_string

def h2(input_string):
    return "##" + input_string

def h3(input_string):
    return "###" + input_string

def h4(input_string):
    return "####" + input_string

def h5(input_string):
    return "#####" + input_string

def link(hyperlink, text):
    return "[" + text + "]" + "(" + hyperlink + ")"

def bullet_list(input_list):
    output_string = ""
    for line in input_list:
        output_string += ("* " + line + "\n")

def numbered_list(input_list):
    output_string = ""
    for x in range(len(input_list) - 1):
        output_string += (str(x + 1) + ". " + input_list[x] + "\n")




