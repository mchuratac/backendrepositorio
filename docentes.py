from conn import Conexion

class Docentes():

    def __init__(self,nombre,apellidos,dni,edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.edad = edad

    def agregarDocente(self):
        try:
            conn = Conexion() 
            dbcliente = conn.conectar()    
            coleccion = dbcliente['docentes']
            diccionario = {"nombre":self.nombre, "apellidos":self.apellidos, "dni":self.dni, "edad":self.edad }       
            coleccion.insert_one(diccionario)
                               
        except Exception as e:
            print("error:" , str(e))
        else:
            conn.cerrar()
       
    def actualizarDocente (self, dni):
        try:
            conn = Conexion()
            dbcliente = conn.conectar()
            coleccion = dbcliente['docentes']
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


#AGREGAR
print ("################# REGISTRAR DOCENTES #################")
agregar = Docentes("Arvinder","Virk",87654321,28)
agregar.agregarDocente()

#BUSQUEDA
print ("################ BUSQUEDA DE DOCENTES #################")
obtener = Docentes("","","","")
obtener.obtenerDocente(43453578)
#ACTUALIZAR
print("################# ACTUALIZAR DOCENTES ##################")
actualizar = Docentes("Jeancarlos","Excelente profesor","77777777",30)
actualizar.actualizarDocente(87654321)

#ELIMINAR
print("################# ELIMINAR DOCENTES ##################")
eliminar = Docentes("","","","")
eliminar.eliminarDocente("43453583")

#LISTAR DOCENTE
print("################# LISTAR DOCENTES ##################")
mostrar = Docentes("","","","")
mostrar.mostrarDocente()
