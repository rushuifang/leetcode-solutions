def permute(order, s):
    if order == 1:
        return s
    else:
        return [x + y for x in permute(1, s) for y in permute(order - 1, s)]


print(permute(1, ["a", "b", "c"]))
print(permute(2, ["a", "b", "c"]))
print(permute(3, ["a", "b", "c"]))
