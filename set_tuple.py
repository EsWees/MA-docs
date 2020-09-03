import string

set1 = set(string.digits[3:7] + string.digits[:5])
set2 = set(string.digits[3:7] + string.digits[6:])

tpl_inter = set1.intersection(set2)

tpl_diff1 = set1.difference(set2)
tpl_diff2 = set2.difference(set1)

print(f"set1={set1}")
print(f"set2={set2}")

print(f"tpl_inter={tpl_inter}")
print(f"tpl_diff1={tpl_diff1}")
print(f"tpl_diff2={tpl_diff2}")

# reverce tuple
set3 = tuple(set2)
print(set3[::-1])
print(set3)

print(list(set2))