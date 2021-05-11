# How do you remove duplicates from an array in place?

s = [3, 3, 66, 66, 3, 3, 4, 5, 5, 6, 66, 2, 1, 66]

seen = []
l = len(s)
i = 0
while i < l:
    if s[i] in seen:
        del s[i]
        l -= 1
    else:
        seen.append(s[i])
        i += 1

print(s)