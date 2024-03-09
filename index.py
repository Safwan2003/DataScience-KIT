def reverse_word(word):
    rword = ''
    for i in range(len(word) - 1, -1, -1):
        rword += word[i]
    return rword

print(reverse_word("hello"))


def get_unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = get_unique_elements(sample_list)
print("Unique List:", unique_list)







def find_maximum(a, b, c):
    return max(a, b, c)

result = find_maximum(10, 5, 8)
print("Maximum of the three numbers is:", result)







def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

sample_list = [1, 2, 3, 4, 5]
total_sum = sum_of_list(sample_list)
print("Sum of the numbers in the list:", total_sum)
