import re
from collections import Counter
correct_password_counter = 0
f = open("daytwo.txt", "r")
for line in f:

    line = line.split(sep=' ')

    nums = line[0].split(sep='-')
    under_bound, upper_bound = int(nums[0].strip()), int(nums[1].strip())
    char = line[1].strip()
    char = re.sub(r'[^\w]', ' ', char).strip()

    password = line[2]

    count = 0
    for c in password:
        if char == c:
            count = count + 1

    if count >= under_bound and count <= upper_bound:
        correct_password_counter = correct_password_counter + 1

print(correct_password_counter)


