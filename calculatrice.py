from tkinter import * 
# to generate a window with tkinter
window = Tk()
window.title("Elo's calculator")

"""
all global needed during the process 
    -> calc_input = string of all the operation required / 
    -> f_nb       = first number entered by the user
    -> operator   = operator used
    -> result     = reuslt of last operation
"""
calc_input=""
f_nb=""
operator=""
result=""


def input_key(value):
    """
    function input_key catch the input value and return a string contening the desired equation
    calc_input is a global var to keep the value even after exiting of the function
    """
    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)#print on a secondary display, to keep?
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(value))

def input_operator(inputOperator):
    """
    function input_operator catch : catch the first value  +  the input operator
    it take them in global
    calc_input += inputOperator is a string witch return numbers and operators
    """
    first_nbr = e.get()
    global f_nb
    f_nb = int(first_nbr)
    global operator
    operator = inputOperator
    
    global calc_input
    calc_input += inputOperator
    calc_input_text.set(calc_input)#print on a secondary display, to keep?
    
    e.delete(0,END)
   
    
def equal():
    """
    catch the second number entered by user (second_nbr)
    catch the operator
    calculate the equation between first_nbr et second_nbr according to the choosen operator
    """
    result = 0
    second_nbr= e.get()
    e.delete(0,END)
    global operator

    if operator == "+": #autres test : avec switch n existe pas et en utilisant un dictionnaire ne retourne que des str
        result = f_nb + int(second_nbr)
    elif operator== "-":
        result = f_nb - int(second_nbr)
    elif operator== "*":
        result = f_nb * int(second_nbr)
    elif operator== "/":
        result = f_nb / int(second_nbr)
        
    global calc_input #to print on a secondary display, to keep?
    calc_input += "="+str(result)#to print on a secondary display, to keep?
    result_text.set(result)#to print on a secondary display, to keep?
    
    e.insert(0, result)
    
def clear():
    """
    to fill the interface to looks like a calculator:
    """
    global calc_input
    calc_input = ""
    print(calc_input) #test console
    calc_input_text.set(calc_input) #clear the secondary display, to keep?
    result_text.set(calc_input) #clear the secondary display, to keep?
    e.delete(0,END)
   
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
button_add =Button(window, text=" + ", command=lambda: input_operator("+")).grid(row=3, column=3)
button_substract =Button(window, text=" - ", command=lambda: input_operator("-")).grid(row=4, column=3)
button_multiply =Button(window, text=" x ", command=lambda: input_operator("*")).grid(row=5, column=3)
button_divide =Button(window, text=" / ", command=lambda: input_operator("/")).grid(row=6, column=3)

button_aqual =Button(window, text=" = ", command=lambda: equal()).grid(row=2, column=3)                                         
button_clear =Button(window, text=" clear ", command=lambda: clear()).grid(row=6, column=1,columnspan=2 )

calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row=1, column=0, columnspan=3)

result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, column=0, columnspan=3)

#end of graphic interface

window.mainloop()