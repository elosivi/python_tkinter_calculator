from tkinter import *
import math

import basic_op


 
# to generate a window with tkinter

window = Tk()
window.title("Elo's calculator")

calc_input=""

#fonctions display
def input_key(value):
    """
    function input_key catch the input value and concatenate simples numbers to
    display the desired complete nbr in 2 aeras.
    """
    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)#print on a secondary display
    
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(value))
    actual_value=e.get()

  

def get_e_value():
    """
    catch the actual value displayed in e 
    It return it to be used in calculator's functions
    """
    actual_nbr = e.get()#catch the 1st nbr
    return actual_nbr

    
def input_operator(operator,actualValue):
    """
    catch the value of operator entered + actual value in e
      1/ add actaul value in the array myOperations calling the function : put_in_myOperations(actualValue) in basic_op.py
      2/ print operator in the second display: calc_input
      3/delete the e display (usual attitude of a calculator)
      4/ send the actual value to the function make_operation in basic_op.py and return the result in cas of user make this = 2+1+, to display 3 as he enter "="
    """
    #1
    basic_op.put_in_myOperations(actualValue)
    #2
    global calc_input
    calc_input += operator
    calc_input_text.set(calc_input)
    #3
    e.delete(0,END)#delete the e
    #4
    result = basic_op.make_operation(operator)
    

def input_eqal(actualValue):
    """
    return the result of operation
    1/catch the value and add it in the array "myOperations"
    2/return the result of operation in a variable names "result" and display it in the 2 areas : "e" and "result_text"
    """
    basic_op.put_in_myOperations(actualValue)
    
    result = basic_op.result()
    e.insert(0,result)
    e.delete(0,END)
    global calc_input #to print on a secondary display, to keep?
    calc_input += "="+str(result)#to print on a secondary display, to keep?
    result_text.set(result)#to print on a secondary display, to keep?
    e.insert(0, result)
    

def input_clear():
    """
    to clear all values displayed in the 2 display areas.
    use function clear_myOperations in basic_op.py to empty the array 'myOperations'
    """
    global calc_input
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(calc_input) 
    e.delete(0,END)
    
    basic_op.clear_myOperations()


# create graphic interface:
e = Entry(window, width=20, borderwidth=2)
e.grid(row=0,column=0,columnspan=3, padx=10, pady=10)

button_close =Button(window, text="Fermer", command=window.quit).grid(row=0, column=3)
button_0 =Button(window, text=" 0 ", command=lambda: input_key("0")).grid(row=6, column=0)
button_1 =Button(window, text=" 1 ", command=lambda: input_key("1")).grid(row=5, column=0)
button_2 =Button(window, text=" 2 ", command=lambda: input_key("2")).grid(row=5, column=1)
button_3 =Button(window, text=" 3 ", command=lambda: input_key("3")).grid(row=5, column=2)
button_4 =Button(window, text=" 4 ", command=lambda: input_key("4")).grid(row=4, column=0)
button_5 =Button(window, text=" 5 ", command=lambda: input_key("5")).grid(row=4, column=1)
button_6 =Button(window, text=" 6 ", command=lambda: input_key("6")).grid(row=4, column=2)
button_7 =Button(window, text=" 7 ", command=lambda: input_key("7")).grid(row=3, column=0)
button_8 =Button(window, text=" 8 ", command=lambda: input_key("8")).grid(row=3, column=1)
button_9 =Button(window, text=" 9 ", command=lambda: input_key("9")).grid(row=3, column=2)
button_add =Button(window, text=" + ", command=lambda: input_operator("+", get_e_value())).grid(row=3, column=3)
button_substract =Button(window, text=" - ", command=lambda: input_operator("-", get_e_value())).grid(row=4, column=3)
button_multiply =Button(window, text=" x ", command=lambda: input_operator("*", get_e_value())).grid(row=5, column=3)
button_divide =Button(window, text=" / ", command=lambda: input_operator("/", get_e_value())).grid(row=6, column=3)

button_eqal =Button(window, text=" = ", command=lambda: input_eqal(get_e_value())).grid(row=2, column=3)                                         
button_clear =Button(window, text=" clear ", command=lambda: input_clear()).grid(row=6, column=1,columnspan=2 )

calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row=1, column=0, columnspan=3)

result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, column=0, columnspan=3)

#end of graphic interface

window.mainloop()