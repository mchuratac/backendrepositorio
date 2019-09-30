import pymongo

class Conexion():

    def __init__(self, host="localhost", puerto="27017",base_datos="colegio"):
        self.host = host
        self.puerto = puerto
        self.base_datos = base_datos
        self.cliente=pymongo.MongoClient(f"mongodb://{self.host}:{self.puerto}/")
        self.respuesta = self.cliente[self.base_datos]
        print("Estas conectado")

    def conectar(self):
        return self.respuesta

    def cerrar (self):
        self.cliente.close()
        print ('Conexion cerrada')


'''
    host="127.0.0.1"
    puerto=27017
    cliente=pymongo.MongoClient(f"mongodb://{host}:{puerto}/")
    mybase=cliente["colegio"]py
    mycole=mybase["docentes"]

    docentesall=[{"Nombre":"pepe","Dni":9999666,"Edad":23},
    {"Nombre":"pepe","Dni":9999666,"Edad":23}]
    mycole.insert_many(docentesall)

   # print(mycole.insert_one(docentesall))
'''
"""
    def bdCliente(self):
        return self.cliente[self.base_datos]

    con = Conexion()
    bd = con.bdCliente()
    docentes = bd["docentes"]

   for docente in docentes.find():
        print(docente)
"""

       
'''
def obtener_bd():
    host='localhost'
    puerto=27017
    base_datos='colegio'
    cliente = MongoClient(f"mongodb://{host}:{puerto}")
    return cliente[base_datos]


db = obtener_bd()
lista = db['docentes'].find()

for listar in lista:
    print(listar)

'''



