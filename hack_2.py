"""
generic script

text: "fooziman" output => "fzmn" 
text: "barziman" output => "brzmn" 
text: "qux" output => "qx" 
"""


def fn_hack_2(s):

    vowels = ["a", "e", "i", "o", "u"]
    _str = []
    
    for char in s:
        if char not in vowels:
            _str.append(char)
    
    result = "".join(_str)
    return result
