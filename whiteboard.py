# #Find Length
# #Given a list (arr1) and an integer (num1), return whether the length of the list is greater than the integer.

# Example:
# Input: arr1 = [1, 5, 7, 8, 9, 2], num1 = 5
# Output: True
# Explanation: the list arr1 has 6 values which is greater than 5.

# Input: arr1 = [29, 3, 2], num1 = 10
# Output: False
# Explanation: the list arr1 has 3 values in it which is not greater than 10.


def x(arr1, num1):
    return (len(arr1) > num1)


print(x([1, 5, 7, 8, 9, 2], 5))

print(x([29, 3, 2], 10))
