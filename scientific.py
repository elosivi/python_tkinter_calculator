import math

pourcent_array= []

def scientific_op(sci_value, e_value):
    value = float(e_value)
    if sci_value == "tan":
        result = math.tan(value)
    if sci_value == "cos":
        result = math.cos(value)
    if sci_value == "sin":
        result = math.sin(value)
    if sci_value == "racine":
        result = math.sqrt(value)
    
    print(result)#test console    
    return result

    