# Python program to print positive Numbers in a List
 
def print_positive_numbers(lst):
    positive_numbers = []
    for num in lst:
        if num > 0:
            positive_numbers.append(num)
    return positive_numbers

# Example usage:
list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Positive numbers in list1: ", print_positive_numbers(list1))
print("Positive numbers in list2: ", print_positive_numbers(list2))
