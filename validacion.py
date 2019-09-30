def validarNumero(tipoValidacion, peticion):
    while True:
        if tipoValidacion ==0: #numero entero en la edad
            try:
                numero = int(input(peticion))
                if numero >=0:
                    break
                else: print ("Dato fuera del rango permitido")
            except Exception:
                print ("Dato invalido")
        elif tipoValidacion ==1:#numero de notas
            try:
                numero = float(input(peticion))
                if numero >=0 and numero <=20:
                    break
                else: print ("Dato fuera de rango")

            except Exception:
                print ("Dato inválido")
    return numero          