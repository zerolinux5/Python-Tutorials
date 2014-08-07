def get_coach_data(filename):
	try:
		with open(filename) as f:
			data = f.readline()
		temp = data.strip().split(',')
		return({'Name':temp.pop(0),
			'DOB':temp.pop(0),
			'Times':str(sorted(set([sanitize(t) for t in temp]))[0:3])})
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

def sanitize(times):
        if '-' in times:
                splitter = '-'
        elif ':' in times:
                splitter = ':'
        else:
                return(times)
        (mins, secs) = times.split(splitter)
        return(mins + '.' + secs)

"""
sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name+"'s fastest times are: "+ str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
"""

cleese = {}
palin = dict()
print(type(cleese))
print(type(palin))

cleese['Name'] = 'John Cleese'
cleese['Occupations'] = ['actor', 'comedian', 'writer', 'film producer']
palin = {'Name' : 'Michael Palin', 'Occupations': ['comedian', 'actor', 'writer', 'tv']}

print(palin['Name'])
print(cleese['Occupations'][-1])

palin['Birthplace'] = "Broomhill, Sheffield, England"
cleese['Birthplace'] = "Weston-super-Mare, North Somerset, England"

print(palin)
print(cleese)

"""
sarah = get_coach_data('sarah2.txt')
sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
print(sarah_data['Name'] + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]))
"""

james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey =  get_coach_data('mikey2.txt')
sarah =  get_coach_data('sarah2.txt')
print(james['Name'] + "'s fastest times are: " + james['Times'])
print(julie['Name'] + "'s fastest times are: " + julie['Times'])
print(mikey['Name'] + "'s fastest times are: " + mikey['Times'])
print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])

class Athlete:
	def __init__(self, a_name, a_dob = None, a_times=[]):
		self.name = a_name
		self.dob = a_dob
		self.times = a_times
sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')
print(type(sarah))
print(type(james))
print(sarah)
print(james)
print(sarah.name)
print(james.name)
print(sarah.dob)
print(james.dob)
print(sarah.times)
print(james.times)
