"""
This file manage the view, and display user's "click"
See import my modules to consult files wich manage mathematicals operations
"""

from tkinter import *
import math

#import my modules
import basic_opcd pack(fmt, v1, v2, ...)
import scientific
 
# to generate a window with tkinter
window = Tk()
window.configure()
window.title("Elo's calculator")

calc_input=""


def set_message(type_mess=""):
    """
    This function manage all messages needed to send to the user for a better utilisation of the app
    """
    if type_mess=="":
        mess=""
    if type_mess == "negative_error" :
        mess = "\n please enter value before \n - \n"
    if type_mess == "how_to_use_pourcent":
        mess="\n pourcent using: \n first enter the %value + % + the basis_value \n like: 50% /of 32 \n - \n"
    if type_mess == "rounded_result":
        mess="\n Please note: \n if necessary, result is rounded 5 numbers after comma: \n 0.12345678 -> 0.12346 \n - \n"
    if type_mess == "fraction_method":
        mess="\n fraction method: enter first your value, then 1/x button \n "
    message_text.set(mess)
    
    
def input_key(input_value):
    """
    This function concatene the value
    1/set the message to null if there is one 
    2/this function catch the input value and concatenate simples numbers to display the desired complete nbr in "e"
    """
    set_message()
    
    if input_value == "pi":
        input_value = math.pi
            
    value = input_value       
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(value))
    actual_value=e.get()
    

def input_neg_value(e_value):
    """
    This function manage the button "+/-"
    1/ if there is not value in "e", send a message about how to use it
    2/ if there is a value entered yet: pass the actual value to the negative and display it in "e"
    """
    if e_value == "":
        set_message("negative_error")
    
    else:
        current_value= e.get()
        neg_value = float(current_value)*-1
        e.delete(0,END)
        e.insert(0,str(neg_value))
        actual_value=e.get()
        
        
def get_e_value():
    """
    This function catch the actual value displayed in "e" 
    It return it to be used in calculator's functions
    """
    actual_nbr = e.get()
    return actual_nbr


def input_operator(operator,actualValue):
    """
    This function catch the value of operator entered + actual value in "e"
      1/ set the message to null if there is one 
      2/ send a message if pourcent is using to help the user
      3/ add actual value in the array myOperations calling the function : put_in_myOperations(actualValue) in basic_op.py
      4/ print operator in the display area name "calc_input_text"
      5/ delete the e display (usual attitude of a calculator)
      6/ send the actual value to the function make_operation in basic_op.py 
    """
    set_message()
    
    global calc_input
    if operator=="pourcent":
        set_message("how_to_use_pourcent")
       
    basic_op.put_in_myOperations(actualValue)
    
    calc_input += e.get()
    if operator=="pourcent":
        operator = "% of "
    calc_input += operator
    calc_input_text.set(calc_input)
    
    e.delete(0,END)
    
    basic_op.make_operation(operator)
    
    
def input_eqal(actualValue):
    """
    This function return the result of operation
    1/set the message to inform the user about the aqal function round the result 
    2/catch the value and add it in the array "myOperations"
    3/return the result of operation in a variable names "result" and display it in the areas named : "e" and "result_text"
    """
    set_message("rounded_result")
    
    global calc_input
    calc_input += e.get()
    calc_input_text.set(calc_input)
    
    basic_op.put_in_myOperations(actualValue)
        
    result=basic_op.calc_all_myOperations()
    result_text.set(result)
    
    calc_result=str(result)
    calc_input += ("="+ calc_result + "/ " )
    calc_input_text.set(calc_input)
    e.insert(0,result)
    e.delete(0,END)
    e.insert(0, result)
    

def input_clear():
    """
    This function clear all operations and data entry 
    1/ set the message to null if there is one 
    2/ clear all the areas wich return values, results and operations.
    3/ use function clear_myOperations in basic_op.py to empty the array 'myOperations'
    """
    set_message()
    
    global calc_input
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(calc_input) 
    e.delete(0,END)
    basic_op.clear_myOperations()


def input_sci_op(input_sci_value, actual_value):
    """
    This function manage scientific operations as tan, cos, sin, racine, fraction
    1/ set the message to null if there is one 
    2/ set a message to help user make a fraction
    3/ send the actual value in "e" to the function scientific_op() in scientific.py and return result
    4/ manage the diplay_view, changing str like "racine" by symbol √, or "franction" by 1/ before display the complete operation and the result in concerning areas
    """
    set_message()
    
    if input_sci_value == "fraction":
        set_message("fraction_method")
        
    value = actual_value
    result = scientific.scientific_op(input_sci_value, value)
    
    if input_sci_value == "racine":
        input_sci_value = "√"
    elif input_sci_value == "fraction":
        input_sci_value = "1/"
    calc_input = input_sci_value + " (" +value + ") = "
    calc_input_text.set(calc_input)
    result_text.set(result) 



"""
Here under script to create the graphic interface:
all common buttons in a calculator
areas to return operations andresults
front-end : modif view with width,height,cbackground,font,etc... 

"""
#row 0 : to close
button_close =Button(window, text="Close", width=10, height=2, bg="#86ADB1", command=window.quit).grid(row=0, column=5)

#row 1 : usual calculator display, here called "e"
e = Entry(window,width =50,justify=RIGHT, borderwidth=2, font=25)
e.grid(row=1,column=0,columnspan=6, padx=20, pady=20)

#row 2 & 3 : special display + row 4 :space
calc_input_text = StringVar()
Label(window, textvariable=calc_input_text,width=70,bg="#ADADAD", font=20, justify=RIGHT).grid(row=2, column=0, columnspan=6)


result_text = StringVar()
Label(window, textvariable=result_text, width=70, height=3, font=30 , bg="#656666", fg="#DBFD00", justify=RIGHT).grid(row=3, column=0, columnspan=6)

#rows 5 -> 9: buttons
button_sin =Button(window, text="sin", width=5, height=3, bg="#2D4044",fg="white", font="bold", command=lambda: input_sci_op("sin", get_e_value())).grid(row=5, column=0, pady=1, padx=1)
button_fraction =Button(window, text="1/x", width=5, height=3, bg="#2D4044",fg="white", font="bold",command=lambda: input_operator("fraction", get_e_value())).grid(row=5, column=1, pady=1, padx=1 )
button_pourcent =Button(window, text="%", width=5, height=3, bg="#2D4044",fg="white", font="bold",command=lambda: input_operator("pourcent", get_e_value())).grid(row=5, column=2, pady=1, padx=1)
button_negative =Button(window, text="+/-", width=5, height=3, bg="#95BFC3", font="bold",command=lambda: input_neg_value(get_e_value())).grid(row=5, column=3, pady=1, padx=1)
button_clear =Button(window, text="A/C", width=22, height=3, bg="#232424", fg="#DBFD00", font="bold",command=lambda: input_clear()).grid(row=5, column=4,columnspan=2, pady=1, padx=1 )

button_tan =Button(window, text="tan", width=5, height=3, bg="#2D4044",fg="white", font="bold",command=lambda: input_sci_op("tan", get_e_value())).grid(row=6, column=0)
button_7 =Button(window, text=" 7 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("7")).grid(row=6, column=1)
button_8 =Button(window, text=" 8 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("8")).grid(row=6, column=2)
button_9 =Button(window, text=" 9 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("9")).grid(row=6, column=3)
button_divide =Button(window, text=" / ", width=5, height=3,  bg="#232424", fg="#DBFD00", font="bold",command=lambda: input_operator("/", get_e_value())).grid(row=6, column=4)
button_eqal =Button(window, text=" = ", width=11, height=15, bg="#DBFD00", font=('Helvetica',12,'bold'), command=lambda: input_eqal(get_e_value())).grid(row=6, column=5,rowspan=4 )    

button_cos =Button(window, text="cos", width=5, height=3, bg="#2D4044",fg="white", font="bold",command=lambda: input_sci_op("cos", get_e_value())).grid(row=7, column=0)
button_4 =Button(window, text=" 4 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("4")).grid(row=7, column=1)
button_5 =Button(window, text=" 5 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("5")).grid(row=7, column=2)
button_6 =Button(window, text=" 6 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("6")).grid(row=7, column=3)
button_multiply =Button(window, text=" x ", width=5, height=3,  bg="#232424", fg="#DBFD00", font="bold",command=lambda: input_operator("*", get_e_value())).grid(row=7, column=4)

button_pi =Button(window, text=" π ", width=5, height=3, bg="#2D4044",fg="white", font="bold",command=lambda: input_key("pi")).grid(row=8, column=0)
button_1 =Button(window, text=" 1 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("1")).grid(row=8, column=1)
button_2 =Button(window, text=" 2 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("2")).grid(row=8, column=2)
button_3 =Button(window, text=" 3 ", width=5, height=3, bg="#527F87", font="bold",command=lambda: input_key("3")).grid(row=8, column=3)
button_substract =Button(window, text=" - ", width=5, height=3,  bg="#232424", fg="#DBFD00", font="bold",command=lambda: input_operator("-", get_e_value())).grid(row=8, column=4)

button_racine =Button(window, text=" √ ", width=5, height=3, bg="#2D4044",fg="white", font="bold",command=lambda: input_sci_op("racine", get_e_value())).grid(row=9, column=0)
button_0 =Button(window, text=" 0 ", width=15, height=3, bg="#527F87", font="bold",command=lambda: input_key("0")).grid(row=9, column=1, columnspan=2)
button_virg =Button(window, text=" . ", width=5, height=3,bg="#95BFC3", font="bold",command=lambda: input_key(".")).grid(row=9, column=3)
button_add =Button(window, text=" + ", width=5, height=3,  bg="#232424", fg="#DBFD00", font="bold",command=lambda: input_operator("+", get_e_value())).grid(row=9, column=4)

message_text = StringVar()
Label(window, textvariable=message_text, font=('Helvetica',12,'bold'),fg="#527F87", justify=CENTER).grid(row=10, column=0, columnspan=6)


                                     




#end of graphic interface

window.mainloop()