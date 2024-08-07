"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""



def fn_hack_8(s):
    result = []
    length = len(s)
    
    # Si la longitud de la lista es impar
    if length % 2 != 0:
        for i in range(length):
            result.append(f"{s[length - 1 - i]}-{length - i}")
    else:
        # Si la longitud es par, devolver solo los índices en formato de cadena
        for i in range(length):
            result.append(str(length - i))
    
    return result
