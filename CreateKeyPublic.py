from Crypto import Random
from Crypto.PublicKey import RSA

randomGen=Random.new().read
rsa=RSA.generate(1024, randomGen)

keyPrivate=rsa.exportKey()
with open('KeyPrivate.txt', 'wb') as f:
    f.write(keyPrivate)

keyPublic=rsa.publickey().exportKey()
with open('KeyPublic.txt', 'wb') as f:
    f.write(keyPublic)

print('Se crearon correctamente las llaves!!!')

print(keyPrivate)
print(keyPublic)

