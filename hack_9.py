"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(d):
    # Paso 1: Eliminar los dos últimos elementos del diccionario
    items = list(d.items())
    if len(items) > 2:
        items = items[:-2]
    
    # Paso 2: Convertir la primera letra de cada clave a mayúscula
    updated_dict = {key.capitalize(): value for key, value in items}
    
    # Paso 3 y 4: Formatear el resultado final
    result = {}
    for key, value in updated_dict.items():
        # Verificar si el valor comienza con la clave original (convertida a minúscula)
        original_key = key.lower()
        if value.startswith(original_key):
            # Formatear el nuevo valor
            new_value = key + value[len(original_key):]
            result[key] = new_value
    
    return result