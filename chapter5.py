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


mins = [1, 2, 3]
secs = [m*60 for m in mins]
print(secs)

meters = [1, 10, 3]
feet = [m * 3.281 for m in meters]
print(feet)

lower = ["I", "don't", "like", "spam"]
upper = [s.upper() for s in lower]
print(upper)

dirty = ['2-22', '2:22', '2.22']
clean = [sanitize(t) for t in dirty]
print(clean)

clean = [float(s) for s in clean]
print(clean)

clean = [float(sanitize(t)) for t in ['2-22', '3:33', '4.44']]
print(clean)

james3 = sorted([sanitize(t) for t in james])
julie3 = sorted([sanitize(t) for t in julie])
mikey3 = sorted([sanitize(t) for t in mikey])
sarah3 = sorted([sanitize(t) for t in sarah])

print(james3)
print(julie3)
print(mikey3)
print(sarah3)


james4 = []
julie4 = []
mikey4 = []
sarah4 = []

for each_t in james:
	if each_t not in james4:
		james4.append(each_t)
for each_t in julie:
	if each_t not in julie4:
		julie4.append(each_t)
for each_t in mikey:
	if each_t not in mikey4:
		mikey4.append(each_t)
for each_t in sarah:
	if each_t not in sarah4:
		sarah4.append(each_t)
print(james4[0:3])
print(julie4[0:3])
print(mikey4[0:3])
print(sarah4[0:3])

