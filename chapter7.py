import pickle
from athletelist import AthleteList
import yate

def get_coach_data(filename):
        try:
                with open(filename) as f:
                        data = f.readline()
                temp = data.strip().split(',')
                return(AthleteList(temp.pop(0), temp.pop(0), temp))
        except IOError as ioerr:
                print('File error: ' + str(ioerr))
                return(None)

def put_to_store(files_list):
	all_athletes = {}
	for each_file in files_list:
		ath = get_coach_data(each_file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print('File error (put_and_store):' + str(ioerr))
	return(all_athletes)

def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle', 'rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print('File error (get_from_store):' + str(ioerr))
	return(all_athletes)


print(dir())

the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
print(data)

for each_athlete in data:
	print(data[each_athlete].name + ' ' + data[each_athlete].dob)

data_copy = get_from_store()
for each_athlete in data_copy:
	print(data_copy[each_athlete].name + ' ' + data_copy[each_athlete].dob)

print(yate.start_response())
print(yate.start_response("text/plain"))
print(yate.start_response("application/json"))
print(yate.include_header("Welcome to my home on the web!"))
print(yate.include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'}))
print(yate.include_footer({}))
print(yate.start_form("/cgi-bin/process-athlete.py"))
print(yate.end_form())
print(yate.end_form("Click to Confirm Your Order"))
for fab in ['John', 'Paul', 'George', 'Ringo']:
	print(yate.radio_button(fab, fab))
print(yate.u_list(['Life of Brian', 'Holy Grail']))
print(yate.header("Welcome to my home on the web"))
print(yate.header("This isa sub-sub-sub-sub-heading", 5))
print(yate.para("Was it worth the wait? We hope it was..."))
