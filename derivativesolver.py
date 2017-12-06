import re
from terms import *

def solve_derivative(function):
    terms = split_terms(function)
    # print terms
    # executes the derivative from terms.py
    for i in range(len(terms)):
        if ("log" in terms[i]):
            terms[i] = solve_log(terms[i])
        elif ("ln" in terms[i]):
            terms[i] = solve_ln(terms[i])
        elif ("sin" in terms[i]):
            terms[i] = solve_sin(terms[i])
        elif ("cos" in terms[i]):
            terms[i] = solve_cos(terms[i])
        elif ("tan" in terms[i]):
            terms[i] = solve_tan(terms[i])
        elif ("e^" in terms[i]):
            terms[i] = solve_e(terms[i])
        elif ("cot" in terms[i]):
            terms[i] = solve_cot(terms[i])
        elif ("csc" in terms[i]):
            terms[i] = solve_csc(terms[i])
        elif ("sec" in terms[i]):
            terms[i] = solve_sec(terms[i])
        # regex finds a number following a '^' for number powers
        elif (re.findall(r'^\d+\^', terms[i])):
            terms[i] = solve_a_power_x(terms[i])
        else:
            terms[i] = solve_power(terms[i])
    # gets signs from the function
    signs = get_signs(function)
    # alligns the signs with the
    derivative = allign_terms(terms)
    return derivative

# splits terms using regex
def split_terms(function):
    terms = re.findall(r'((\+?\-?\d+)?x\^?\d+?|(\d+)?.*\([^)]+\)|((\+|\-)?\d+?)x|(\+|\-)?x|(\+|\-)?\d+\^\([^)]+\))', function)
    # gets the first term from an array of 3
    for i in range(len(terms)):
        terms[i] = terms[i][0]
    return terms

# assigns + if first term is positive
def first_term_sign(function):
    if function[:1] == "-":
        return "-"
    else:
        return "+"

# gives an array of signs from the first term
def get_signs(function):
    # array of signs without the first
    # uses regex to findall pluses and minuses from the input function
    signs_wo_first = re.findall(r'\+|\-', function)
    # returns an array including the first term's sign
    return [first_term_sign(function)] + signs_wo_first

# drops constants
def drop_constant(terms):
    return list(filter(lambda term: 'x' in term, terms))

def allign_terms(terms):
    derivative = ""
    # assigns + to positive terms without a +
    for i in range(len(terms)):
        if terms[i][:1] != "-":
            terms[i] = "+" + terms[i]
        # combines all terms to be a function
        derivative += terms[i]
    # clear leading +
    if derivative[:1] == "+":
        derivative = derivative[1:]
    return derivative
