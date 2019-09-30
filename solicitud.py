import validacion as v
from alumnos import Alumnos
from crudalumno import crudAlumnos




def registrarAlumnos():
    #Numero de alumnos a registrar
    peticion = "Ingrese numero de alumnos a registrar:"
    tipoValidacion = 0
    numeroAlumnos = v.validarNumero(tipoValidacion,peticion)
    
    #Numero de notas a registrar
    peticion = "Ingrese numero de notas a registrar por alumno:"
    tipoValidacion = 0 
    numeroNotas = v.validarNumero(tipoValidacion,peticion)
    #Registrar n alumnos
    for i in range(1,numeroAlumnos+1):
        print(f"Alumno nro. {i}:")
        datosAlumno = solicitarDatosAlumno()
        nombre = datosAlumno[0]
        apellidos = datosAlumno[1]
        dni = datosAlumno[2]
        edad = datosAlumno[3]
        notas = []
        for j in range(1,numeroNotas+1):
            peticion = f"Ingrese la nota {j}:"
            tipoValidacion=1
            notas.append(v.validarNumero(tipoValidacion,peticion))
        alumnos = Alumnos(nombre, apellidos,dni,edad,notas)
        nuevoAlumno = crudAlumnos()
        nuevoAlumno.agregarAlumno(alumnos)

def solicitarDatosAlumno():
    nombre = input ("Ingrese su nombre:")
    apellidos = input ("Ingrese sus apellidos:")
    dni = input ("Ingrese su numero de DNI:")
    peticion = "Ingrese su edad:"
    tipoValidacion=0
    edad = v.validarNumero(tipoValidacion,peticion)
    datos = [nombre, apellidos,dni,edad]
    return datos


def listarAlumnos():
    alumnos = crudAlumnos()
    alumnos.listarAlumnos

def actualizarAlumnos():
    alumnos = crudAlumnos()
    alumnos.actualizAlumnos(actualizAlumnos,dni_actualizar)


def eliminarAlumnos():
    alumnos = crudAlumnos()
    alumnos.eliminarAlumnos(dni_eliminar)


#AGREGAR
print("############ REGISTRAR ALUMNOS #####################")
registrarAlumnos()
print ("######### FIN DE REGISTRO #########################")

#LISTAR
print ("########### LISTADO DE ALUMNOS ####################")
#crudAlumnos().listarAlumnos()
print ("######### FIN DE REGISTRO #########################")


#ACTUALIZAR
print ("########## ACTUALIZAR ALUMNOS #####################")
#actualizarAlumnos = Alumnos("Jesus","Gracias amigo","43453578","26",[10,10,14] )
#crudAlumnos().actualizAlumnos(actualizarAlumnos,"43453578")

print ("######### FIN DE REGISTRO #########################")

#ELIMINAR
print ("############ ELIMINAR ALUMNOS #####################")
#crudAlumnos().eliminarAlumnos("78456396")
print ("######### FIN DE REGISTRO #########################")
