TOKENS_VALIDOS = {
    "clave_unica_servicio1": "Servicio1",
    "clave_unica_servicio2": "Servicio2",
    "clave_unica_servicio3": "Servicio3"
}

def verificar_token(token):
    return token in TOKENS_VALIDOS
