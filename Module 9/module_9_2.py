first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(first_strings[i]) for i in range(len(first_strings)) if len(first_strings[i]) >= 5]
second_result = [(i, y) for i in first_strings for y in second_strings if len(i) == len(y)]
third_result = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)