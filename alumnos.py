from conn import Conexion

class Alumnos():
    def __init__(self,nombre,apellidos,dni,edad,notas):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad
        self.notas = notas

    
    def getnotaMaxima(self):
        notaMaxima= max(self.notas)
        return notaMaxima
    
    def getnotaMinima(self):
        notaMinima = min(self.notas)
        return notaMinima


    def getPromedio(self):
        suma=0
        numeroNotas = len(self.notas)
        for nota in self.notas:
            suma +=nota
        promedio = suma/numeroNotas
        return promedio


   
'''


class Alumnos():
    def __init__(self,nombre,dni,edad,notas,prom):
        self.nombre = nombre
        self.dni = dni
        self.edad = edad
        self.notas = notas
        self.prom = prom

    def agregarAlumnos(self):
        try:
            conn = Conexion()
            dbcliente = conn.conectar()
            coleccion = dbcliente['alumnos']
            diccionario = {''}

            
        except Exception as e:
            print ("error:", str(e))
        else:
            conn.cerrar()


 def actualizarAlumnos (self, dni):
        try:
            conn = Conexion()
            dbcliente = conn.conectar()
            coleccion = dbcliente['alumnos']
            query = {'dni': dni}
            queryset = {"$set":{'nombre': self.nombre , 'apellidos': self.apellidos, 'edad':self.edad}}
            coleccion.update_one(query, queryset)    
        except Exception as e:
            print ("error" , str(e))
        else:
            conn.cerrar()
    def obtenerDocente(self, dni):
        try:
            conn = Conexion()
            dbcliente = conn.conectar()
            coleccion = dbcliente['docentes']
            query = {"dni":self.dni}
            for x in coleccion.find(query):
                print (x)

        except Exception as e:
            print("error" , str(e))
        else:
            conn.cerrar()
    def eliminarDocente(self, dni):
        try:
            conn = Conexion()
            dbcliente = conn.conectar()
            coleccion = dbcliente['docentes']
            query = {'dni':dni}
            coleccion.remove(query)
        except Exception as e:
            print("error:" , str(e))
        else:
            conn.cerrar()

    def mostrarDocente (self):
        try:
            conn = Conexion()
            dbcliente = conn.conectar()
            coleccion = dbcliente['docentes']
            for x in coleccion.find():
                print (x)
        except Exception as e:
            print ("error", str(e))
        else:
            conn.cerrar()
'''