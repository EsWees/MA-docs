print(f'hello world')

countries = {
    'Ukr': 'UA',
    'Israel': 'IL'
}

capitals = {
    'UA': 'Kiev',
    'IL': 'Jeruaslem'
}

countries['Italy'] = 'IT'
capitals['IT'] = 'Rome'

for key, value in countries.items():
    print(f'Domain for {key} is {value}')

for key in countries:
    print(f'Domain for {key} is {countries[key]}')

print(capitals.get('FR', ""))

capitals.setdefault('GR', "Frankfurt")

print(capitals.get('FR', ""))
print(capitals.get('GR', "ololo"))

print(capitals)







testinggggg = "asd kajs dlkjas ;lkjf;uj fr4kjnqf jbucvbnszv'gj"

counts = {}
for i in testinggggg:
    counts[i] = counts.get(i, 0) + 1

for i, n in counts.items():
    print(i, n)