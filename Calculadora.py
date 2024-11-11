from decimal import Decimal, InvalidOperation

def es_decimal(cadena):
    try:
        Decimal(cadena)
        return True
    except InvalidOperation:
        return False
    


print("|******************************************************************************************|")
print("|                       CALCULADORA DE INDICE DE MASA CORPORAL  (IMC)                      |")
print("|******************************************************************************************|")
name = input(' Ingresa tu nombre: ')
if name == "":
    print(" Tienes que colocar tu nombre, intentalo de nuevo")
    exit()
else:
    pass
    
firts_name = input(' Ingresa tu apellido paterno: ')
if firts_name == "":
    print(" Tienes que colocar tu apellido paterno, intentalo de nuevo")
    exit()
else:
    pass

last_name = input(' Ingresa tu apellido materno: ')
if last_name == "":
    print(" Tienes que colocar tu apellido materno, intentalo de nuevo")
    exit()
else:
    pass

age = input(' Ingresa tu edad: ')
if age.isnumeric() :
    pass
else:
    print(" Ese no es un numero, vuelve a intentarlo")
    exit()

weight = input(' Ingresa la cifra de tu peso en kilogramos: ')
if es_decimal(weight) :
    pass
else:
    print(" Ingresa solo la cifra, vuelve a intentarlo")
    exit()

height = input(' Ingresa tu estatura en metros: ')
if es_decimal(height) :
    pass
else:
    print(" Ingresa solo la cifra, vuelve a intentarlo")
    exit()


imc = float(weight) / float(height) ** 2

print(" \n Tu nombre completo es: " + name + " " + firts_name + " " + last_name + " y tienes " + age + " años")
print(f" Tu IMC es {imc:1,.2f} \n")
print("|******************************************************************************************|")
