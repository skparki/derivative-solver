import re

def solve_power(term):
    if term[:1] == "x":
        term = "1" + term
    try:
        coefficient,power = re.findall(r'(\-?\d+?)x\^?(\-?\d+)?', term)[0]
    except IndexError:
        coefficient, power = (1,1)
    # print power
    # parse
    coefficient = int(coefficient)
    if not power:
        power = 1
    power = int(power)
    # operate
    if power > 2:
        coefficient *= power
        power -= 1
        # concatenate
        result = "%sx^%s" % (coefficient, power)
        return result
    elif power == 2:
        coefficient *= power
        # concatenate
        result = "%sx" % (coefficient)
        return result
    elif power == 1:
        result = "%s" % (coefficient)
        return result

def solve_ln(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?ln', term)[0]
    innerfunction = re.findall(r'ln\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "(%s)/(%s)" % (derivative_of_innerfunction, innerfunction)
    return "((%s)(%s))/(%s)" % (coefficient, derivative_of_innerfunction, innerfunction)

def solve_sin(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?sin', term)[0]
    innerfunction = re.findall(r'sin\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "(%s)cos(%s)" % (derivative_of_innerfunction, innerfunction)
    return "(%s)(%s)cos(%s)" % (coefficient, derivative_of_innerfunction, innerfunction)

def solve_cos(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?cos', term)[0]
    innerfunction = re.findall(r'cos\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "-(%s)sin(%s)" % (derivative_of_innerfunction, innerfunction)
    return "-(%s)(%s)sin(%s)" % (coefficient, derivative_of_innerfunction, innerfunction)

def solve_tan(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?tan', term)[0]
    innerfunction = re.findall(r'tan\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "(%s)sec^2(%s)" % (derivative_of_innerfunction, innerfunction)
    return "(%s)(%s)sec^2(%s)" % (coefficient, derivative_of_innerfunction, innerfunction)

def solve_e(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?e', term)[0]
    innerfunction = re.findall(r'e\^\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "(%s)e^(%s)" % (derivative_of_innerfunction, innerfunction)
    return "(%s)(%s)e^(%s)" % (coefficient, derivative_of_innerfunction, innerfunction)

def solve_cot(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?cot', term)[0]
    innerfunction = re.findall(r'cot\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "-(%s)csc^2(%s)" % (derivative_of_innerfunction, innerfunction)
    return "-(%s)(%s)csc^2(%s)" % (coefficient, derivative_of_innerfunction, innerfunction)

def solve_csc(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?csc', term)[0]
    innerfunction = re.findall(r'csc\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "-(%s)csc(%s)cot(%s)" % (derivative_of_innerfunction, innerfunction, innerfunction)
    return "-(%s)(%s)csc(%s)cot(%s)" % (coefficient, derivative_of_innerfunction, innerfunction, innerfunction)

def solve_sec(term):
    from derivativesolver import solve_derivative
    coefficient = re.findall(r'(\-?\d+?)?sec', term)[0]
    innerfunction = re.findall(r'sec\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    if coefficient == '':
        coefficient = 1
        return "(%s)sec(%s)tan(%s)" % (derivative_of_innerfunction, innerfunction, innerfunction)
    return "(%s)(%s)sec(%s)tan(%s)" % (coefficient, derivative_of_innerfunction, innerfunction, innerfunction)

def solve_a_power_x(term):
    from derivativesolver import solve_derivative
    a,innerfunction = re.findall(r'(\-?\d+)\^\((.*)\)', term)[0]
    derivative_of_innerfunction = solve_derivative(innerfunction)
    return "(%s)(%s)^(%s)ln(%s)" % (derivative_of_innerfunction, a, innerfunction, a)
