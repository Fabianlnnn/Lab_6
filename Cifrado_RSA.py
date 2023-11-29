import random

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def verifica_primo(n):
    c = 0
    x = 2
    if n >= 2:
        while x <= n/2:
            if n % x == 0:
                c = c + 1
                x = x + 1
            else:
                x = x + 1
        if c == 0:
            return True
        else:
            return False
    else:
        return False

def genera_primos(n):
    lp = []
    x = 2
    while n != 0:
        if verifica_primo(x):
            lp.append(x)
            x = x + 1
            n = n - 1
        else:
            x = x + 1
    return lp

def generar_p_y_q():
    lista_primos = genera_primos(100)
    p = int(random.choice(lista_primos))
    q = int(random.choice(lista_primos))
    return p, q

def calcular_phi(p, q):
    return (p - 1) * (q - 1)

def calcular_e(phi):
    for candidato in range(2, phi):
        if mcd(candidato, phi) == 1:
            return candidato
    return None

def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calcular_d(e, phi):
    k = 1
    while True:
        d = (1 + k * phi) / e
        if d.is_integer():
            return int(d)
        k += 1

def cifrar_mensaje(mensaje, clave_publica):
    mensaje = mensaje.upper()
    palabras = mensaje.split(" ")
    mensaje_cifrado = ""
    for palabra in palabras:
        palabra_cifrada = cifrar_palabra(palabra, clave_publica)
        mensaje_cifrado += str(palabra_cifrada) + " "
    return mensaje_cifrado.strip()

def cifrar_palabra(palabra, clave_publica):
    cifrado = ""
    n, e = clave_publica
    for letra in palabra:
        posicion = buscar_posicion(letra)
        if posicion != -1: 
            cifra = pow(posicion, e, n)
            cifrado += str(cifra) + " "
    return cifrado.strip()

def buscar_posicion(letra):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    try:
        return alfabeto.index(letra)
    except ValueError:
        print(f"La letra '{letra}' no está en el alfabeto.")
        return -1

def descifrar_mensaje(mensaje, clave_privada):
    descifrado = ""
    palabras = mensaje.split()
    for palabra in palabras:
        letra_descifrada = descifrar_numero(palabra, clave_privada)
        descifrado += letra_descifrada
    return descifrado

def descifrar_numero(num, clave_privada):
    n, d = clave_privada
    try:
        num = int(num)
        letra = buscar_letra(pow(num, d, n))
        return letra
    except ValueError:
        print(f"No se pudo convertir '{num}' a un número entero.")
        return ""

def buscar_letra(posicion):
    alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    if 0 <= posicion < len(alfabeto):
        return alfabeto[posicion]
    else:
        return ""

p, q = generar_p_y_q()
n = p * q
phi = calcular_phi(p, q)
e = calcular_e(phi)
d = calcular_d(e, phi)

clave_publica = (n, e)
clave_privada = (n, d)

archivo = open("mensajeentrada.txt", "r")
mensaje_entrada = str(archivo.readline().upper())
archivo.close()

mensaje_cifrado = cifrar_mensaje(mensaje_entrada, clave_publica)

mensaje_cifrado = str(mensaje_cifrado.strip())
mensaje_descifrado = descifrar_mensaje(mensaje_cifrado, clave_privada)

