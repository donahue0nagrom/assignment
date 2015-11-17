a= int(input("Enter the first operand: "))
op=input("Enter the operator: ")
b=int(input("Enter the second operand: "))

if (op=="+"):
    c=a+b
elif (op=="-"):
    c=a-b
elif (op=="/"):
    c=a/b
else:
    c=a*b

from tkinter import *
master= Tk()

canvas_width=750
canvas_height=750

w=Canvas(master,width=canvas_width,height=canvas_height)
w.pack()



result=(a,op,b,"=",c)
w.create_text(canvas_width/1.95,canvas_height/4.7,font=("Arial",22), text="result", fill="blue")
