import os
from pymongo import MongoClient
from dotenv import load_dotenv

def insertarDatos(array):
    load_dotenv()
    # Cadena de conexión a tu servidor MongoDB 
    URI = os.getenv("MONGODB_URLSTRING")

    # Crea una instancia del cliente MongoClient
    client = MongoClient(URI)

    # Accede a la base de datos deseada
    db = client.lavoz

    # Accede a una colección en la base de datos
    coleccion = db.lavoz
    for i in array:
        coleccion.insert_one(i)
    client.close()
