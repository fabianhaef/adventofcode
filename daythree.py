f = list(open("daythree.txt", "r"))

def solution_1():
	trees = 0
	size_row = len(f[0])-1

	for i in range(len(f)):
		location = f[i][i*3%size_row]
		if location == "#":
			trees += 1

	return trees

trees_one = solution_1()
print(trees_one)

with open("daythree.txt") as input:
    lines = input.readlines()
    counts = []
    for right, down in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        x = y = 0
        count = 0
        while y <= len(lines) - 1:
            loc = lines[y][x]
            if loc == "#":
                count += 1
            x = x + right
            if x >= len(lines[0]) - 1:
                x = x - len(lines[0]) + 1
            y = y + down
        counts.append(count)
    print(counts)
    ans = 1
    for count in counts:
        ans *= count
    print(ans)
