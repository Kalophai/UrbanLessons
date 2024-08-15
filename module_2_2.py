first = int(input())
second = int(input())
third = int(input())
summary = 0
if first == second:
    summary = summary + 1
if first == third:
    summary = summary + 1
if second == third:
    summary = summary + 1
print(summary)