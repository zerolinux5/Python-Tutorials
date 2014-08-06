""" This .py file gives a function called print_lol
    which prints all the nested lists of a list
    Arguments: a list
    Side Effects: prints to screen
"""
import sys

def print_lol(the_list, indent = False,  level = 0, fh=sys.stdout):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1, fh)
		else:
			if indent:
				for tabs in range(level):
					print("\t", end='', file=fh)
			print(each_item, file=fh)
