full_list = []
old_list = []
count = 0

for _ in range(int(input())):
    if not full_list:
        full_list = ['F', 'A', 'C', 'E']
    new_list = input().split()
    if new_list == full_list[-4:][::-1]:
        full_list = full_list[:-4]
        count += 1
    else:
        full_list.extend(new_list)

print(count)
