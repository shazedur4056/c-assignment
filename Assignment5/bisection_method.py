# Bisection Method using Python
# Student Name: Rahman Md Shazedur
# Student ID: M25W7502

import math

# Student Information Variables
student_full_name_M25W7502 = "Rahman Md Shazedur"
student_identification_M25W7502 = "M25W7502"

print("Student Name:", student_full_name_M25W7502)
print("Student ID:", student_identification_M25W7502)


# Bisection Method Function

def bisection_method(function_name, lower_bound, upper_bound, tolerance, maximum_iteration):

    print("\nSolving:", function_name)
    print("Iteration\tRoot Value")

    iteration_counter = 1

    while iteration_counter <= maximum_iteration:

        midpoint_value = (lower_bound + upper_bound) / 2

        # Equation 1
        if function_name == "equation_1":
            function_lower = lower_bound**3 - lower_bound - 2
            function_mid = midpoint_value**3 - midpoint_value - 2

        # Equation 2
        elif function_name == "equation_2":
            function_lower = lower_bound**2 - 4
            function_mid = midpoint_value**2 - 4

        print(iteration_counter, "\t\t", round(midpoint_value, 6))

        # Stop condition
        if abs(function_mid) < tolerance:
            print("\nFinal Root =", round(midpoint_value, 6))
            break

        # Update interval
        if function_lower * function_mid < 0:
            upper_bound = midpoint_value
        else:
            lower_bound = midpoint_value

        iteration_counter += 1


# Test Case 1
# Equation: x^3 - x - 2 = 0

bisection_method(
    function_name="equation_1",
    lower_bound=1,
    upper_bound=2,
    tolerance=0.0001,
    maximum_iteration=50
)


# Test Case 2
# Equation: x^2 - 4 = 0

bisection_method(
    function_name="equation_2",
    lower_bound=0,
    upper_bound=3,
    tolerance=0.0001,
    maximum_iteration=50
)