"""
Emite informações sobre as vozes
"""

def emitir_som(voz_aguda=True):
    """Emite um som de voz"""
    if voz_aguda:
        print("Voce ouviu num tom bem agudo. ")
    else:
        print("voce ouviu uma voz grave. ")