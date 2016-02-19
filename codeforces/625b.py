gogol = raw_input()
pineapple = raw_input()

i = replaces = 0

while gogol.find(pineapple, i) != -1:
    found = gogol.find(pineapple, i)
    i = found + len(pineapple)
    replaces += 1

print(replaces)
