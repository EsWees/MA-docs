inp = open('MytestFile1', 'w')
inp.write("testing\n")
inp.close()

inp = open('MytestFile1', 'r+')
inp.seek(0)
print(f"r+\n{inp.read()}")
inp.close()

inp = open('MytestFile1', 'a+')
for i in range(12):
    inp.write(f"i={i}\n")

inp.seek(0)
print(inp.read())
inp.flush()
inp.close()

with open('MytestFile1', 'r') as f:
    print(f.read())

print(f.name)