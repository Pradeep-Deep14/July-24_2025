#Approach 1
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers=[4,2,9,7,5,6]
print(find_max(numbers))

# Output: 9

#Approach 2
def find_max(numbers):
    return max(numbers)

numbers=[4,2,9,7,5,6]
print(find_max(numbers))
# Output: 9