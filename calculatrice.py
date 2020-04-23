from tkinter import *
import math

#import my modules
import basic_op
import scientific
 
# to generate a window with tkinter
window = Tk()
window.title("Elo's calculator")

calc_input=""

def set_message(type_mess=""):
    if type_mess=="":
        mess=""
    if type_mess == "negative_error" :
        mess = "\n please enter value before \n - \n"
    if type_mess == "how_to_use_pourcent":
        mess="\n pourcent using: \n first enter the %value + % + the basis_value \n like: 50% /of 32 \n - \n"
    if type_mess == "rounded_result":
        mess="\n Please note: \n if necessary, result is rounded 5 numbers after comma: \n 0.12345678 -> 0.12346 \n - \n"
    message_text.set(mess)
    
def input_key(input_value):
    """
    function input_key catch the input value and concatenate simples numbers to
    display the desired complete nbr in 2 areas : "cal_input_text" and "e"
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
    pass the actual value to the negative 
    and display it in the 2 same areas as input_key
    """
    print(e_value)
    print(type(e_value))
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
    catch the actual value displayed in e 
    It return it to be used in calculator's functions
    """
    actual_nbr = e.get()
    return actual_nbr

    
def input_operator(operator,actualValue):
    """
    catch the value of operator entered + actual value in e
      1/ add actaul value in the array myOperations calling the function : put_in_myOperations(actualValue) in basic_op.py
      2/ print operator in the second display: calc_input
      3/delete the e display (usual attitude of a calculator)
      4/ send the actual value to the function make_operation in basic_op.py and return the result in cas of user make this = 2+1+, to display 3 as he enter "="
    """
    set_message()
    global calc_input
    if operator=="pourcent":
        set_message("how_to_use_pourcent")
        
    #1
    basic_op.put_in_myOperations(actualValue)
    #2
    
    calc_input += e.get()
    if operator=="pourcent":
        operator = "% of "
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
    to clear all values displayed in the 2 display areas.
    use function clear_myOperations in basic_op.py to empty the array 'myOperations'
    """
    set_message()
    
    global calc_input
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(calc_input) 
    e.delete(0,END)
    
    global neg_value
    neg_value= False
    
    basic_op.clear_myOperations()


def input_sci_op(input_sci_value, actual_value):
    set_message()
    value = round(actual_value,5)
    result = scientific.scientific_op(input_sci_value, value)
    if input_sci_value == "racine":
        input_sci_value = "√"
    
    calc_input = input_sci_value + " (" +value + ") = "
    calc_input_text.set(calc_input)
    result_text.set(result) 



# create graphic interface:
#row 0 : to close
button_close =Button(window, text="Close", command=window.quit).grid(row=0, column=4, columnspan=2)

#row 1 : usual calculator display
e = Entry(window, width=20, justify=RIGHT, borderwidth=2)
e.grid(row=1,column=0,columnspan=6, padx=10, pady=10)

#row 2 & 3 : special display + row 4 :space
calc_input_text = StringVar()
Label(window, textvariable=calc_input_text,justify=RIGHT).grid(row=2, column=0, columnspan=5)
Label(window, textvariable="=").grid(row=2, column=5)

result_text = StringVar()
Label(window, textvariable=result_text, justify=RIGHT).grid(row=3, column=0, columnspan=6)

#rows 5 -> 9: buttons
button_sin =Button(window, text="sin", command=lambda: input_sci_op("sin", get_e_value())).grid(row=5, column=0)
button_fraction =Button(window, text="1/x", command=lambda: input_sci_op("fraction", get_e_value())).grid(row=5, column=1)
button_pourcent =Button(window, text="%", command=lambda: input_operator("pourcent", get_e_value())).grid(row=5, column=2)
button_negative =Button(window, text="+/-", command=lambda: input_neg_value(get_e_value())).grid(row=5, column=3)
button_clear =Button(window, text="A/C", command=lambda: input_clear()).grid(row=5, column=4,columnspan=2 )

button_tan =Button(window, text="tan", command=lambda: input_sci_op("tan", get_e_value())).grid(row=6, column=0)
button_7 =Button(window, text=" 7 ", command=lambda: input_key("7")).grid(row=6, column=1)
button_8 =Button(window, text=" 8 ", command=lambda: input_key("8")).grid(row=6, column=2)
button_9 =Button(window, text=" 9 ", command=lambda: input_key("9")).grid(row=6, column=3)
button_divide =Button(window, text=" / ", command=lambda: input_operator("/", get_e_value())).grid(row=6, column=4)
button_eqal =Button(window, text=" = ", command=lambda: input_eqal(get_e_value())).grid(row=6, column=5,rowspan=4 )    

button_cos =Button(window, text="cos", command=lambda: input_sci_op("cos", get_e_value())).grid(row=7, column=0)
button_4 =Button(window, text=" 4 ", command=lambda: input_key("4")).grid(row=7, column=1)
button_5 =Button(window, text=" 5 ", command=lambda: input_key("5")).grid(row=7, column=2)
button_6 =Button(window, text=" 6 ", command=lambda: input_key("6")).grid(row=7, column=3)
button_multiply =Button(window, text=" x ", command=lambda: input_operator("*", get_e_value())).grid(row=7, column=4)

button_pi =Button(window, text=" π ", command=lambda: input_key("pi")).grid(row=8, column=0)
button_1 =Button(window, text=" 1 ", command=lambda: input_key("1")).grid(row=8, column=1)
button_2 =Button(window, text=" 2 ", command=lambda: input_key("2")).grid(row=8, column=2)
button_3 =Button(window, text=" 3 ", command=lambda: input_key("3")).grid(row=8, column=3)
button_substract =Button(window, text=" - ", command=lambda: input_operator("-", get_e_value())).grid(row=8, column=4)

button_racine =Button(window, text=" √ ", command=lambda: input_sci_op("racine", get_e_value())).grid(row=9, column=0)
button_0 =Button(window, text=" 0 ", command=lambda: input_key("0")).grid(row=9, column=1, columnspan=2)
button_virg =Button(window, text=" . ", command=lambda: input_key(".")).grid(row=9, column=3)
button_add =Button(window, text=" + ", command=lambda: input_operator("+", get_e_value())).grid(row=9, column=4)

message_text = StringVar()
Label(window, textvariable=message_text, justify=CENTER).grid(row=10, column=0, columnspan=6)


                                     




#end of graphic interface

window.mainloop()