import json
import math 

def save_to_file(data, file_name):
	with open(file_name, 'w') as write_file:
		#this also indents the dictionary 4 tabs in the output file
		json.dump(data, write_file, indent =4)
		print("The file was successfully created")


#Exercise 3: based on the slides presentation, write a function to read a file containing JSON object and output a dict
def read_from_file(file_name):
	with open(file_name, 'r') as read_file:
		data=json.load(read_file)
		return data


def append_to_file(data, file_name):
	with open(file_name, 'a') as write_file:
		#this also indents the dictionary 4 tabs in the output file
		json.dump(data, write_file, indent =4)
		print("The file was successfully appended to")






















