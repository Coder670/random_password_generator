from PIL import Image, ImageTk
import random
import Tkinter as tk

window = tk.Tk()
window.geometry("400x300")
window.title("Random Password Generator")

#--------FUNCTIONS---------
def password_generator():
    characters = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9,!,@,#,$,%,&,*,?'

    # This turns the characters string into a list
    characters = characters.split(",")
    length_of_password = int(numOfchar_input.get())
    password = []
    for i in range(length_of_password):
        password.append(characters[random.randint(0, len(characters)-1)])
    password = ''.join(password)
    return password

def password_display():
    password1 = password_generator()

    # This creates a text field.
    text_answer = tk.Text(master=window, height=10, width=30)
    text_answer.grid(column=0, row=5)

	#This prints out the password into the text field.
    text_answer.insert(tk.END, password1)

#--------BUTTONS----------
click_me_button = tk.Button(text="Click me!", command=password_display)
click_me_button.grid(column= 0,row= 3)

#--------LABELS-----------
title_prompt = tk.Label(text="""Welcome to the
Random Password Generator""")
title_prompt.grid(column= 0,row= 1)

character_input_prompt = tk.Label(text= """How many characters do you
want your password to have?""")
character_input_prompt.grid(column= 0,row=2 )

#--------ENTRIES-----------
numOfchar_input = tk.Entry()
numOfchar_input.grid(column= 1,row= 2)

#-------IMAGES------------
image = Image.open("password_cryptography.jpg")
image.thumbnail((100,100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column= 1,row=0)

window.mainloop()
