# Newton Method using Python
# Student Name: Rahman Md Shazedur
# Student ID: M25W7502

import math

# Student Information Variables
student_full_name_M25W7502 = "Rahman Md Shazedur"
student_identification_M25W7502 = "M25W7502"

print("Student Name:", student_full_name_M25W7502)
print("Student ID:", student_identification_M25W7502)


# Newton Method Function

def newton_method(function_name, initial_guess, tolerance, maximum_iteration):

    print("\nSolving:", function_name)
    print("Iteration\tRoot Value")

    iteration_counter = 1
    current_x = initial_guess

    while iteration_counter <= maximum_iteration:

        # Equation 1
        if function_name == "equation_1":
            function_value = current_x**3 - 2 * current_x - 5
            derivative_value = 3 * (current_x**2) - 2

        # Equation 2
        elif function_name == "equation_2":
            function_value = math.cos(current_x) - current_x
            derivative_value = -math.sin(current_x) - 1

        next_x = current_x - (function_value / derivative_value)

        print(iteration_counter, "\t\t", round(next_x, 6))

        # Stop condition
        if abs(next_x - current_x) < tolerance:
            print("\nFinal Root =", round(next_x, 6))
            break

        current_x = next_x
        iteration_counter += 1


# Test Case 1
# Equation: x^3 - 2x - 5 = 0

newton_method(
    function_name="equation_1",
    initial_guess=2,
    tolerance=0.0001,
    maximum_iteration=50
)


# Test Case 2
# Equation: cos(x) - x = 0

newton_method(
    function_name="equation_2",
    initial_guess=1,
    tolerance=0.0001,
    maximum_iteration=50
)