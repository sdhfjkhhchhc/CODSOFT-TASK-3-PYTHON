''' CODSOFT Internship - PYTHON PROGRAMMING 
    TASK 3 - PASSWORD GENERATOR
    DONE BY Moneesh S
'''

import tkinter #create the layout
import string #for creating digits
import random #random letter generator
import pyperclip #used for copy the generated password

from tkinter import*



root =Tk()
root.title("Password generator by Moneesh S")
root.geometry("370x550+400+100")#creating dimensions  and resolution
root.resizable(False,False)#to fix the lay out
root.configure(bg="#ffc0cb")#backgroung colour


#For generating the password
def generate():
    small_alphabets=string.ascii_lowercase  
    capital_alphabet=string.ascii_uppercase 
    numbers=string.digits
    special_characters=string.punctuation   

    all=small_alphabets+capital_alphabet+numbers+special_characters #mixing of letters
    passwordlength=int(length_box.get())  #generated password=length of the password given by user

    #password=random.sample(all,passwordlength)
    #passwordDisplay.insert(0,password)

#Based upon the user input  we can able to generate the password     

    if choice.get()==1: #weak password
        passwordDisplay.insert(0,random.sample(small_alphabets,passwordlength))

    if choice.get()==2: #medium password
        passwordDisplay.insert(0,random.sample(small_alphabets+capital_alphabet,passwordlength))

    if choice.get()==3: #hard or strong password
        passwordDisplay.insert(0,random.sample(all,passwordlength))

def copy(): #for copying the password weneed to import pyperclip
    random_password=passwordDisplay.get()
    pyperclip.copy(random_password)

choice=IntVar()

# application icon
app_icon = PhotoImage(file="Image/password.png")
root.iconphoto(False,app_icon)



#application name
passwordLabel=Label(root,text="Password Generator",font="arial 20 bold",fg="black",bg="#ffc0cb")
passwordLabel.place(x=55,y=20)

#weak button font,color,text,size,position
weakbutton=Radiobutton(root,text="weak",value=1,variable=choice,font="arial 15 bold",fg="black",bg="#ffc0cb")
weakbutton.grid(pady=10)
weakbutton.place(x=23.33,y=130)

#medium button font,color,text,size,position
mediumbutton=Radiobutton(root,text="Medium",value=2,variable=choice,font="arial 15 bold",fg="black",bg="#ffc0cb")
mediumbutton.grid(pady=10)
mediumbutton.place(x=140,y=130)

#hard button font,color,text,size,position
hardbutton=Radiobutton(root,text="Hard",value=3,variable=choice,font="arial 15 bold",fg="black",bg="#ffc0cb")
hardbutton.grid(pady=10)
hardbutton.place(x=270,y=130)

#crete the text=password length and its size,position,font,color
passwordlengthLabel=Label(root,text="Password length",font="arial 20 bold",fg="black",bg="#ffc0cb")
passwordlengthLabel.place(x=15,y=240)

#create the Spinbox to get the user input from initial to final value and fix its size,position,color
length_box=Spinbox(root,from_=6,to_=19,width=5,font="arial 20 bold")
length_box.grid()
length_box.place(x=250,y=240)

#create the generate button to get the output letters in display unit
generatebuttton=Button(root,text="Generate",font="arial 20 bold",command=generate)
generatebuttton.grid(pady=300,padx=110)

#here the user can able to see their generated password
passwordDisplay=Entry(root,width=20,bd=2,font="arial 20 bold")
passwordDisplay.grid()
passwordDisplay.place(x=40,y=410)

#copybutton is placed to copy the generated password
copybutton=Button(root,text="COPY",font="arial 20 bold",command=copy)
copybutton.grid(pady=5)
copybutton.place(x=140,y=470)


#for the excution of program in loop condition
root.mainloop()
