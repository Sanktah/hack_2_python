"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""



def fn_hack_10(lst):
    num_map = {"a": "1", "b": "2", "c": "3", "d": "4", "e": "5", "f": "6"}
    _str = [{num_map[k]: num_map[v]} for d in lst for k, v in d.items()]
    
    result = _str
    return result

# Ejemplo de uso:
print(fn_hack_10([{"a": "b"}, {"c": "d"}, {"e": "f"}]))  # Output: [{"1": "2"}, {"3": "4"}, {"5": "6"}]
