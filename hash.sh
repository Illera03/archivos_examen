#!/bin/bash

# Directorio donde están las imágenes
DIRECTORIO="imagen"
# El hash MD5 que estamos buscando
HASH_OBJETIVO="e5ed313192776744b9b93b1320b5e268"

# Recorremos cada archivo de imagen en el directorio
for archivo in "$DIRECTORIO"/*; do
    # Calculamos el hash MD5 del archivo
    # Este comando(md5sum) devuelve una salida que tiene dos partes: el hash MD5 seguido del nombre del archivo.
    # Con el comando awk '{print $1}' seleccionamos solo el hash MD5 (y no el nombre del archivo)
    hash_actual=$(md5sum "$archivo" | awk '{print $1}')

    # Comprobamos si el hash coincide con el que buscamos
    if [ "$hash_actual" == "$HASH_OBJETIVO" ]; then
        echo "¡Archivo encontrado! El archivo con el hash es: $archivo"
        # Si sabemos que solo hay un archivo con el hash, podemos salir del bucle con break
    fi
done

### PREGUNTAS:
## El mensaje se puede extraer abriendo la aplicación Stegosuite y seleccionando la foto que indica el script y pulsando Extract
# Este dice: "Al Fascismo no se le discute, se le destruye." Buenaventura Durrutie
#---------------------------------------------------------------------------------------------------------------------------------------

## Si quieres escribir un mensaje secreto en una imagen, y garantizar al destinatario que nadie lo ha modificado, ¿Qué pasos seguirías?
# Ocultar el mensaje usando esteganografía.
# Generar un hash criptográfico (SHA-256) de la imagen resultante.
# Enviar tanto la imagen como el hash al destinatario.
# El destinatario verifica la integridad de la imagen calculando su propio hash y comparándolo con el hash recibido.

#---------------------------------------------------------------------------------------------------------------------------------------

## ¿Sería posible incorporar en el contenido de un fichero su propio resumen criptográfico? Esto es, ¿Podría
## ponerse en el texto de este enunciado el resumen criptográfico que le corresponda al propio enunciado para que pudiérais comprobar su autenticidad?
# No puedes incluir el resumen criptográfico de un archivo dentro del propio archivo porque cambiaría su contenido y por tanto el propio resumen criptográfico.

#---------------------------------------------------------------------------------------------------------------------------------------
