import math

pourcent_array= []

def scientific_op(sci_value, e_value):
    #This function manage the scientific operations and return the value to calculatrice.py
    value = float(e_value)
    if sci_value == "tan":
        result = math.tan(value)
    if sci_value == "cos":
        result = math.cos(value)
    if sci_value == "sin":
        result = math.sin(value)
    if sci_value == "racine":
        result = math.sqrt(value)
    if sci_value =="fraction":
        result = (1/value)
        print(result)
    
    print(result)#test console    
    return result

    