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
    
    if len(myOperations)>3:
        last_result=result()
        return last_result
    else:
        return None
    

def calc_all_myOperations():
    """
    this function browse the array myOperations to return the result
    of all the operations 2 by 2 from the first to the last, entered
    before click on "="
    when it make the fist operation with the 3 first values (2 values + 1 operator)
    it delete 2 value and replace the first one by the result
    while it's not empty it continue to make the other operations.
    Carefull it don't manage priorities between operators (% and * before + and -)
    """
    while len(myOperations)>1:
        f_nb = float(myOperations[0])
        operator = myOperations[1]
        s_nb = float(myOperations[2])
        
        if operator == "+": 
            result = f_nb + s_nb
        elif operator== "-":
            result = f_nb - s_nb
        elif operator== "*":
            result = f_nb * s_nb
        elif operator== "/":
            result = f_nb / s_nb
        
        print(result)
        del myOperations[:2]
        myOperations[0]=result
        print("new")
        print(myOperations)
    
    clear_myOperations()  
    return result
        