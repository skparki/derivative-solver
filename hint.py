from terms import *
from derivativesolver import *

def assign_hint(function):
    terms = split_terms(function)
    # print terms
    # executes the derivative from terms.py
    for i in range(len(terms)):
        if ("log" in terms[i]):
            hint = "a/(xln10)"
        elif ("ln" in terms[i]):
            hint = "1/x"
        elif ("sin" in terms[i]):
            hint = "acos(ax)"
        elif ("cos" in terms[i]):
            hint = "-asin(ax)"
        elif ("tan" in terms[i]):
            hint = "asec^2(ax)"
        elif ("e^" in terms[i]):
            hint = "ae^(ax)"
        elif ("cot" in terms[i]):
            hint = "-acsc^2(ax)"
        elif ("csc" in terms[i]):
            hint = "-acsc(ax)cot(ax)"
        elif ("sec" in terms[i]):
            hint = "asec(ax)tan(ax)"
        # regex finds a number following a '^' for number powers
        elif (re.findall(r'^\d+\^', terms[i])):
            hint = "a^(x)(ln(a))"
        else:
            hint = "nx^(n-1)"
    return hint
