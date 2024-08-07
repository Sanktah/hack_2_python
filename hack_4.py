"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""

def fn_hack_4(s):
    # Si la longitud de la cadena es mayor a 2, eliminar la primera y última letra
    if len(s) > 3:
        result = s[1:-1]
    else:
        # Devolver la cadena original si la longitud es 2 o menor
        result = s
    
    return result