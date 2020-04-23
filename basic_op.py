"""
all global needed during the process 
    -> calc_input = string of all the operation required / 
    -> f_nb       = first number entered by the user
    -> operator   = operator used
    -> result     = reuslt of last operation
"""

myOperations=[]

def put_in_myOperations(value):
    myOperations.append(value)
    print(myOperations)#test console

def clear_myOperations():
    myOperations[:]=[]
    print(myOperations)#test console

def make_operation(inputOperator):
    """
    When user entered an operator the function input_operator catch the actual value as first value +  the input operator
    it take them in global
    calc_input += inputOperator is a string witch return numbers and operators
    If user use a second operator I wan the opration make it anyway. 
    ex: 2+2=4 but if user make 2+2+2, I want e display 4 after the 1st add and 2 add to 4, so = 6 and not 4.
    """
    
    myOperations.append(inputOperator)
    print(myOperations)#test console
    last_result = 0
    return last_result
    
def result():
    """
    1/last value is append to the list myOperations
    2/catch the 2 last values (first ans second) and the last operator in the array/list
    3/calculate the equation between first_nbr et second_nbr according to the operator
    4/return the result
    """
    result = 0
    
    #1
    last_key=(len(myOperations)-1)
    s_nb = int(myOperations[last_key])
    
    #2
    first_nbr_key = last_key-2
    f_nb = int(myOperations[first_nbr_key])
    
    
    operator_key = last_key-1
    operator=myOperations[operator_key]
    
    #3
    if operator == "+": 
        result = f_nb + s_nb
    elif operator== "-":
        result = f_nb - s_nb
    elif operator== "*":
        result = f_nb * s_nb
    elif operator== "/":
        result = f_nb / s_nb
    #4
    return result

    