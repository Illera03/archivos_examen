def ordenar(letras):
    return sorted(letras.items(), key=lambda x: x[1], reverse=True)

def descifrar():
    mensaje = """
    RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE
    AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
    AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ
    TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX
    DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936,
    PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN
    TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE,
    HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK
    HKCZJOI OKEJSZCNHE
    """
    
    # Inicializar el diccionario para contar frecuencias de letras
    letras = {chr(i): 0 for i in range(65, 91)}  # ASCII de A a Z
    
    # Frecuencias de cada letra en el mensaje
    for char in mensaje:
        if char in letras:
            letras[char] += 1

    # Ordenar por frecuencia
    letras_ordenadas = ordenar(letras)
    
    # Mostrar frecuencias
    print("Frecuencias de letras en el mensaje:")
    for letra, frecuencia in letras_ordenadas:
        print(f"{letra}: {frecuencia}")
    
    # Diccionario de letras a reemplazar
    reemplazos = {
        "X": "e",
        "E": "a",
        "K": "r",
        "I": "o",
        "C": "i",
        "J": "n",
        "T": "l",
        "A": "d",
        "R": "c",
        "Z": "u",
        "H": "tContar las fp",
        "O": "f",
        "Q": "b",
        "S": "q",
        "G": "j",
        "V": "y",
        "U": "g",
        "v": "v",
        "M": "h",
        "L": "z",
        "F": "x",
    }
    
    # Reemplazar las letras en el mensaje
    mensaje_reemplazado = mensaje
    for letra_cifrada, letra_descifrada in reemplazos.items():
        mensaje_reemplazado = mensaje_reemplazado.replace(letra_cifrada, letra_descifrada)
    
    # Imprimir el mensaje descifrado
    print("\nMensaje descifrado:")
    print(mensaje_reemplazado)

descifrar()



