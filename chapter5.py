with open('james.txt') as jamesF:
	data = jamesF.readline()
james = data.strip().split(',')
with open('julie.txt') as julieF:
	data = julieF.readline()
julie = data.strip().split(',')
with open('mikey.txt') as mikeyF:
	data = mikeyF.readline()
mikey = data.strip().split(',')
with open('sarah.txt') as sarahF:
	data = sarahF.readline()
sarah = data.strip().split(',')

print(james)
print(julie)
print(mikey)
print(sarah)
