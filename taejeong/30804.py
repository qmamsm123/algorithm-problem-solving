from collections import defaultdict

N = int(input())
S = [int(i) for i in input().split()]

i, j = [0, 0]
sublist: defaultdict[int, int] = defaultdict(lambda: 0)
sublist[S[i]] += 1
max_length = 1
while True:
    # count the number of types in current sublist
    number_of_types = 0
    for (fruit, amount) in sublist.items():
        if amount > 0:
            number_of_types += 1
    # j-side expand if the number of types is less than or equal to 2
    if number_of_types <= 2:
        # update the max length by the length of current sublist
        current_length = 0
        for amount in sublist.values():
            current_length += amount
        if current_length > max_length:
            max_length = current_length

        j += 1
        if j < N:
            sublist[S[j]] += 1
        else:
            break
    # i-side shrink if the number of types is more than 2
    else:
        sublist[S[i]] -= 1
        i += 1
        if i >= j:
            break

print(max_length)
