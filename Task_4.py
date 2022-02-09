a = [5, 2, 4, 23, 5235, 345]
b = [4, 1, 2, 5, 23, 3, 345]

same_things= list(set(a) & set(b))

print(f"We have first list named a: {a}\n")
print(f"And second list named b: {b}\n")
print(f"And third list that shows the same things in a and b list: {same_things}")
