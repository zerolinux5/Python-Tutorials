import os
os.getcwd()
#os.chdir('~/Desktop/pythontuts/')
os.getcwd()
data = open('sketch.txt')
print(data.readline(), end='')
print(data.readline(), end='')
data.seek(0)
for each_line in data:
	print(each_line, end='')
data.close()

data = open('sketch.txt')
for each_line in data:
	if not each_line.find(':') == -1:
		(role, line_spoken) = each_line.split(':', 1)
		print(role, end='')
		print(' said: ', end='')
		print(line_spoken, end='')
data.close()

data = open('sketch.txt')

for each_line in data:
	try:
		(role, line_spoken) = each_line.split(':', 1)
		print(role, end='')
		print(' said ', end='')
		print(line_spoken, end='')
	except ValueError:
		pass

data.close()

if os.path.exists('sketch.txt'):
	data = open('sketch.txt')
	for each_line in data:
		if not each_line.find(':') == -1:
			(role, line_spoken) = each_line.split(':', 1)
			print(role, end='')
			print(' said: ', end='')
			print(line_spoken, end='')
	data.close()
else:
	print('The data file is missing!')

try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			print(role, end='')
			print(' said ', end='')
			print(line_spoken, end='')
		except ValueError:
			pass

	data.close()
except IOError:
	print('The data file is missing!')


