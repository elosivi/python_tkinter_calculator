from tkinter import *
import math

import basic_op


 
# to generate a window with tkinter

window = Tk()
window.title("Elo's calculator")

#array/list wich keep in memory all values and operators entered by user.


nb_input=""
calc_input=""
# is_first= True

#fonctions display
def input_key(value):
    """
    function input_key catch the input value as a concatenate simples numbers and return the desired complete nbr
    current catch the actual value in e
    """
    
    global calc_input
    calc_input += value
    
    calc_input_text.set(calc_input)#print on a secondary display
   
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(value))

def get_e_value():
    """
    catch the actual value displayed in e 
    It return it to be used in calculator's functions
    """
    actual_nbr = e.get()#catch the 1st nbr
    return actual_nbr

def clear_e_display():
    e.delete(0,END)#clear the first display
    
def input_operator(operator,actualValue):
    """
    catch the value of operator entered + actual value in e
      1/ print operator in the second display: calc_input
      2/ send the actual value + operator in basic_op.make_operation 
    print it in the second display
    delete the e display (usual attitude of a calculator)
    """
    
    # global is_first
    global calc_input
    calc_input += operator
    calc_input_text.set(calc_input)
    
    e.delete(0,END)#delete the e
    basic_op.make_operation(operator,actualValue)
    
    # if is_first==True:
    #     is_first=False
    # else:
    #     new_value= basic_op.result(actualValue)
    #     e.insert(0, new_value)
   

def input_eqal(actualValue):
    result = basic_op.result(actualValue)
    e.insert(0,result)
    e.delete(0,END)
    global calc_input #to print on a secondary display, to keep?
    calc_input += "="+str(result)#to print on a secondary display, to keep?
    result_text.set(result)#to print on a secondary display, to keep?
    e.insert(0, result)
    

def input_clear():
    """
    to clear all values displayed in the 2 display areas.
    """
    global calc_input
    calc_input = ""
    calc_input_text.set(calc_input) #clear the secondary display
    result_text.set(calc_input) #clear the secondary display
    e.delete(0,END)#clear the first display
    # global is_first
    # is_first=True
    myOperations=[]

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

button_aqual =Button(window, text=" = ", command=lambda: input_eqal(get_e_value())).grid(row=2, column=3)                                         
button_clear =Button(window, text=" clear ", command=lambda: input_clear()).grid(row=6, column=1,columnspan=2 )

calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row=1, column=0, columnspan=3)

result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, column=0, columnspan=3)

#end of graphic interface



window.mainloop()