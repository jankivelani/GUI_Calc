from tkinter import *

win=Tk()#this is to create basic window
win.geometry("312x324")#for the size of window
win.resizable(0,0)#its prevent resize
win.title("calculator")

#btn_click functuion:
#This function continously update the input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression+str(item)
    input_text.set(expression)
    
#btn_clear funtion : this is used to clear the input field

def btn_clear():
    global expression
    expression=""
    input_text.set("")
    
def btn_equal():
    global expression
    result=str(eval(expression))
    input_text.set(result)
    expression=""
    
expression=""
#stringvar is instance of the input feild
input_text=StringVar()

#lets creating a frame for the input feild

input_frame =Frame(win,width=312,height=50,bd =0,highlightbackground="black",highlightcolor="black",highlightthickness=2)
input_frame.pack(side=TOP)

input_field=Entry(input_frame, font=('arial',18,'bold'),textvariable=input_text,width=50,bg="#eee",bd=0, justify=RIGHT)

input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btns_frame=Frame(win,width=312,height=272.5,bg="grey")
btns_frame.pack()

#first row 

clear=Button(btns_frame,text="C",fg="black",width=32,height=3,bd=0,bg="#eee",cursor="hand2",command = lambda:btn_clear()).grid(row=0,column=0,columnspan = 3, padx=1, pady=1)  

divide=Button(btns_frame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command=
lambda:btn_click("/")).grid(row=0,column=3,padx=1,pady=1)

#second row

seven=Button(btns_frame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command = lambda:btn_click(7)).grid(row=1,column=0,padx=1,pady=1)

eight=Button(btns_frame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command = lambda:btn_click(8)).grid(row=1,column=1,padx=1,pady=1)

nine=Button(btns_frame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2",command = lambda:btn_click(9)).grid(row=1,column=2,padx=1,pady=1)

multiply=Button(btns_frame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2",command = lambda:btn_click("*")).grid(row=1,column=3,padx=1,pady=1)

#third row

four=Button(btns_frame,text="4",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2" ,command = lambda: btn_click(4)).grid(row=2,column=0,padx=1,pady=1)

five=Button(btns_frame,text="5",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2", command = lambda: btn_click(5)).grid(row=2,column=1,padx=1,pady=1)

six=Button(btns_frame,text="6",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2", command = lambda: btn_click(6)).grid(row=2,column=2,padx=1,pady=1)

minus=Button(btns_frame,text="-",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2", command = lambda: btn_click("-")).grid(row=2,column=3,padx=1,pady=1)

#fourth row
one=Button(btns_frame,text="1",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2" ,command = lambda: btn_click(1)).grid(row=3,column=0,padx=1,pady=1)

two=Button(btns_frame,text="2",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2" ,command = lambda: btn_click(2)).grid(row=3,column=1,padx=1, pady=1)

three=Button(btns_frame,text="3",fg="black",width=10,height=3,bd=0,bg="#fff",cursor="hand2" ,command = lambda: btn_click(3)).grid(row=3,column=2,padx=1,pady=1)

plus=Button(btns_frame,text="+",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2", command = lambda: btn_click("+")).grid(row=3,column=3,padx=1,pady=1)

#fifth row

zero=Button(btns_frame,text="0",fg="black",width=21,height=3,bd=0,bg="#fff",cursor="hand2" ,command = lambda: btn_click(2)).grid(row=4,column=0,columnspan=2,padx=1,pady=1)

point=Button(btns_frame,text=".",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2", command = lambda: btn_click(3)).grid(row=4,column=2,padx=1,pady=1)

equals=Button(btns_frame,text="=",fg="black",width=10,height=3,bd=0,bg="#eee",cursor="hand2", command = lambda: btn_equal()).grid(row=4,column=3,padx=1,pady=1)

win.mainloop()