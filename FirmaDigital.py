import base64
from inspect import signature
from pathlib import Path
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto.PublicKey import RSA

def firmar(msj):
    with open('KeyPrivate.txt') as f:
        key=f.read()
        rsaKey=RSA.importKey(key)
        signer=Signature_pkcs1_v1_5.new(rsaKey)

        digest=SHA.new()
        digest.update(msj)

        print('Contenido del documento', msj)
        print('HASH generado', digest.hexdigest())

        sign=signer.sign(digest)
        signature=base64.b64encode(sign)
    
    with open('Sign.txt', 'wb') as fp1:
        fp1.write(signature)
        fp1.close()
    
    print('Firma creada', signature)
    print('Firma guardada en Sign.txt')

    return signature

if Path('KeyPrivate.txt').is_file():
    datosUser=input('Agregar el texto que desea encriptar: ')
    with open('DatosUser.txt', 'w') as fu:
        fu.write(datosUser)

    with open('DatosUser.txt', 'r') as f1:
        msj=f1.read()

    msj=msj.encode()
    signature=firmar(msj)
else:
    print('El archivo KeyPrivate.txt no se ha creado \nEjecutar el archivo CreateKeyPublic.py para crearlo. ')
