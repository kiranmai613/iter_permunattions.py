import itertools

word = "cat"
perms = itertools.permutations(word, 3)

for perm in perms:
    print("".join(perm))
