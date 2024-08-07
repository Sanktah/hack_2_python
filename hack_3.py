"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
    replacements = {'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v'}
    result = []

    # Aplicar reemplazos y mantener el caso de la letra original
    for char in s:
        lower_char = char.lower()
        replaced_char = replacements.get(lower_char, char)
        # Mantener la mayúscula si el carácter original era mayúscula
        if char.isupper():
            replaced_char = replaced_char.upper()
        result.append(replaced_char)

    # Convertir el primer carácter a mayúscula
    if result:
        result[0] = result[0].upper()

    # Convertir la última letra a mayúscula si es una letra y ajustar X y v
    if len(result) > 1 and result[-1].isalpha():
        if result[-1].lower() == 'x':
            result[-1] = 'X'
        elif result[-1].lower() == 'v':
            result[-1] = 'v'
        else:
            result[-1] = result[-1].upper()

    return ''.join(result)
