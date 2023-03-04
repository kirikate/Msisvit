from regexes import *
import re

vars = {}
ops = {}


def analyze(text: str):
    check_func(text)


def check_func(text: str):
    lst = re.findall(func, text)
    for fn in lst:
        operators = operators.replace('|'+fn[0]+')', ')')


def check_vars(text: str):
    lst = re.findall(variable, text)
    for var in lst:
        vars[var[0]] = len(re.findall('\b'+var[0]+'\b', text))

    lst = re.findall(string_literal, text)
    for lit in lst:
        vars[lit] = len(re.findall(lit, text))

    lst = re.findall(char_literal, text)
    for chr in lst:
        vars[chr] = len(re.findall(chr, text))

    lst = re.findall(numb_literal, text)
    for numb in lst:
        vars[numb] = len(re.findall('\b'+numb+'\b', text))


# find funcs
# add to operators
# scan all variables
# scan all operators
