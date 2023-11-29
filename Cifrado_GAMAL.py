import random
from math import pow

# Función para calcular el máximo común divisor
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b
    else:
        return gcd(b, a % b)

# Función para generar una clave con números grandes
def generar_clave(q):
    clave = random.randint(pow(10, 20), q)
    while gcd(q, clave) != 1:
        clave = random.randint(pow(10, 20), q)
    return clave

# Función para realizar la potenciación modular
def potencia_modular(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c
        y = (y * y) % c
        b = int(b / 2)
    return x % c

# Función para cifrar un mensaje
def cifrado(mensaje, q, h, g):
    cifrado_texto = []
    clave_privada = generar_clave(q)
    s = potencia_modular(h, clave_privada, q)
    p = potencia_modular(g, clave_privada, q)
    for letra in mensaje:
        cifrado_texto.append(s * ord(letra))
    return cifrado_texto, p

# Función para descifrar un mensaje
def descifrado(cifrado_texto, p, clave_privada, q):
    texto_descifrado = []
    h = potencia_modular(p, clave_privada, q)
    for valor in cifrado_texto:
        texto_descifrado.append(chr(int(valor / h)))
    return texto_descifrado

