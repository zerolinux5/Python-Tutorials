movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])

"""
cast = ["Cleese", 'Palin', 'Jones', "Idle"]
print(cast)
print(len(cast))
print(cast[1])
cast.append("Gilliam")
print(cast)
cast.pop()
print(cast)
cast.extend(["Gilliam", "Chapman"])
print(cast)

cast.remove("Chapman")
print(cast)
cast.insert(0, "Chapman")
print(cast)
"""
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)
#print(movies)

fav_movies= ["The Holy Grail", "The Life of Brian"]

for each_flick in fav_movies:
	print(each_flick)

movies2 = ["The Holy Grail", 1975, "Terry Jones & Terry Filliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese", "Terry Filliam", "Eric Idle", "Terry Jones"]]]

print(movies2[4][1][3])
print(movies2)
for each_item in movies2:
	print(each_item)
"""
names = ['Michael', 'Terry']
print(isinstance(names, list))
num_names= len(names)
print(isinstance(num_names, list))
"""
for each_item in movies2:
	if(isinstance(each_item, list)):
		for nested_item in each_item:
			if(isinstance(nested_item, list)):
				for deeper_item in nested_item:
					print(deeper_item)
			else:
				print(nested_item)
	else:
		print(each_item)


print("\n");


def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)	

print_lol(movies2)
