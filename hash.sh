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

    # Se comprueba si el hash coincide con el que tenemos
    if [ "$hash_actual" == "$HASH_OBJETIVO" ]; then
        echo "¡Archivo encontrado! El archivo con el hash es: $archivo"
        # break si no hay mas de uno
    fi
done
