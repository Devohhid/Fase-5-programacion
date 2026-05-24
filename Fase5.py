# Generador de informes de compromiso de clientes basado en matrices

# guarde estos datos en uan variable que llamare "sesiones" 
# para que guarde los datos de cada cliente, son ejemplos inventados con valores aleatorios

# Cada elemento de la matriz contiene en ID de cliente - segundos y clics
# Cada fila contiene esa informacion ordenadamente.
sesiones = [
    ["C001", 240, 12],
    ["C002", 45, 2],
    ["C003", 120, 5],
    ["C004", 300, 15],
    ["C005", 70, 1]
]

# Para la clasificación basadas en el ejercicio se realizan en esta seccion.

# Se usa def para definir uan funcion con ciertas reglas que clasificara cada cliente por niveles
# "clasificacion_nivel_de_compromiso" es el nombre de la función y el return será el resultado

def clasificacion_nivel_de_compromiso(duracion, clics): # en azul se resaltan los parametros que se usaran de las matrices
    # El ejercicio establece 3 reglas para clasificar el compromiso de los clientes:
    # 1. Si la duración es mayor a 180 segundos y los clics son mayores a 8 --> "Alto"
    # 2. Si la duración es menor a 60 segundos ó los clics son menores a 3 --> "Bajo"
    # 3. En cualquier otro caso --> "Medio" 

# regla # 1
    if duracion > 180 and clics > 8:
        return "Alto"
# regla # 2
    elif duracion < 60 or clics < 3:
        return "Bajo"
# regla # 3
    else:
        return "Medio"

# Resultados del informe de compromiso de clientes
print("++++++++++++++++++++++++++++++++++++++++++++++++++")
print(" INFORME DE COMPROMISO DE CLIENTES ")
print("++++++++++++++++++++++++++++++++++++++++++++++++++")

# estas lineas de codigo se realiza un ciclo linea a linea de la matriz o fila asi se realiza el ciclo por cada cleinte
for sesion in sesiones:
# Para la extraccion de datos se asigna una "ubicación" para que el codigo sepa que dato solicitamos
# 0, 1 y 2 indica la ubicacion del dato de izquierda a derecha. es decir 1,1; 1,2 y 1,3 respectivamente

    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]
# Llamamos a la función para obtener el dato de la función "clasificacion_nivel_de_compromiso"
    clasificacion = clasificacion_nivel_de_compromiso(duracion, clics)
# Impresion de resultados
# El uso de f" " permite formatear la cadena de texto para incluir variables dentro de ella, en este caso id_cliente y clasificacion

    print(f"Cliente: {id_cliente} --> Compromiso: {clasificacion}")                     

# Id cliente nos ayuda a identificar el cliente y clasificación nos da el resultado de su nivel de compromiso.
