"""
all global needed during the process 
    -> calc_input = string of all the operation required / 
    -> f_nb       = first number entered by the user
    -> operator   = operator used
    -> result     = reuslt of last operation
"""
nb_input=""
calc_input=""
calc_input_text=""
f_nb=""
operator=""
result=""
result_text=""
myOperations=[]

# def input_key_concat(value):
#     """
#     concat values entered by user to make complete number. ex : 1,2,3 -> 123
#     send it to calculatrice.input_key to display it
#     """
#     global nb_input
#     nb_input += value
#     return nb_input

def make_operation(inputOperator, actual_nbr):
    """
    When user entered an operator the function input_operator catch the actual value as first value +  the input operator
    it take them in global
    calc_input += inputOperator is a string witch return numbers and operators
    If user use a second operator I wan the opration make it anyway. 
    ex: 2+2=4 but if user make 2+2+2, I want e display 4 after the 1st add and 2 add to 4, so = 6 and not 4.
    """
    
    global f_nb
    f_nb = int(actual_nbr)
    global operator 
    operator = inputOperator
    
    myOperations.append(actual_nbr)
    myOperations.append(inputOperator)
    print(myOperations)#test console
    
    
def result(actualValue):
    """
    catch the second number entered by user (second_nbr)
    catch the operator
    calculate the equation between first_nbr et second_nbr according to the choosen operator
    """
    second_nbr=actualValue
    result = 0
    global operator
    if operator == "+": #autres test : avec switch n existe pas et en utilisant un dictionnaire ne retourne que des str
        result = f_nb + int(second_nbr)
    elif operator== "-":
        result = f_nb - int(second_nbr)
    elif operator== "*":
        result = f_nb * int(second_nbr)
    elif operator== "/":
        result = f_nb / int(second_nbr)
    return result

    