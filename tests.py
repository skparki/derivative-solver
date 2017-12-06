from derivativesolver import *
import terms

print "\nFunction tests\n"
# function tests
print("Linear function & constant" , solve_derivative('2x+2') == "2")
print("Power function " , solve_derivative('5x^4-3x^3+2x^2+2x') == "20x^3-9x^2+4x+2")
# print("logarithmic function " , solve_derivative('2log_3(3x)+2') == "dont know")
# print("e function " , solve_derivative('e^3x') == "3e^3x")
# print("ln function " , solve_derivative('ln(2x+2)') == "(2)/(2x+2)")
# print("trig function " , solve_derivative('2sin(3x+2)') == "6cos(3x+2)")
# print("fraction function " , solve_derivative('(3x+2)/(4x+1)') == "dont know")

print "\nHelper functions\n"
# helper functions
print("split terms", split_terms('2x+2-3x^2') == ["2x", "-3x^2"])
print("drop constant", drop_constant(["4x^2", "+2x", "+4"]) == ["4x^2", "+2x"])
print("signs", get_signs('2x+2-3x^2') == ["+", "+", "-"])
# print("allign terms with leading -", allign_terms(['2x^2','5x','2'], ['-', '+', '-']) == "-2x^2+5x-2")
# print("allign terms with leading +", allign_terms(['2x^2','5x','2'], ['+', '+', '-']) == "2x^2+5x-2")

print "\nTerm functions\n"
# power term functions
print("power terms", terms.solve_power('2x^2') == "4x")
print("power terms", terms.solve_power('2x^6') == "12x^5")
print("power terms", terms.solve_power('2x') == "2")
# print("power terms", terms.solve_power('-5x^5') == "-25x^4")
# print("power terms", terms.solve_power('x^-5') == "-5x^-6")
# print("power terms", terms.solve_power('-x^-5') == "5x^-6")
# ln term functions
print("ln terms", terms.solve_ln('ln(2x^2)') == "(4x)/(2x^2)")
print("ln terms", terms.solve_ln('ln(2x^6)') == "(12x^5)/(2x^6)")
print("ln terms", terms.solve_ln('ln(2x)') == "(2)/(2x)")
# sin term functions
print("sin terms", terms.solve_sin('sin(2x^2)') == "(4x)cos(2x^2)")
print("sin terms", terms.solve_sin('sin(2x^6)') == "(12x^5)cos(2x^6)")
# print("sin terms", terms.solve_sin('4sin(3x-4)') == "(4)(3)cos(3x-4)")
print("sin terms", terms.solve_sin('sin(2x)') == "(2)cos(2x)")
# print("sin terms", terms.solve_sin('sin(-5x^-3)') == "(15x^-4)cos(-5x^-3)")
# cos term functions
print("cos terms", terms.solve_cos('cos(2x^2)') == "-(4x)sin(2x^2)")
print("cos terms", terms.solve_cos('cos(2x^6)') == "-(12x^5)sin(2x^6)")
print("cos terms", terms.solve_cos('cos(2x)') == "-(2)sin(2x)")
# tan term functions
print("tan terms", terms.solve_tan('tan(2x^2)') == "(4x)sec^2(2x^2)")
print("tan terms", terms.solve_tan('tan(2x^6)') == "(12x^5)sec^2(2x^6)")
print("tan terms", terms.solve_tan('tan(2x)') == "(2)sec^2(2x)")
# e term functions
print("e terms", terms.solve_e('e^(2x^2)') == "(4x)e^(2x^2)")
print("e terms", terms.solve_e('e^(2x^6)') == "(12x^5)e^(2x^6)")
print("e terms", terms.solve_e('e^(2x)') == "(2)e^(2x)")
# sec term functions
print("sec terms", terms.solve_sec('sec(2x^2)') == "(4x)sec(2x^2)tan(2x^2)")
print("sec terms", terms.solve_sec('sec(2x^6)') == "(12x^5)sec(2x^6)tan(2x^6)")
print("sec terms", terms.solve_sec('sec(2x)') == "(2)sec(2x)tan(2x)")
# csc term functions
print("csc terms", terms.solve_csc('csc(2x^2)') == "-(4x)csc(2x^2)cot(2x^2)")
print("csc terms", terms.solve_csc('csc(2x^6)') == "-(12x^5)csc(2x^6)cot(2x^6)")
print("csc terms", terms.solve_csc('csc(2x)') == "-(2)csc(2x)cot(2x)")
# cot term functions
print("cot terms", terms.solve_cot('cot(2x^2)') == "-(4x)csc^2(2x^2)")
print("cot terms", terms.solve_cot('cot(2x^6)') == "-(12x^5)csc^2(2x^6)")
print("cot terms", terms.solve_cot('cot(2x)') == "-(2)csc^2(2x)")

# a^x term functions
print("a^x terms", terms.solve_a_power_x('5^(2x^2)') == "(4x)(5)^(2x^2)ln(5)")
print("a^x terms", terms.solve_a_power_x('3^(2x^6)') == "(12x^5)(3)^(2x^6)ln(3)")
print("a^x terms", terms.solve_a_power_x('7^(2x)') == "(2)(7)^(2x)ln(7)")
