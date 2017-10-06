from derivativesolver import *

print "/exit to exit"

while True:
    function = raw_input("enter a function: ")
    if function == "/exit":
        break
    print "The derivative is", solve_derivative(function)
