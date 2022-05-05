from tkinter import *
import random

def activate(x): # activates certain characters that you want in your password by adding to list, or removing
    for i in range(len(options)):
        if x == options[i][0]:
            if options[i][1].get() == 1:
                ls.extend(options[i][2].split())
            else:
                temp = options[i][2].split()
                for a in temp:
                    ls.remove(a)
    

def createPassword(ls): # creates the password using the characters in list ls
    temp = ''
    for i in range(scale.get()):
        x = random.randint(0, len(ls) - 1)
        temp += ls[x]
    password.set(temp)
    generated.configure(text='Your password is: ' + password.get())
    save_label.grid(row = j + 3)
    save_button.grid(row = j+3, column=1)

def name_password(): # creates confirm password and save to file window 
    def save_to_file(): # saves to file set as with the password and entry they gave
        f = open('Passwords.txt', 'a')
        f.write(f'\n{entry_str.get()}: {password.get()}')
        f.close()
        cfm.destroy()
        root.destroy()
    cfm = Tk()
    entry_str = StringVar(cfm)
    Label(cfm, text = 'Name of password:').grid(row=0)
    e = Entry(cfm, textvariable=entry_str)
    e.grid(row=0,column=1)

    Label(cfm, text='Your password is:').grid(row=1)
    Label(cfm, text = password.get()).grid(row=1, column=1)

    #cfm.bind('<Return>', lambda e=e.get(), name=password.get(): save_to_file(e, name))
    Button(cfm, text='Save', command=save_to_file).grid(row=2, columnspan=2)



ls = [] # list that stores all the characters that can be in the password

# initializes the window and top text
root = Tk()
frm = Frame(root, padx=10, pady=10)
frm.grid()
Label(frm, text = "What Features Would You Like Your Password To Have?").grid(row = 0, columnspan=2)

# options list with tuples of type of character, on/off variable, and the characters as a string
var0, var1, var2, var3 = IntVar(), IntVar(), IntVar(), IntVar()
options = [ ("Lowercase letters", var0, 'a b c d e f g h i j k l m n o p q r s t u v w x y z'), 
            ("Uppercase letters", var1, 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'), 
            ("Numbers", var2, '1 2 3 4 5 6 7 8 9'), 
            ('Other characters', var3, "! @ # $ % ^ & * ( ) _ + ~ { } | : \" < > ? ` - = [ ] ; ' , . /")]

# creating the labels and checkbuttons for everything in options list
j = 1
for i, var, stuff in options:
    Label(frm, text = i,).grid(row = j)
    Checkbutton(frm, variable=var, command=lambda i=i: activate(i)).grid(row = j, column = 1)
    j += 1

#length of password label and scale creation
Label(frm, text = 'Length of password:').grid(row=j) 
scale = Scale(frm, from_=5, to=25, orient = HORIZONTAL)
scale.set(12)
scale.grid(row=j, column = 1)

# create my password label and button creation
password = StringVar()
Button(frm, text = 'Create my password!', command=lambda: createPassword(ls)).grid(row = j+1, columnspan=2)
generated = Label(frm, text = 'Your password is: ', width=50)
generated.grid(row = j + 2)

# save password to file label and button that calls name_password function
save_label = Label(frm, text = 'Do you want to save your password to the passwords file?')
save_button = Button(frm, text = 'Yes', command=name_password)
root.mainloop()