"""
myOperations is a list wich memory all values and operators entered by the user before click on "="
"""

myOperations=[]

def put_in_myOperations(value):
    #this function fill myOperations list
    myOperations.append(value)

def clear_myOperations():
    #this function delete all values in myOperations list
    myOperations[:]=[]

def make_operation(inputOperator):    
    #this function add the operator in the array "myOperations
    myOperations.append(inputOperator)

def calc_all_myOperations():
    """
    This function browse the array myOperations to return the result
    of all the operations 2 by 2 from the first to the last, entered
    before click on "="
    When it make the fist operation with the 3 first values (2 values + 1 operator)
    it delete 2 value and replace the first one by the result
    While it's not empty it continue to make the other operations.
    It don't manage priorities between operators (% and * before + and -)
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
        elif operator== "% of ":
            print(myOperations)
            result = f_nb/100*s_nb
        
        round_result=round(result,5)
        del myOperations[:2]
        myOperations[0]=round_result
    
    clear_myOperations()  
    return round_result
