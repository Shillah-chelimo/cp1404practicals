# Question a
for increment_by_10 in range(0, 101, 10):
    print(increment_by_10, end=' ')
print()

# Question b
for countdown in range(20, 0, -1):
    print(countdown, end=' ')
print()

# Question c
num_stars = int(input("Number of stars: "))
for _ in range(num_stars):
    print('*', end='')
print()

# Question d
num_lines = int(input("Number of lines: "))
for line_number in range(1, num_lines + 1):
    print('*' * line_number)
