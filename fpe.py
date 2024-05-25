import pyffx
import sys
import string

# identificador único del paciente pasado por parametro
patient_identifier = sys.argv[1]
key = b'HospitalSantJoanDeDeu' # clave convertida en bytes

# El identificador puede contener letras y números
alphabet=string.ascii_letters+string.digits

# Creamos en objeto para encriptar usando el algoritmo FPE a partir de la clave definida
encryptor = pyffx.String(key, alphabet=alphabet,length=len(str(patient_identifier)))

# Obtemos el identificador anonimizado del paciente
identifier_anonymized = encryptor.encrypt(patient_identifier)
# Descencriptamos el identificador y obtenemos el original 
identifier_decrypted = encryptor.decrypt(identifier_anonymized)

print(f'Identificador único original: {patient_identifier} \nIdentificador anonimizado: {identifier_anonymized}\nIdentificador original desencriptado: {identifier_decrypted}')
