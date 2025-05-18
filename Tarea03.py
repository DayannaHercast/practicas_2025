## Inicio de  Ejercicios de Pila


# Factorial de un número entero positivo
# factorial_pila(número)

def factorial_pila(número):
    """
    Función principal que calcula el factorial de un número entero positivo.
    E: número (int)
    S: El factorial del número
    R: número debe ser un entero positivo mayor o igual a 1
    """
    if type(número) != int:
        return "Error 01" 
    elif número < 1:
        return "Error 02"
    else:
        return factorial_aux(número)


def factorial_aux(número):
    """
    Función auxiliar recursiva que calcula el factorial.
    """
    if número == 1:
        return 1
    else:
        return número * factorial_aux(número - 1)

# Máximo común divisor de dos números
# mcd_pila(número1, número2)
def mcd_pila(número1, número2):
    """
    Función principal que calcula el máximo común divisor (MCD) de dos números
    usando el algoritmo de Euclides.
    E: número1 (int), número2 (int)
    S: El MCD de ambos números
    R: Ambos deben ser enteros. número1 >= 0, número2 > 0.
       No se permite que ambos números sean cero.
    """
    if type(número1) != int or type(número2) != int:
        return "E01"  # Tipos inválidos
    elif número1 < 0 or número2 <= 0:
        return "E02"  # Rango inválido
    elif número1 == 0 and número2 == 0:
        return "E03"  # El MCD no está definido si ambos son cero
    else:
        return mcd_aux(número1, número2)


def mcd_aux(número1, número2):
    """
    Función auxiliar que implementa el algoritmo de Euclides de forma recursiva.
    """
    if número1 % número2 != 0:
        return mcd_aux(número2, número1 % número2)
    else:
        return número2


# Eliminar un dígito de un número entero positivo
# eliminar_digito_pila(digito, número)
def eliminar_digito_pila(digito, número): 
    """
    Elimina todas las apariciones del dígito 'digito' en el número 'número'.

    E: número (int). Número del cual se eliminará el dígito.
       digito (int). Dígito que se desea eliminar del número.
    S: Número resultante sin el dígito indicado.
    R: número y digito deben ser enteros. 
       número debe ser mayor o igual que 0. 
       digito debe estar en el rango 0-9.
    """
    if type(número) != int or type(digito) != int:
        return "E01"  # Tipos inválidos
    elif número < 0 or digito < 0:
        return "E02"  # Valores negativos
    elif digito >= 10:
        return "E03"  # Dígito fuera de rango
    else:
        return eliminar_digito_aux(digito, número)


def eliminar_digito_aux(digito, número):
    """
    Función auxiliar que elimina las apariciones del dígito en el número.
    """
    if número == 0:
        return 0
    elif número % 10 == digito:
        return eliminar_digito_aux(digito, número // 10)
    else:
        return eliminar_digito_aux(digito, número // 10) * 10 + (número % 10)
    

# Invertir un número entero positivo
# invertir_número_pila(número)
def invertir_número_pila(número):
    """
    Invierte los dígitos de un número entero positivo.

    E: número (int). Número a invertir.
    S: Número invertido.
    R: número debe ser tipo int y mayor o igual que 0.
    """
    if type(número) != int:
        return "E01"  # Tipo inválido
    elif número < 0:
        return "E02"  # Número negativo
    else:
        return invertir_número_aux(número, calcular_potencia(número, 0))


def calcular_potencia(número, potencia):
    """
    Calcula la potencia de 10 correspondiente a la cantidad de dígitos menos 1.
    """
    if número < 10:
        return 1
    else:
        return 10 * calcular_potencia(número // 10, potencia)


def invertir_número_aux(número, potencia):
    """
    Función auxiliar que invierte un número usando recursión de pila,
    solo con parámetros.
    """
    if número < 10:
        return número * potencia
    else:
        return (número % 10) * potencia + invertir_número_aux(número // 10, potencia // 10)

# Contar la cantidad de veces que un dígito dado está presente en un número
# contar_dígito_pila(digito, número)
def contar_dígito_pila(digito, número):
    """
    Determina cuántas veces aparece un dígito en un número entero positivo.

    E:
    número: int. Número entero positivo en el que se buscará el dígito.
    digito: int. Dígito (entre 0 y 9) que se desea buscar en el número.

    S:
    int. Cantidad de veces que el dígito aparece en el número.

    R:
    número debe ser un número entero mayor o igual a 0.
    digito debe ser un número entero entre 0 y 9.
    """

    if type(número) != int or type(digito) != int:
        return "E01"  # Tipos inválidos
    elif número < 0 or digito < 0 or digito > 9:
        return "E02"  # Fuera de rango
    else:
        return contar_dígito_aux(digito, número)


def contar_dígito_aux(digito, número):
    """Función auxiliar recursiva de pila que cuenta las ocurrencias del dígito en el número."""

    if número == 0:
        return 0
    elif número % 10 == digito:
        return 1 + contar_dígito_aux(digito, número // 10)
    else:
        return contar_dígito_aux(digito, número // 10)



# Contar la cantidad de veces que un caracter dado está presente en un texto
# contar_caracter_pila(caracter, texto)

def contar_caracter_pila(caracter, texto):
    """
    Cuenta cuántas veces aparece un carácter en un texto.

    E:texto: str. Cadena en la que se buscará.
    caracter: str. Carácter a contar.

    S:int. Cantidad de apariciones del carácter.

    R:texto y caracter deben ser strings.
    caracter debe tener longitud 1.
    """

    if type(texto) != str or type(caracter) != str:
        return "E01"
    elif len(caracter) != 1:
        return "E02"
    elif len(texto) <= 0:
        return "E03"
    else:
        return contar_caracter_aux(caracter, texto)


def contar_caracter_aux(caracter, texto):
    """Función auxiliar."""

    if texto == "":
        return 0
    elif texto[0] == caracter:
        return 1 + contar_caracter_aux(caracter, texto[1:])
    else:
        return contar_caracter_aux(caracter, texto[1:])

# Eliminar una sección de un texto que está delimitada por dos índices enteros positivos válidos
# eliminar_sección_pila(inicio, final, texto)
def eliminar_sección_pila(inicio, final, texto):
    """
    Elimina la sección de un texto que está delimitada por dos índices enteros positivos válidos.

    E:
    texto: str. Cadena en la que se eliminará la sección.
    inicio, final: int. Índices de la sección a eliminar.

    S:
    str. Texto sin la sección indicada.

    R:
    texto debe ser un string no vacío.
    inicio y final deben ser enteros mayores o iguales a 0.
    """

    if type(texto) != str or texto == "":
        return "E01"
    elif type(inicio) != int or type(final) != int:
        return "E02"
    elif inicio < 0 or final < 0:
        return "E02-1"
    elif inicio >= final:
        return "E03"  # El índice de inicio debe ser menor que el índice final
    else:
        return eliminar_sección_aux(inicio, final, texto)


def eliminar_sección_aux(inicio, final, texto):
    """Función auxiliar para eliminar la sección delimitada."""

    if texto == "":
        return ""
    elif inicio > 0:
        return texto[0] + eliminar_sección_aux(inicio - 1, final - 1, texto[1:])
    elif final >= 0:
        return eliminar_sección_aux(inicio, final - 1, texto[1:])
    else:
        return texto[0] + eliminar_sección_aux(inicio, final, texto[1:])
    

# Eliminar la sección final de un texto a partir de un índice dado
# eliminar_final_pila(indice, texto)
def eliminar_final_pila(indice, texto):
    """
    Elimina la sección final de un texto a partir del índice dado.

    E:texto: str. Cadena original.
    indice: int. Índice desde el cual se eliminará el texto final, incluido.

    S:str. Cadena sin la sección final a partir del índice.

    R: texto debe ser string y no puede estar vacío.
    indice debe ser un entero mayor o igual a 0.
    """
    
    if type(texto) != str or type(indice) != int:
        return "E01"
    elif texto == "":
        return "E03"  # Error si el texto está vacío
    elif indice < 0:
        return "E02"
    else:
        return eliminar_final_aux(indice, texto)


def eliminar_final_aux(indice, texto):
    """Función auxiliar para eliminar la sección final a partir de un índice."""

    if indice == 0: 
        return "" 

    elif texto == "":  
        return texto

    else:  
        return texto[0] + eliminar_final_aux(indice - 1, texto[1:])
    
# Contar la cantidad de vocales presente en un texto
# contar_vocales_pila(texto)  # Solo minúsculas sin tilde
def contar_vocales_pila(texto):
    """
    Cuenta la cantidad de vocales en un texto.

    E:texto: str. Texto a evaluar.

    S:int. Número de vocales.

    R:texto no debe ser diferente de str ni estar vacío.
    """

    if type(texto) != str:
        return "E01"  # Error si el texto no es una cadena
    elif texto == "":
        return "E01-1"  # Error si el texto está vacío
    else:
        return contar_vocales_aux(texto)


def contar_vocales_aux(texto):
    """Función auxiliar que cuenta las vocales recursivamente."""

    if texto == "":  # Caso base: cuando no hay más texto
        return 0
    elif texto[0] == 'a' or texto[0] == 'e' or texto[0] == 'i' or texto[0] == 'o' or texto[0] == 'u':  # Si es una vocal
        return 1 + contar_vocales_aux(texto[1:])
    else:  # Si no es una vocal
        return contar_vocales_aux(texto[1:])
    

# Invertir un texto
# invertir_texto_pila(texto)

def invertir_texto_pila(texto):
    """
    Invierte una cadena de texto.

    E:texto: str. Cadena original.

    S: str. Cadena invertida.

    R: texto debe ser de tipo string y no debe estar vacío.
    """

    if type(texto) != str:
        return "E01"
    elif texto == "":
        return "E02"
    else:
        return invertir_texto_aux(texto)

def invertir_texto_aux(texto):
    """Función auxiliar que invierte recursivamente el texto."""

    if texto == "":
        return ""
    else:
        return invertir_texto_aux(texto[1:]) + texto[0]

# Determinar si un número es palíndromo
# es_número_palindromo_pila(número)
def es_número_palindromo_pila(número):
    """
    Función que determina si un número es palíndromo.

    E:numero: int. Número entero positivo.

    S: bool. True si el número es palíndromo, False si no.

    R:  numero debe ser de tipo int y no negativo.
    """
    if type(número) != int:
        return "E01"
    elif número < 0:
        return "E02"
    else:
        return es_número_palindromo_aux(número)


def es_número_palindromo_aux(numero):
    """
    Función auxiliar que compara el número con su versión invertida.
    """
    if numero == invertir_número_pila(numero):
        return True
    else: 
        return False



# Determinar si un texto es palíndromo
# es_texto_palindromo_pila(texto)

def es_texto_palindromo_pila(texto):
    """
    Verifica si un texto es un palíndromo.

    E:
    texto: str. Texto a evaluar.

    S:
    bool. True si es palíndromo, False si no.

    R:
    texto debe ser de tipo string y no estar vacío.
    """
    if type(texto) != str:
        return "E01"
    elif texto == "":
        return "E02"
    else:
        return es_texto_palindromo_aux(texto)


def es_texto_palindromo_aux(texto):
    """Función auxiliar."""
    if texto == invertir_texto_pila(texto):
        return True
    else: 
        return False

# Eliminar espacios de un texto
# eliminar_espacios_pila(texto)
def eliminar_espacios_pila(texto):
    """
    Elimina todos los espacios en blanco de una cadena de texto.

    E:texto: str. Cadena original.

    S:str. Cadena sin espacios.

    R:texto debe ser de tipo string y no debe estar vacío.
    """
    if type(texto) != str:
        return "E01"
    elif texto == "":
        return "E02"
    else:
        return eliminar_espacios_aux(texto)


def eliminar_espacios_aux(texto):
    """Función auxiliar."""
    if texto == "":
        return ""
    elif texto[0] == " ":
        return eliminar_espacios_aux(texto[1:])
    else:
        return texto[0] + eliminar_espacios_aux(texto[1:])


# Separar palabras de acuerdo a un carácter dado
# separar_palabras_pila(caracter, texto)

def separar_palabras_pila(caracter, texto):
    """
    Separa las palabras de un texto según un carácter dado, sin usar variables auxiliares.

    E: caracter: str de un solo carácter
       texto: str

    S: Lista de palabras separadas por el carácter

    R: texto debe ser str, caracter debe ser str y de un solo carácter
    """
    if type(texto) != str:
        return "E01"
    elif type(caracter) != str:
        return "E02"
    elif len(caracter) != 1:
        return "E03"
    else:
        return separar_palabras_pila_aux(caracter, texto)


def separar_palabras_pila_aux(caracter, texto):
    if texto == "":
        return []
    elif texto[0] == caracter:
        return [""] + separar_palabras_pila_aux(caracter, texto[1:])
    else:
        return [texto[0] + separar_palabras_pila_aux(caracter, texto[1:])[0]] + separar_palabras_pila_aux(caracter, texto[1:])[1:]


# Contar elementos presentes en una lista
# contar_elementos_pila(lista)
def contar_elementos_pila(lista):
    """
    Cuenta la cantidad de elementos en una lista.

    E:lista: list. Lista con elementos.

    S:int. Cantidad de elementos en la lista.

    R: lista debe ser de tipo list.
    """
    if type(lista) != list:
        return "E01"
    else:
        return contar_elementos_aux(lista)


def contar_elementos_aux(lista):
    """Función auxiliar."""

    if lista == []:
        return 0
    else:
        return 1 + contar_elementos_aux(lista[1:])


# Contar los elementos impares presentes en una lista
# contar_elementos_impares_pila(lista)

def contar_elementos_impares_pila(lista):
    """
    Cuenta la cantidad de números impares en una lista.

    E:
    lista: list. Lista con números enteros.

    S:
    int. Cantidad de números impares en la lista.

    R:
    lista debe ser de tipo list y contener solo enteros.
    """
    if type(lista) != list:
        return "E01"
    elif verificar_todos_enteros_pila(lista) == False:
        return "E02"
    else:
        return contar_elementos_impares_aux(lista)


def contar_elementos_impares_aux(lista):
    """Función auxiliar."""

    if lista == []:
        return 0
    elif lista[0] % 2 != 0:
        return 1 + contar_elementos_impares_aux(lista[1:])
    else:
        return contar_elementos_impares_aux(lista[1:])
    
#Ayuda a la funcion contar_elementos_impares
def verificar_todos_enteros_pila(lista):
    """
    Verifica si todos los elementos de una lista son enteros.

    E:lista: list. Lista a verificar.

    S:True si todos son enteros, False si hay al menos uno que no lo sea.

    R:lista debe ser de tipo list.
    """
    if type(lista) != list:
        return "E01"
    else:
        return verificar_todos_enteros_aux(lista)


def verificar_todos_enteros_aux(lista):
    """Función auxiliar estilo pila para verificar enteros."""
    if lista == []:
        return True
    elif type(lista[0]) == int:
        return verificar_todos_enteros_aux(lista[1:])
    else:
        return False
    
       
# Extraer los elementos pares presentes en una lista y retornarlos todos juntos en una lista
# extraer_elementos_pares_pila(lista)
def extraer_elementos_pares_pila(lista):
    """
    Extrae todos los números pares de una lista y los retorna en una nueva lista.

    E:lista: list. Lista con números enteros.

    S: list. Lista de números pares.

    R:lista debe ser de tipo list y contener solo enteros.
    """
    if type(lista) != list:
        return "E01"
    elif verificar_todos_enteros_pila(lista) == False:
        return "E02"
    else:
        return extraer_elementos_pares_aux(lista)


def extraer_elementos_pares_aux(lista):
    """Función auxiliar."""
    if lista == []:
        return []
    elif lista[0] % 2 == 0:
        return [lista[0]] + extraer_elementos_pares_aux(lista[1:])
    else:
        return extraer_elementos_pares_aux(lista[1:])


# Extraer los elementos impares presentes en una lista y retornarlos todos juntos en una lista
# extraer_elementos_impares_pila(lista)

def extraer_elementos_impares_pila(lista):
    """
    Extrae todos los números impares de una lista y los retorna en una nueva lista.

    E:lista: list. Lista con números enteros.

    S:list. Lista de números impares.

    R:lista debe ser de tipo list y contener solo enteros.
    """
    if type(lista) != list:
        return "E01"
    elif verificar_todos_enteros_pila(lista) == False:
        return "E02"
    else:
        return extraer_elementos_impares_aux(lista)


def extraer_elementos_impares_aux(lista):
    """Función auxiliar estilo pila."""
    if lista == []:
        return []
    elif lista[0] % 2 != 0:
        return [lista[0]] + extraer_elementos_impares_aux(lista[1:])
    else:
        return extraer_elementos_impares_aux(lista[1:])

# Separar los elementos pares e impares presentes en una lista -> [[1, 3, 5], [2, 4, 6]]
# separar_elementos_pares_impares_pila(lista)

def separar_elementos_pares_impares_pila(lista):
    """
    Separa los números pares e impares de una lista.

    E:lista: list. Lista con números enteros.

    S:list. Una lista que contiene dos listas: una con pares y otra con impares.

    R:lista debe ser tipo list y no debe estar vacía, y debe contener solo enteros.
    """
    if type(lista) != list:
        return "E01"
    elif lista == []:
        return "E02"
    elif verificar_todos_enteros_pila(lista) == False:
        return "E03"
    else:
         return [extraer_elementos_pares_pila(lista), extraer_elementos_impares_pila(lista)]


# Implementar una suma de conjuntos
# suma_conjuntos_pila(conjunto1, conjunto2)
def suma_conjuntos_pila(conjunto1, conjunto2):
    """
    Une dos conjuntos (listas) sin repetir elementos, usando recursividad de pila.

    E: conjunto1, conjunto2: list
    S: list. Unión sin repetidos.
    R: Ambas listas deben ser de tipo list.
    """
    if type(conjunto1) != list:
        return "E01"
    elif type(conjunto2) != list:
        return "E02"
    elif verificar_todos_numericos_pila(conjunto1):
        return "E03"
    elif verificar_todos_numericos_pila(conjunto2):
        return "E04"
    else:
        return eliminar_repetidos(conjunto1 + conjunto2)

def eliminar_repetidos(lista):
    """
    Elimina elementos repetidos en una lista
    """
    if lista == []:
        return []
    elif pertenece(lista[0], lista[1:]):
        return eliminar_repetidos(lista[1:])
    else:
        return [lista[0]] + eliminar_repetidos(lista[1:])

def pertenece(elemento, lista):
    """
    Verifica si un elemento ya está en la lista.
    """
    if lista == []:
        return False
    elif lista[0] == elemento:
        return True
    else:
        return pertenece(elemento, lista[1:])

    
# Multiplicar un escalar por un vector
#   multiplicar_escalar_vector_pila(escalar, vector)
def multiplicar_escalar_vector_pila(escalar, vector):
    """
    Función que multiplica un número por todos los elementos de una lista.

    E:
    escalar: int o float. Número a multiplicar.
    vector: list. Lista con elementos numéricos.

    S:
    list. Nueva lista con cada elemento multiplicado por el número.

    R:
    vector debe ser de tipo list.
    escalar debe ser de tipo int o float.
    """
    if type(vector) != list:
        return "E01"
    elif type(escalar) != int and type(escalar) != float:
        return "E02"
    elif escalar<0 or escalar>=10:
        return "E02"
    elif verificar_todos_numericos_pila(vector) != True:
        return "E03"
    else:
        return multiplicar_escalar_vector_pila_aux(escalar, vector)


def multiplicar_escalar_vector_pila_aux(escalar, vector):
    """Función auxiliar."""

    if vector == []:
        return []
    else:
        return [escalar * vector[0]] + multiplicar_escalar_vector_pila_aux(escalar, vector[1:])

# Verificar que todos los elementos de una lista sean numéricos
#   verificar_todos_numericos_pila(lista)
def verificar_todos_numericos_pila(lista):
    """
    Verifica si todos los elementos de una lista son NUMERICOS.

    E:lista: list. Lista a verificar.

    S:True si todos son int o float, False si hay al menos uno que no lo sea.

    R:lista debe ser de tipo list.
    """
    if type(lista) != list:
        return "E01"
    else:
        return verificar_todos_numericos_pila_aux(lista)

def verificar_todos_numericos_pila_aux(lista):
    """Función auxiliar estilo pila para verificar enteros."""
    if lista == []:
        return True
    elif type(lista[0]) == int or type(lista[0]) == float:
        return verificar_todos_numericos_pila_aux(lista[1:])
    else:
        return False
    
    
# Invertir una lista 
#   invertir_lista_pila(lista)
def invertir_lista_pila(lista):
    """
    Función que recibe una lista y la invierte.

    E:lista: list.

    S:list. La lista invertida.

    R:lista debe ser de tipo list.
    """
    if type(lista) != list:
        return "E01"
    elif len(lista)==0:
        return "E02"
    else:
        return invertir_lista_pila_aux(lista)


def invertir_lista_pila_aux(lista):
    """Función auxiliar."""

    if lista == []:
        return []
    else:
        return invertir_lista_pila_aux(lista[1:]) + [lista[0]]

# Buscar un texto dentro de otro
#   buscar_texto_pila(busca, texto)

def buscar_texto_pila(busca, texto):
    """
    Función que busca una subcadena 'busca' dentro de la cadena 'texto'.

    E:busca: str.
    texto: str.
    S: bool. True si se encuentra, False si no.
    R: Ambos deben ser de tipo str.
    """
    if type(busca) != str:
        return "E01"
    elif type(texto) != str:
        return "E02"
    else:
        return buscar_texto_pila_aux(busca, texto)


def buscar_texto_pila_aux(busca, texto):
    """Función auxiliar."""

    if texto == "":
        return False
    elif esta_al_inicio(busca, texto):
        return True
    else:
        return buscar_texto_pila_aux(busca, texto[1:])

def esta_al_inicio(busca, texto): 
    """
    Función que retorna True si 'busca' está al inicio de 'texto'.
    E:busca: str.
    texto: str.
    S: bool. True si 'busca' está al inicio de 'texto', False si no.
    R:Ambos parámetros deben ser de tipo str.
    """
    if type(busca) != str:
        return "E01"
    elif type(texto) != str:
        return "E02"
    else:
        return esta_al_inicio_aux(busca, texto)


def esta_al_inicio_aux(busca, texto):
    """Función auxiliar."""

    if busca == "":
        return True
    elif texto == "":
        return False
    elif busca[0] != texto[0]:
        return False
    else:
        return esta_al_inicio_aux(busca[1:], texto[1:])
    
# Dibujar un triángulo con asteriscos (en ambos sentidos)
#   dibujar_triangulo_pila(número)
def dibujar_triangulo_pila(número):
    """
    Dibuja un triángulo con asteriscos hacia abajo y luego hacia arriba, usando recursividad de pila.

    E: número impar positivo (int)
    S: Triángulo de asteriscos.
    R: El número debe ser impar, entero y mayor o igual a 1.
    """
    if type(número) != int:
        return "E01"
    elif número < 1:
        return "E02"
    elif número % 2 == 0:
        return "E03"
    else:
        return dibujar_pico(número, 0)

def dibujar_pico(n, espacio):
    """
    Dibuja recursivamente el triángulo hacia abajo y luego lo refleja al subir.
    """
    if n <= 0:
        return ""
    print("  " * espacio + "* " * n)
    dibujar_pico(n - 2, espacio + 1)
    print("  " * espacio + "* " * n)


# Dibujar un rectángulo con asteriscos
#   dibujar_rectangulo_pila(largo, ancho)
def dibujar_rectangulo_pila(largo, ancho):
    """
    Función que dibuja un rectángulo con asteriscos.
    
    E: Dos números como largo y ancho.
    S: Los asteriscos con forma de rectángulo.
    R: No puede ser diferente de int, positivo y largo != ancho.
    """
    if type(largo) != int:
        return "EO1"
    elif type(ancho) != int:
        return "EO2"
    elif largo <= 0 or ancho <= 0:
        return "EO3"
    elif largo == ancho:
        return "EO4"
    else:
        return dibujar_rectangulo_aux(largo, ancho)

def dibujar_rectangulo_aux(largo, ancho):
    """
    Función auxiliar que dibuja el rectángulo de asteriscos.
    """
    if ancho == 0:
        return ""
    else:
        print(" * " * largo)
        return dibujar_rectangulo_aux(largo, ancho - 1)

# Permutaciones de una lista [1,2] [4, 5] -> [[1,4],[1,5],[2,4],[2,5]]
#   permutaciones_pila(lista1, lista2)
def permutaciones_pila(lista1, lista2):
    """
    Función principal que genera permutaciones entre dos listas.
    
    E: lista1 y lista2 deben ser listas.
    S: Lista con todas las permutaciones [[a,b],...]
    R: Ambos parámetros deben ser tipo list.
    """
    if type(lista1) != list or type(lista2) != list:
        return "E01"

    else:
        return permutaciones_externas(lista1, lista2)

def permutaciones_externas(lista1, lista2):
    """
    Recorre externamente la lista1, generando subpermutaciones con lista2.
    """
    if lista1 == []:
        return []
    else:
        return permutaciones_internas([lista1[0]], lista2) + permutaciones_externas(lista1[1:], lista2)

def permutaciones_internas(elem, lista2):
    """
    Para un elemento dado de lista1, lo combina con cada elemento de lista2.
    """
    if lista2 == []:
        return []
    else:
        return [elem + [lista2[0]]] + permutaciones_internas(elem, lista2[1:])
    

## Final de  Ejercicios de Pila

#############################################


## Inicio de  Ejercicios de Cola

# Factorial de un número entero positivo
# factorial_cola(número)
def factorial_cola(número):
    """ 
    Función que calcula el factorial de un número.
    E: Un número entero int
    S: El factorial de ese número
    R: Tiene que ser tipo int y positiv
    """
    if type(número) != int:
        return "Error 01"  # El valor no es un entero

    elif número < 0:
        return "Error 02"  # El número es negativo

    elif número == 0:
        return 1  # Caso base especial para 0! = 1

    else:
        return factorial_aux(número, 1)

def factorial_aux(número, resultado):
    "Función Auxiliar"
    if número == 1:
        return resultado
    else:
        return factorial_aux(número - 1, resultado * número)


# Máximo común divisor de dos números
# mcd_cola(número1, número2)
def mcd_cola(número1, número2):
    """
    Función que calcula el máximo común divisor de dos números.
    E: Dos números enteros
    S: El MCD de esos dos números
    R: No puede ser diferente de int y tampoco negativo
    """
    if type(número1) != int or type(número2) != int:
        return "Error 01"  # Los valores deben ser enteros

    elif número1 < 0 or número2 < 0:
        return "Error 02"  # No se permiten negativos

    elif número1 < número2:
        return "Error 03"  # Se espera que el primer número sea mayor o igual al segundo

    else:
        return mcd_aux(número1, número2)

def mcd_aux(número1, número2):
    """Función Auxiliar que aplica el algoritmo de Euclides"""
    if número2 == 0:
        return número1
    else:
        return mcd_aux(número2, número1 % número2)


# Eliminar un dígito de un número entero positivo
# eliminar_digito_cola(digito, número)
def eliminar_digito_cola(digito, número):
    """
    Función principal que elimina el dígito dado de un número.
    E: número (int), dígito (int)
    S: número con el dígito eliminado
    R: Ambos deben ser enteros, el número debe ser positivo, el dígito entre 0 y 9
    """
    if type(número) != int or type(digito) != int:
        return "Error 01"  # Tipos inválidos

    elif número < 0 or digito < 0 or digito >= 10:
        return "Error 02"  # Rango inválido

    else:
        return eliminar_digito_aux(digito, número, 0, 1)

def eliminar_digito_aux(digito, número, resultado, elevado):
    """
    Función auxiliar con parámetros en el mismo orden que la principal.
    """
    if número == 0:
        return resultado

    elif número % 10 == digito:
        return eliminar_digito_aux(digito, número // 10, resultado, elevado)

    else:
        return eliminar_digito_aux(digito, número // 10, resultado + (número % 10) * elevado, elevado * 10)

# Invertir un número entero positivo
# invertir_número_cola(número)
def invertir_número_cola(número):
    """
    Función que invierte un número.
    E: número int a invertir
    S: número int invertido
    R: número debe ser tipo int y positivo
    """
    if type(número) != int:
        return "Error 01"  # No es entero

    elif número < 0:
        return "Error 02"  # Es negativo

    else:
        return invertir_número_aux(número, 0)

def invertir_número_aux(número, resultado):
    """Función auxiliar"""
    if número == 0:
        return resultado
    else:
        return invertir_número_aux(número // 10, resultado * 10 + número % 10)


# Contar la cantidad de veces que un dígito dado está presente en un número
# contar_dígito_cola(digito, número)
def contar_dígito_cola(digito, número):
    """
    Función que cuenta cuántas veces aparece un dígito en un número.
    E: dígito (int), número (int)
    S: número de apariciones del dígito
    R: número y dígito deben ser enteros, no negativos, y dígito debe estar entre 0 y 9.
    """
    if type(número) != int or type(digito) != int:
        return "E01"
    elif número < 0 or digito < 0:
        return "E02"
    elif digito > 9:
        return "E03"
   
    else:
        return contar_dígito_aux(digito, número, 0)

def contar_dígito_aux(digito, número, resultado):
    """Función Auxiliar"""
    if número == 0:
        return resultado
    elif número % 10 == digito:
        return contar_dígito_aux(digito, número // 10, resultado + 1)
    else:
        return contar_dígito_aux(digito, número // 10, resultado)


# Contar la cantidad de veces que un caracter dado está presente en un texto
# contar_caracter_cola(caracter, texto)
def contar_caracter_cola(caracter, texto):
    """
    Función que cuenta cuántas veces aparece un carácter en un texto.
    E: texto (str), caracter (str de un solo carácter)
    S: número de apariciones del caracter
    R: texto y caracter deben ser str, caracter debe tener longitud 1.
    """
    if type(texto) != str or type(caracter) != str:
        return "E01"
    elif len(caracter) != 1:
        return "E02"
    else:
        return contar_caracter_aux(caracter, texto, 0, len(texto), 0)

def contar_caracter_aux(caracter, texto, indice, largo, resultado):
    """Función Auxiliar"""
    if indice == largo:
        return resultado
    elif texto[indice] == caracter:
        return contar_caracter_aux(caracter, texto, indice + 1, largo, resultado + 1)
    else:
        return contar_caracter_aux(caracter, texto, indice + 1, largo, resultado)


# Eliminar una sección de un texto que está delimitada por dos índices enteros positivos válidos
# eliminar_sección_cola(inicio, final, texto)
def eliminar_sección_cola(inicio, final, texto):
    """
    Función que elimina una sección de un texto entre dos índices (inclusive).
    E: inicio (int), final (int), texto (str)
    S: texto resultante sin la sección entre los índices
    R: texto debe ser str, inicio y final deben ser int, mayores o iguales a 0 y en orden.
    """
    if type(texto) != str:
        return "E01"
    elif type(inicio) != int or type(final) != int:
        return "E02"
    elif inicio < 0 or final < 0:
        return "E03"
    elif inicio > final:
        return "E04"
    elif final >= len(texto):
        return "E05"
    else:
        return eliminar_sección_aux(inicio, final, texto, 0, "")

def eliminar_sección_aux(inicio, final, texto, contador, resultado):
    """Función Auxiliar"""
    if contador == len(texto):
        return resultado
    elif contador < inicio:
        return eliminar_sección_aux(inicio, final, texto, contador + 1, resultado + texto[contador])
    elif contador > final:
        return eliminar_sección_aux(inicio, final, texto, contador + 1, resultado + texto[contador])
    else:
        return eliminar_sección_aux(inicio, final, texto, contador + 1, resultado)


# Eliminar la sección final de un texto a partir de un índice dado
# eliminar_final_cola(indice, texto)
def eliminar_final_cola(indice, texto):
    """
    Función que elimina desde una posición final del texto
    E: índice (int) y texto (str)
    S: El texto sin los caracteres finales desde el índice
    R: texto debe ser str, índice debe ser int y positivo, y no mayor que el largo del texto
    """
    if type(texto) != str:
        return "E01"
    elif type(indice) != int:
        return "E02"
    elif indice < 0:
        return "E03"
    elif indice > len(texto):
        return "E04"
    else:
        return eliminar_final_aux(indice, texto, 0, "")

def eliminar_final_aux(indice, texto, recorrido, resultado):
    """Función Auxiliar"""
    if recorrido == indice:
        return resultado
    else:
        return eliminar_final_aux(indice, texto, recorrido + 1, resultado + texto[recorrido])


# Contar la cantidad de vocales presente en un texto
# contar_vocales_cola(texto)  # Solo minúsculas sin tilde
def contar_vocales_cola(texto):
    """Función que cuenta la cantidad de vocales que tiene un texto
    E: texto (str)
    S: la cantidad de vocales que aparecen en el texto
    R: texto debe ser str, solo se cuentan las vocales minúsculas sin tilde
    """
    if type(texto) != str:
        return "E01"  # Error si el texto no es un string
    else:
        return contar_vocales_aux(texto, len(texto), 0, 0)

def contar_vocales_aux(texto, largo, indice, resultado):
    """Función Auxiliar que cuenta vocales usando índice."""
    if indice == largo:
        return resultado
        
    elif texto[indice] == "a" or texto[indice] == "e" or texto[indice] == "i" or texto[indice] == "o" or texto[indice] == "u":
        return contar_vocales_aux(texto, largo, indice + 1, resultado + 1)
    else:
        return contar_vocales_aux(texto, largo, indice + 1, resultado)

# Invertir un texto
# invertir_texto_cola(texto)
def invertir_texto_cola(texto):
    """
    Función principal que invierte un texto validando el tipo.
    E: Un texto (str)
    S: El texto invertido
    R: Debe ser de tipo str
    """
    if type(texto) != str:
        return "E01"  # Error si el texto no es un string
    else:
        return invertir_texto_auxiliar(texto, len(texto), 0, "")

def invertir_texto_auxiliar(texto, largo_texto, indice, resultado):
    """
    Función auxiliar para invertir el texto usando índices.
    """
    if largo_texto == indice:
        return resultado
    else:
        return invertir_texto_auxiliar(texto, largo_texto, indice+1, texto[indice]+resultado)

# Determinar si un número es palíndromo
# es_número_palindromo_cola(número)
def es_número_palindromo_cola(número):
    """
    Función que verifica si un número es palíndromo.
    E: Un número entero
    S: True si es palíndromo, False si no
    R: Debe ser de tipo int y positivo
    """
    if type(número) != int:
        return "E01"  # Error si el número no es un entero
    elif número < 0:
        return "E02"  # Error si el número es negativo
    else:
        return es_número_palindromo_aux(número)

def es_número_palindromo_aux(número):
    """Función Auxiliar"""
    if invertir_número_cola(número) == número:
        return True
    else:
        return False

# Determinar si un texto es palíndromo
# es_texto_palindromo_cola(texto)
def es_texto_palindromo_cola(texto):
    """
    Función que verifica si un texto es palíndromo.
    E: Un texto (str)
    S: True si es palíndromo, False si no
    R: Debe ser de tipo str
    """
    if type(texto) != str:
        return "E01"  # Error si el texto no es una cadena
    else:
        return es_texto_palindromo_aux(texto)

def es_texto_palindromo_aux(texto):
    """Función Auxiliar"""
    if invertir_texto_cola(texto) == texto:
        return True
    else:
        return False
    
# Eliminar espacios de un texto
# eliminar_espacios_cola(texto)
def eliminar_espacios_cola(texto):
    """
    Función que elimina todos los espacios de un texto.
    E: Un texto str
    S: El texto sin espacios
    R: texto debe ser de tipo str
    """
    if type(texto) != str:
        return "E01"
    else:
        return eliminar_espacios_aux(texto, 0, len(texto), "")

def eliminar_espacios_aux(texto, indice, largo, resultado):
    """Función Auxiliar"""
    if indice == largo:
        return resultado
    elif texto[indice] == " ":
        return eliminar_espacios_aux(texto, indice + 1, largo, resultado)
    else:
        return eliminar_espacios_aux(texto, indice + 1, largo, resultado + texto[indice])

# Separar palabras de acuerdo a un carácter dado
# separar_palabras_cola(caracter, texto)
def separar_palabras_cola(caracter, texto):
    """
    Función principal para separar palabras según un carácter dado.
    E: caracter (str de un solo carácter), texto (str)
    S: Lista de palabras separadas
    R: texto debe ser str, caracter debe ser str y de un solo carácter
    """
    if type(texto) != str:
        return "E01"
    elif type(caracter) != str:
        return "E02"
    elif len(caracter) != 1:
        return "E03"
    else:
        return separar_palabras_aux(caracter, texto, len(texto), 0, "", [])

def separar_palabras_aux(caracter, texto, largo, indice, palabra_actual, resultado):
    """Función Auxiliar"""
    if indice == largo:
        if palabra_actual != "":
            return resultado + [palabra_actual]
        else:
            return resultado
    elif texto[indice] == caracter:
        return separar_palabras_aux(caracter, texto, largo, indice + 1, "", resultado + [palabra_actual])
    else:
        return separar_palabras_aux(caracter, texto, largo, indice + 1, palabra_actual + texto[indice], resultado)


# Contar elementos presentes en una lista
# contar_elementos_cola(lista)
def contar_elementos_cola(lista):
    """
    Función que cuenta los elementos de una lista.
    E: Una lista
    S: Un número entero representando la cantidad de elementos
    R: Debe ser tipo list, no vacía y contener solo números
    """
    if type(lista) != list:
        return "E01"
    elif len(lista) == 0:
        return "E02"
    elif verificar_todos_numericos_cola_ayuda(lista) != True:
        return "E03"
    else:
        return contar_elementos_aux(lista, len(lista), 0, 0)

def contar_elementos_aux(lista, largo, indice, resultado):
    """Función Auxiliar"""
    if largo == indice:
        return resultado
    else:
        return contar_elementos_aux(lista, largo, indice + 1, resultado + 1)
#AYUDA A CONTAR QUE TODOS SEAN NUMERICOS 
def verificar_todos_numericos_cola_ayuda(lista):
    """
    Función que verifica si todos los elementos de una lista son int o float.
    E: Una lista
    S: True si todos los elementos son int o float, False en caso contrario
    R: La entrada debe ser de tipo list
    """
    if type(lista) != list:
        return "E01"
    else:
        return verificar_todos_numericos_aux(lista, len(lista), 0)

def verificar_todos_numericos_aux(lista, largo, indice):
    """
    Función auxiliar para verificar elementos numéricos.
    """
    if indice == largo:
        return True
    elif type(lista[indice]) == int or type(lista[indice]) == float:
        return verificar_todos_numericos_aux(lista, largo, indice + 1)
    else:
        return False
# Contar los elementos impares presentes en una lista
# contar_elementos_impares_cola(lista)

def contar_elementos_impares_cola(lista):
    """
    Función que cuenta los elementos impares en una lista.
    E: Una lista
    S: Un número entero representando la cantidad de impares
    R: Debe ser de tipo list con elementos numéricos
    """
    if type(lista) != list:
        return "E01"
    elif verificar_todos_enteros(lista) != True:
        return "E02"
    else:
        return contar_elementos_impares_cola_aux(lista, len(lista), 0, 0)

def contar_elementos_impares_cola_aux(lista, largo, indice, acumulador):
    """Función auxiliar con cola para contar impares"""
    if indice == largo:
        return acumulador
    elif type(lista[indice]) == int and lista[indice] % 2 == 1:
        return contar_elementos_impares_cola_aux(lista, largo, indice + 1, acumulador + 1)
    else:
        return contar_elementos_impares_cola_aux(lista, largo, indice + 1, acumulador)

#AYUDA A CONTAR LOS NUMEROS ENTEROS DE UNA LISTA
def verificar_todos_enteros(lista):
    """
    Función que verifica si todos los elementos de una lista son int.
    E: Una lista
    S: True si todos los elementos son int o float, False en caso contrario
    R: La entrada debe ser de tipo list
    """
    if type(lista) != list:
        return "E01"
    else:
        return verificar_todos_enteros_aux(lista, len(lista), 0)

def verificar_todos_enteros_aux(lista, largo, indice):
    """
    Función auxiliar para verificar elementos numéricos.
    """
    if indice == largo:
        return True
    elif type(lista[indice]) == int:
        return verificar_todos_enteros_aux(lista, largo, indice + 1)
    else:
        return False

# Extraer los elementos pares presentes en una lista y retornarlos todos juntos en una lista
# extraer_elementos_pares_cola(lista)

def extraer_elementos_pares_cola(lista):
    """
    Función que retorna una lista con los elementos pares de la lista original.
    E: Una lista de enteros
    S: Una lista con los números pares
    R: La entrada debe ser de tipo list. Todos los elementos deben ser int.
    """
    if type(lista) != list:
        return "E01"
    elif verificar_todos_enteros(lista) != True:
        return "EO2"
    else:
        return extraer_elementos_pares_cola_aux(lista, len(lista), 0, [])

# Función auxiliar
def extraer_elementos_pares_cola_aux(lista, largo, indice, resultado):
    """
    Función auxiliar para construir una nueva lista con los elementos pares.
    """
    if indice == largo:
        return resultado
    elif lista[indice] % 2 == 0:
        return extraer_elementos_pares_cola_aux(lista, largo, indice + 1, resultado + [lista[indice]])
    else:
        return extraer_elementos_pares_cola_aux(lista, largo, indice + 1, resultado)


# Extraer los elementos impares presentes en una lista y retornarlos todos juntos en una lista
# extraer_elementos_impares_cola(lista)
def extraer_elementos_impares_cola(lista):
    """
    Función que retorna una lista con los elementos impares de la lista original.
    E: Una lista de enteros
    S: Una lista con los números impares
    R: La entrada debe ser de tipo list. Todos los elementos deben ser int.
    """
    if type(lista) != list:
        return "E01"
    elif verificar_todos_enteros(lista) != True:
        return "EO2"
    else:
        return extraer_elementos_impares_cola_aux(lista, len(lista), 0, [])

# Función auxiliar
def extraer_elementos_impares_cola_aux(lista, largo, indice, resultado):
    """
    Función auxiliar que construye la lista de impares.
    """
    if indice == largo:
        return resultado
    elif lista[indice] % 2 == 1:
        return extraer_elementos_impares_cola_aux(lista, largo, indice + 1, resultado + [lista[indice]])
    else:
        return extraer_elementos_impares_cola_aux(lista, largo, indice + 1, resultado)

# Separar los elementos pares e impares presentes en una lista -> [ [1,3,5], [2,4,6] ]
# separar_elementos_pares_impares_cola(lista)
def separar_elementos_pares_impares_cola(lista):
    """
    Función que retorna una lista que contiene dos listas: una de impares y otra de pares.
    E: Una lista de enteros
    S: Una lista [impares, pares]
    R: La entrada debe ser de tipo list. Todos los elementos deben ser int.
    """
    if type(lista) != list:
        return "E01"
    elif verificar_todos_enteros(lista) != True:
        return "E02"
    else:
        return separar_elementos_pares_impares_aux(lista, len(lista), 0, [], [])

# Función auxiliar
def separar_elementos_pares_impares_aux(lista, largo, indice, impares, pares):
    """
    Función auxiliar que separa los elementos impares y pares en listas diferentes.
    """
    if indice == largo:
        return [impares, pares]
    elif lista[indice] % 2 == 0:
        return separar_elementos_pares_impares_aux(lista, largo, indice + 1, impares, pares + [lista[indice]])
    else:
        return separar_elementos_pares_impares_aux(lista, largo, indice + 1, impares + [lista[indice]], pares)


# Implementar una suma de conjuntos
# suma_conjuntos_cola(conjunto1, conjunto2)
def suma_conjuntos_cola(conjunto1, conjunto2): 
    """
    Función principal que une dos listas (conjuntos) sin repetir elementos.
    E: conjunto1 y conjunto2 deben ser listas de enteros
    S: Una lista unificada sin repeticiones
    R: Ambas entradas deben ser listas. Todos los elementos deben ser enteros.
    """
    if type(conjunto1) != list or type(conjunto2) != list:
        return "E01"
    elif verificar_todos_enteros(conjunto1) != True or verificar_todos_enteros(conjunto2) != True:
        return "E02"
    else:
        return suma_conjuntos_aux(conjunto1, conjunto2, [], 0, 0, len(conjunto1), len(conjunto2))

def suma_conjuntos_aux(lista1, lista2, resultado, indice1, indice2, largo1, largo2):
    """
    Función auxiliar que concatena dos listas sin duplicar elementos (no importa si son consecutivos o no).
    """
    if indice1 == largo1 and indice2 == largo2:
        return resultado

    if indice1 < largo1:
        if verificar_repetido(resultado, lista1[indice1], len(resultado), 0) == False:
            return suma_conjuntos_aux(lista1, lista2, resultado + [lista1[indice1]], indice1 + 1, indice2, largo1, largo2)
        else:
            return suma_conjuntos_aux(lista1, lista2, resultado, indice1 + 1, indice2, largo1, largo2)

    if indice2 < largo2:
        if verificar_repetido(resultado, lista2[indice2], len(resultado), 0) == False:
            return suma_conjuntos_aux(lista1, lista2, resultado + [lista2[indice2]], indice1, indice2 + 1, largo1, largo2)
        else:
            return suma_conjuntos_aux(lista1, lista2, resultado, indice1, indice2 + 1, largo1, largo2)

def verificar_repetido(lista, elemento, largo, indice):
    """
    Verifica si un elemento ya existe en la lista sin usar 'in'.
    """
    if indice == largo:
        return False
    elif lista[indice] == elemento:
        return True
    else:
        return verificar_repetido(lista, elemento, largo, indice + 1)


# Multiplicar un escalar por un vector
# multiplicar_escalar_vector_cola(escalar, vector)
def multiplicar_escalar_vector_cola(escalar, vector):
    """
    Función que escala un vector (lista de enteros) por un escalar.
    E: Un escalar (int) y un vector (list de int)
    S: Una nueva lista con los elementos escalados
    R: vector debe ser lista de enteros, escalar debe ser entero
    """
    if type(vector) != list  and type(vector) != float:
        return "E01"
    elif type(escalar) != int and type(escalar) != float:
        return "E02"
    elif verificar_todos_numericos_cola_ayuda(vector) != True:
        return "E03"
    return multiplicar_escalar_aux(escalar, vector, len(vector), 0, [])

def multiplicar_escalar_aux(escalar, vector, largo_v, indice, resultado):
    """
    Función auxiliar que multiplica cada elemento del vector por el escalar.
    """
    if indice == largo_v:
        return resultado
    else:
        return multiplicar_escalar_aux(escalar, vector, largo_v, indice + 1, resultado + [vector[indice] * escalar])


# Verificar que todos los elementos de una lista sean numéricos
# verificar_todos_numéricos_cola(lista)
def verificar_todos_numéricos_cola(lista):
    """
    Función que verifica si todos los elementos de una lista son int o float.
    E: Una lista
    S: True si todos los elementos son int o float, False en caso contrario
    R: La entrada debe ser de tipo list
    """
    if type(lista) != list:
        return "E01"
    else:
        return verificar_todos_numéricos_aux(lista, len(lista), 0)

def verificar_todos_numéricos_aux(lista, largo, indice):
    """
    Función auxiliar para verificar elementos numéricos.
    """
    if indice == largo:
        return True
    elif type(lista[indice]) == int or type(lista[indice]) == float:
        return verificar_todos_numéricos_aux(lista, largo, indice + 1)
    else:
        return False

# Invertir una lista 
# invertir_lista_cola(lista)
def invertir_lista_cola(lista):
    """
    Función que invierte una lista.
    E: Una lista
    S: La lista invertida
    R: La entrada debe ser de tipo list
    """
    if type(lista) != list:
        return "E01"
    return invertir_lista_aux(lista, len(lista), 0, [])

def invertir_lista_aux(lista, largo, indice, resultado):
    """
    Función auxiliar que construye la lista invertida usando recursión con acumulador.
    """
    if indice == largo:
        return resultado
    else:
        return invertir_lista_aux(lista, largo, indice + 1, [lista[indice]] + resultado)


# Buscar un texto dentro de otro
# buscar_texto_cola(busca, texto)

def buscar_inicio(buscar, texto):
    """
    Función que verifica si un texto comienza con el subtexto 'buscar'.
    E: Dos cadenas de texto
    S: True si 'texto' comienza con 'buscar', False si no
    R: La entrada debe ser de tipo str
    """
    if type(texto) != str or type(buscar) != str:
        return "E01"
    elif len(buscar) > len(texto): 
        return False
    else:
        return buscar_inicio_aux(buscar, texto, len(buscar), 0, True)


def buscar_inicio_aux(buscar, texto, largo_b, indice, resultado):
    """
    Función auxiliar que compara carácter por carácter si el texto comienza con 'buscar'.
    E: Dos cadenas de texto y su longitud
    S: True si el texto comienza con el subtexto
    R: La entrada debe ser de tipo str
    """
    if largo_b == indice:
        return resultado
    elif texto[indice] == buscar[indice]:
        return buscar_inicio_aux(buscar, texto, largo_b, indice + 1, resultado)
    else:
        return False

# Función Principal para buscar un texto dentro de otro
def buscar_texto_cola(busca, texto):
    """
    Función que busca un subtexto dentro de un texto completo.
    E: Dos cadenas de texto
    S: True si 'buscar' está dentro de 'texto', False si no
    R: La entrada debe ser de tipo str
    """
    if type(texto) != str or type(busca) != str:
        return "E01"
    else:
        return buscar_texto_aux(busca, texto, len(texto), 0)


def buscar_texto_aux(buscar, texto, largo_t, indice):
    """
    Función auxiliar que recorre el texto e intenta encontrar el subtexto.
    E: Un texto y un subtexto
    S: True si encuentra el subtexto en el texto
    R: La entrada debe ser de tipo str
    """
    if largo_t == indice:
        return False
    elif buscar_inicio(buscar, texto[indice:]):
        return True
    else:
        return buscar_texto_aux(buscar, texto, largo_t, indice + 1)
    

# Dibujar un triángulo con asteriscos (en ambos sentidos)
# dibujar_triángulo_cola(número)
def dibujar_triángulo_cola(número):
    """
    Función principal para dibujar un triángulo con asteriscos.
    E: Un número entero
    S: Dibuja un triángulo de asteriscos
    R: El número debe ser entero positivo e impar
    """
    if type(número) != int:
        return "E01"
    elif número < 0:
        return "E02"
    elif número % 2 == 0:
        return "E03"
    else:
        return dibujar_triangulo_cola_aux(número, 0)

def dibujar_triangulo_cola_aux(num, espacio):
    """
    Función en cola para dibujar el triángulo de asteriscos.
    E: Un número entero (base del triángulo) y un espacio de indentación
    S: Dibuja el triángulo con recursión en cola
    R: El número debe ser entero positivo e impar
    """
    if num <= 0:
        return dibujar_triangulo_invertido_cola(1, espacio - 1)
    else:
        print(" " * espacio + "* " * num)
        return dibujar_triangulo_cola_aux(num - 1, espacio + 1)

def dibujar_triangulo_invertido_cola(num, espacio):
    """
    Función en cola para dibujar la parte invertida del triángulo de asteriscos.
    E: Un número entero (base del triángulo invertido) y un espacio de indentación
    S: Dibuja la parte invertida del triángulo
    R: El número debe ser entero positivo
    """
    if espacio < 0:
        return
    else:
        print(" " * espacio + "* " * num)
        return dibujar_triangulo_invertido_cola(num + 1, espacio - 1)


# Dibujar un rectángulo con asteriscos
# dibujar_rectángulo_cola(largo, ancho)
def dibujar_rectángulo_cola(largo, ancho):
    """
    Función principal para dibujar un rectángulo de asteriscos.
    E: Dos enteros, largo (ancho) y ancho del rectángulo
    S: Dibuja un rectángulo con asteriscos
    R: El largo y la ancho deben ser enteros positivos
    """
    if type(largo) != int or type(ancho) != int:
        return "E01"
    elif largo <= 0 or ancho <= 0:
        return "E02"
    
    elif largo == ancho:
        return "E03"
    else:
        return dibujar_rectángulo_cola_aux(largo, ancho, 0)

def dibujar_rectángulo_cola_aux(largo, ancho, indice):
    """
    Función en cola que dibuja un rectángulo de asteriscos.
    E: Largo y ancho del rectángulo, y el índice de iteración.
    S: Dibuja el rectángulo con recursión en cola.
    R: El largo y la ancho deben ser enteros positivos.
    """
    if indice == ancho:
        return " "
    else:
        print(" * " * largo)
        return dibujar_rectángulo_cola_aux(largo, ancho, indice + 1)

# Permutaciones de una lista [1,2] [4,5] -> [[1,4],[1,5],[2,4],[2,5]]
# permutaciones_cola(lista1, lista2)

def permutaciones_cola(lista1, lista2): 
    """ 
    Función que valida las entradas y genera las permutaciones
    entre dos listas.

    E: Dos listas, lista1 y lista2.
    S: Retorna una lista con las permutaciones de los elementos de lista1 y lista2, o un mensaje de error si no son listas.
    R: El tipo de lista1 y lista2 debe ser 'list'.
    """
    if type(lista1) != list or type(lista2) != list:
        return "E01"  # Error si los parámetros no son listas
    
    else:
        return permutacion_aux(lista1, lista2, len(lista1), len(lista2), 0, 0, [])

def permutacion_aux(lista1, lista2, largo1, largo2, indice1, indice2, resultado):
    """
    Función auxiliar
    """
    if largo1 == indice1:  
        return resultado

    elif largo2 != indice2:  
        return permutacion_aux(lista1, lista2, largo1, largo2, indice1, indice2 + 1, resultado + [[lista1[indice1], lista2[indice2]]])

    else: 
        return permutacion_aux(lista1, lista2, largo1, largo2, indice1 + 1, 0, resultado)
