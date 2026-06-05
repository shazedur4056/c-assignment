# ============================================
# Assignment: Exponentiation using Iteration
# Name: Rahman Md Shazedur
# Student ID: M25W7502
# ============================================

# input
base_shazedur_M25W7502 = int(input("Enter base: "))
exponent_shazedur_M25W7502 = int(input("Enter exponent: "))

# initial value
result_shazedur_M25W7502 = 1
count_shazedur_M25W7502 = 0

# logic
if exponent_shazedur_M25W7502 == 0:
    result_shazedur_M25W7502 = 1

elif exponent_shazedur_M25W7502 > 0:
    while count_shazedur_M25W7502 < exponent_shazedur_M25W7502:
        result_shazedur_M25W7502 = result_shazedur_M25W7502 * base_shazedur_M25W7502
        count_shazedur_M25W7502 = count_shazedur_M25W7502 + 1

else:
    temp_exponent = -exponent_shazedur_M25W7502
    while count_shazedur_M25W7502 < temp_exponent:
        result_shazedur_M25W7502 = result_shazedur_M25W7502 * base_shazedur_M25W7502
        count_shazedur_M25W7502 = count_shazedur_M25W7502 + 1
    result_shazedur_M25W7502 = 1 / result_shazedur_M25W7502

# output
print("Result =", result_shazedur_M25W7502)