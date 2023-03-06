from regexes import *
import re

vars: dict = {}
ops: dict = {}


def analyze(text: str):
    check_func(text)
    check_vars(text)
    check_ops(text)
    return {"operands": vars, "operators": ops}


def check_func(text: str):
    global operators
    lst = re.findall(func, text)
    for fn in lst:
        operators.append(fn[0])


def check_vars(text: str):
    lst = re.findall(variable, text)
    lst = set(lst)
    for var in lst:
        vars[var[0]] = len(re.findall(r'\b'+var[0]+r'\b', text))

    lst = re.findall(string_literal, text)
    lst = set(lst)
    for lit in lst:
        vars[lit] = len(re.findall(lit, text))

    lst = re.findall(char_literal, text)
    lst = set(lst)
    for chr in lst:
        vars[chr] = len(re.findall(chr, text))

    lst = re.findall(numb_literal, text)
    lst = set(lst)
    for numb in lst:
        vars[numb] = len(re.findall(r'\b'+numb+r'\b', text))


def check_ops(text: str):
    global ops
    for op in operators:
        lst = re.findall(op, text)
        if len(lst) == 0:
            continue
        ops[lst[0]] = len(lst)

    lst = re.findall(include, text)
    for op in lst:
        vars[op[1]] = 1
        if op[0] == '<':
            ops['<'] -= 1
            ops['>'] -= 1
    ops["#include"] = len(lst)

    lst = re.findall(brackets, text)
    lst = set(lst)
    for br in lst:
        ops[br] = len(re.findall(br, text))

    ops["cout"] = len(re.findall(cout, text))
    ops['cin'] = len(re.findall(cin, text))
# find funcs
# add to operators
# scan all variables
# scan all operators
