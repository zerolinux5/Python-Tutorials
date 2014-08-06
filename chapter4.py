import nester
import pickle

man = []
other = []
try:
	data = open('sketch.txt')
	for each_line in data:
		try:
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken = line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
		except ValueError:
			pass
	data.close()
except IOError:
	print('The datafile is missing!')

try:
	man_file = open('man_data.txt', 'w')
	other_file = open('other_data.txt', 'w')
	
	print(man, file=man_file)
	print(other, file=other_file)

except IOError as err:
	print('File error.' + str(err))
finally:
	man_file.close()
	other_file.close()

#Using standard with as block
try:
	with open('man_data.txt', 'w') as man_file:
		print(man, file=man_file)
	with open('other_data.txt', 'w') as other_file:
		print(other, file = other_file)
except IOErrror as err:
	print('File error:' + str(err))

#combining both withs into one line
try:
	with open('man_data.txt', 'w') as man_file,open('other_data.txt', 'w') as other_file:
		nester.print_lol(man, True, 0, fh=man_file)
		nester.print_lol(other, True, 0, fh=other_file)
except IOError as err:
	print('File error:' + str(err))

#Using pickle
try:
	with open('man_dataP.txt', 'wb') as man_file,open('other_dataP.txt', 'wb') as other_file:
		pickle.dump(man, man_file)
		pickle.dump(other, other_file)
except pickle.PickleError as perr:
	print('File error:' + str(perr))

new_man = []
try:
	with open('man_dataP.txt', 'rb') as man_file:
		new_man = pickle.load(man_file)
except IOError as err:
	print('File error: ' + str(err))
except pickle.PickleError as perr:
	print('Pickling error: ' + str(perr))
nester.print_lol(new_man, True, 0)
