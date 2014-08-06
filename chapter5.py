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

data = [6, 3, 1, 2, 4, 5]
print(data)
data2 = sorted(data)
print(data)
print(data2)

def sanitize(times):
	if '-' in times:
		splitter = '-'
	elif ':' in times:
		splitter = ':'
	else:
		return(times)
	(mins, secs) = times.split(splitter)
	return(mins + '.' + secs)

james2 = []
julie2 = []
mikey2 = []
sarah2 = []

for each_item in james:
	james2.append(sanitize(each_item))
for each_item in julie:
	julie2.append(sanitize(each_item))
for each_item in mikey:
	mikey2.append(sanitize(each_item))
for each_item in sarah:
	sarah2.append(sanitize(each_item))

print(sorted(james2))
print(sorted(julie2))
print(sorted(mikey2))
print(sorted(sarah2))
