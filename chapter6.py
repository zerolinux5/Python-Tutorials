def get_coach_data(filename):
        try:
                with open(filename) as f:
                        data = f.readline()
                return(data.strip().split(','))
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


sarah = get_coach_data('sarah2.txt')
(sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
print(sarah_name+"'s fastest times are: "+ str(sorted(set([sanitize(t) for t in sarah]))[0:3]))

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
