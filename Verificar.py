from pathlib import Path
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64

def verificar(msj, sign):
    with open('KeyPublic.txt') as f:
        key=f.read()
        rsakey=RSA.importKey(key)
        verifier=Signature_pkcs1_v1_5.new(rsakey)
        
        digest=SHA.new()
        digest.update(msj)

        print('Calcular Hash de documento recibido', digest.hexdigest())
        print('Desencriptamos la firma para sacar el Hash')

        is_verify=verifier.verify(digest, base64.b64decode(sign))

    if is_verify:
        print('Los Hash coinciden \nAutor Legitimo')
    else:
        print('Los Hash no son iguales \nFirma Ilegal')

if Path('DatosUser.txt').is_file() and Path('Sign.txt').is_file():
    with open('DatosUser.txt', 'r') as f1:
        msj=f1.read()
    
    with open('Sign.txt', 'r') as f2:
        sign=f2.read()

    if Path('KeyPublic.txt').is_file():
        msj=msj.encode()
        verificar(msj, sign)
    else:
        print('El archivo KeyPublic.txt no se ha creado \nEjecutar el archivo CreateKeyPublic.py para crearlo.')
else:
    print('El archivo DatosUser.txt y Sign.txt no se han creado \nEjecutar el archivo FirmaDigital.py para crearlos. \n')




