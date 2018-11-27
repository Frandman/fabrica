# Test program for connecting to Mongodb

import pymongo
from pymongo import MongoClient

try:
	MONGO_DB_NAME="fabrica"
	MONGO_COLLECTION_NAME="fichas"
	fichas = MongoClient().fabrica.fichas
	#print("successful connection to fichas")
except:
	print('An error occurred on line {} in statement {}'.format(line, text))
	exit(1)

# CRUD Methods on fichas



def insert_ficha():
	pass

def edit_ficha():
	pass

def print_ficha():
	pass

def udpate_ficha():
	pass

def delete_ficha():
	pass

def get_price():
	pass

def main():
	pass

if __name__ == '__main__':
	main()