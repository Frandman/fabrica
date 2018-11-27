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

# CONSTANTS

SE_GOC = 0.63
GAS_GEN = 0.23

# CRUD Methods on fichas

def create_ficha():
	pass

def insert_ficha(f):
	ficha_id = fichas.insert_one(f).inserted_id;
	print (ficha_id)
	return (ficha_id)

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


ficha = { "ref": "5035",
		  "name": "Mini Bag",
          "client": "ByFar",
          "season": "2019",
          "leather": "Matisse Lux Croc",
          "color": "Tan",
          "materials":[

          	{"type": "leather",
          	 "name":"Matisse Lux Croc";
          	 "ref": "",
          	 "uom": "p2",
          	 "precio": 3.8,
          	 "consumo":5.0,
          	 "proveedor":"Meridiana",
          	 "compra": True},

          	{"type":"hardware", 
          	 "name": "hebilla",
          	 "ref":"V512",
          	 "uom": "ud",
          	 "precio":0.8,
          	 "consumo":1
          	 "provedor":"F Sierra",
          	 "compra": True}],

          "tasks":[
            
            {"name": "corte piel",
             "precio": 0.015,
             "consumo": 10 }
          ]
}

insert_ficha(ficha)
