from pymongo import MongoClient
import json
import certifi

ca= certifi.where()


######################################
# CARGAMOS ARCHIVO DE CONFIGURACION #
#####################################

def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

##################################
# CONECTAMOS A LA BASE DE DATOS #
################################

def dbConnection():
    dataconfig = loadConfigFile()
    try:
        #Server connection
        client = MongoClient(dataconfig['MONGO_URI_SERVER'],tlsCAFile=ca)
        #Local Connection
        #client = MongoClient(dataconfig['MONGO_URI_LOCAL'],dataconfig['LOCAL_PORT'])
        db=client["proyecto_ciclo_4"]
    except ConnectionError:
        print("Error de conexión con la base de datos")
    return db