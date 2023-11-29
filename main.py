from flask import Flask, render_template
import Cifrado_RSA as rsa
import Cifrado_GAMAL as gamal
import random

app = Flask(__name__)

#### RSA
p, q = rsa.generar_p_y_q()
n = p * q
ø = (p - 1) * (q - 1)
e = rsa.calcular_e(ø)
d = rsa.calcular_d(e, ø)

clave_publica = [n, e]
clave_privada = [n, d]

archivo_rsa = open("mensajeentrada.txt", "r")
mensaje_entrada_rsa = str(archivo_rsa.readline().upper())
archivo_rsa.close()

mensaje_rsa = mensaje_entrada_rsa
mensaje_cifrado_rsa = rsa.cifrar_mensaje(mensaje_rsa, clave_publica)
mensaje_cifrado_rsa = str(mensaje_cifrado_rsa.strip())
mensaje_descifrado_rsa = rsa.descifrar_mensaje(mensaje_cifrado_rsa, clave_privada)

#### GAMAL
q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
clave_gamal = gamal.generar_clave(q)
h = gamal.potencia_modular(g, clave_gamal, q)

archivo_gamal = open("mensajeentrada.txt", "r")
mensaje_entrada_gamal = str(archivo_gamal.readline().upper())
archivo_gamal.close()

mensaje_gamal = mensaje_entrada_gamal
mensaje_cifrado_gamal, p = gamal.cifrado(mensaje_gamal, q, h, g)
mensaje_descifrado_gamal = gamal.descifrado(mensaje_cifrado_gamal, p, clave_gamal, q)
mensaje_descifrado_gamal = ''.join(mensaje_descifrado_gamal)

@app.route('/', methods=["GET", "POST"])
def principal():
    clave_publica = [n, e]
    clave_privada = [n, d]

    file_rsa = open("mensaje_recibido_rsa.txt", "w+")
    file_rsa.write(str(mensaje_descifrado_rsa))
    file_rsa.close()

    file_gamal = open("mensaje_recibido_gamal.txt", "w+")
    file_gamal.write(str(mensaje_descifrado_gamal))
    file_gamal.close()

    return render_template('index.html',
                           clave_publica=clave_publica,
                           clave_privada=clave_privada,
                           mensaje_encriptado_rsa=str(rsa.cifrar_mensaje(mensaje_rsa, clave_publica)),
                           mensaje_recibido_rsa=str(mensaje_descifrado_rsa),
                           mensaje_encriptado_gamal=mensaje_cifrado_gamal,
                           mensaje_recibido_gamal=str(mensaje_descifrado_gamal))

with open("mensaje_cifrado_rsa.txt", "w") as file_rsa:
    file_rsa.write(str(mensaje_cifrado_rsa))

with open("mensaje_cifrado_gamal.txt", "w") as file_gamal:
    file_gamal.write(str(mensaje_cifrado_gamal))

if __name__ == '__main__':
    app.run(debug=True)
