D = [0, 1, 2, 3, 4, 5, 20, 7]

print(sum(x for i, x in enumerate(D) if i % 2 == 1))
print([2*x if x < 15 else x for x in D])
