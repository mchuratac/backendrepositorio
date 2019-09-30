from alumnos import Alumnos
from conn import Conexion

class crudAlumnos():
    __conexion= Conexion()
    __con = __conexion.cliente

    def agregarAlumno(self,Alumnos):
        try: 
            nomColeccion = "alumnos"
            diccionario = {"nombre": Alumnos.nombre,"apellidos": Alumnos.apellidos,"dni": Alumnos.dni, "edad": Alumnos.edad,"notas": Alumnos.notas ,"notamaxima": Alumnos.getnotaMaxima(),"notaminima": Alumnos.getnotaMinima(),"promedio": Alumnos.getPromedio()}
            coleccion = self.__conexion.conectar() [nomColeccion]
            coleccion.insert_one(diccionario)
        except Exception as e:
            print("Error:", str(e))
        else:
            self.__conexion.cerrar()
    
    def listarAlumnos(self):
        try:
            nomColeccion = "alumnos"
            coleccion = self.__conexion.conectar() [nomColeccion]
            for x in coleccion.find():
                print (x)
        except Exception as e:
            print("Error:", str(e))
        else:
            self.__conexion.cerrar()
    
    def buscarAlumnos(self,dni_buscar):
        try:
            nomColeccion = "alumnos"
            coleccion = self.__conexion.conectar()[nomColeccion]
            query = {"dni":dni_buscar}
            alumnos = coleccion.find(query)
            return alumnos
        except Exception as e:
            print ("Error:", str(e))
        else:
            self.__conexion.cerrar()

    def actualizAlumnos (self,Alumnos ,dni_actualizar):
        try:
            nomColeccion = "alumnos"
            coleccion = self.__conexion.conectar()[nomColeccion]
            query = {"dni":dni_actualizar}
            queryUpdate = {"$set":{"nombre": Alumnos.nombre, "apellidos": Alumnos.apellidos, "edad": Alumnos.edad, "notas": Alumnos.notas, "notamaxima": Alumnos.getnotaMaxima(),"notaminima": Alumnos.getnotaMinima(), "promedio": Alumnos.getPromedio()}}
            coleccion.update(query,queryUpdate,upsert=False)
            print ("Registro Actualizado")
        except Exception as e:
            print ("Error:", str(e))
        else:
            self.__conexion.cerrar()
            
    def eliminarAlumnos(self,dni_eliminar):
        try:
            nomColeccion = "alumnos"
            coleccion = self.__conexion.conectar() [nomColeccion]
            query = {'dni':dni_eliminar}
            coleccion.remove(query)
            print("Registro Eliminado")
        except Exception as e:
            print("Error:",str(e))
        else:
            self.__conexion.cerrar()




