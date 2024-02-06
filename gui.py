import tkinter as tk

root=tk.Tk()
root.geometry("600x600")
calculation=""
def add_to_calculation(e):

    global calculation
    calculation+=str(e)
    user_input.delete(1.0,"end")
    user_input.insert(1.0,calculation)
def show_result():
    global calculation
    try:
        calculation=eval(calculation)
        user_input.delete(1.0,"end")
        user_input.insert(1.0,calculation)
    except:
        clear_field()
        user_input.insert(1.0,"end")
        
def clear_field():
            global   calculation
            calculation=""
            user_input.delete(1.0,"end")
            user_input.insert(1.0,calculation)

            


user_input=tk.Text(root,font=("Arial","10"),height=6, width=40)

user_input.grid(row=0,column=0,columnspan=4)
button_1=tk.Button(root,text="1",width=9,font=("Helvetica",'10'),command=lambda:add_to_calculation(1))
button_1.grid(row=1,column=0)
button_2=tk.Button(root,text="2",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(2))
button_2.grid(row=1,column=1)
button_3=tk.Button(root,text="3",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(3))
button_3.grid(row=1,column=2)
button_7=tk.Button(root,text="+",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation("+"))
button_7.grid(row=1,column=3)

button_4=tk.Button(root,text="4",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(4))
button_4.grid(row=2,column=0)
button_5=tk.Button(root,text="5",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(5))
button_5.grid(row=2,column=1)
button_6=tk.Button(root,text="6",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(6))
button_6.grid(row=2,column=2)
button_8=tk.Button(root,text="-",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation("-"))
button_8.grid(row=2,column=3)
button_9=tk.Button(root,text="7",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(7))
button_9.grid(row=3,column=0)
button_10=tk.Button(root,text="8",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(8))
button_10.grid(row=3,column=1)
button_11=tk.Button(root,text="9",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation(9))
button_11.grid(row=3,column=2)
button_11=tk.Button(root,text="*",width=9,font=("Times New Roman","10"),command=lambda:add_to_calculation("*"))
button_11.grid(row=3,column=3)
button_12=tk.Button(root,text="CE",width=9,font=("Times New Roman","10"),command=lambda:clear_field())
button_12.grid(row=4,column=0)
button_13=tk.Button(root,text="0",width=9,font=("Times New roman","10"),command=lambda:add_to_calculation(0))
button_13.grid(row=4,column=1)
button_14=tk.Button(root,text="00",width=9,font=("Times New roman","10"),command=lambda:add_to_calculation(00))
button_14.grid(row=4,column=2)
button_14=tk.Button(root,text="=",width=9,font=("Times New roman","10"),command=lambda:show_result())
button_14.grid(row=4,column=3)

root.mainloop()
