"""
McMaster University Course 3K04 Final Project
The Device Controller-Monitor (DCM) for pacemacker
Last Revision: 
"""

from tkinter import *
import os

creds = 'UserInfo.txt' # text file to store the User information


"""
@brief: Welcome Screen

@Object: Display -> Display the welcome word
         Start -> Button that leads the user to the Login screen or Sign-up Screen if no User exists
"""
def Welcome():
    global wel
    wel = Tk()
    wel.title('Welcome to Device-Control Display')
    Display = Label(wel, text='Welcome to Device-Control Display!',width="80",heigh="3")
    Display.grid(rowspan=2,columnspan=3)

    Start = Button(wel,text='Enter',width="5",heigh='1',command=Enter)
    Start.grid(row=2,columnspan=3)
    
"""
@brief: Pacemaker Control Panel

@Object: 
"""


def ControlPanel():
    destroy_r() # Destroy the System Message Screen
    Panel = Tk()
    Panel.title('User Control Panel')
    instruction = Label(Panel,'Welcome to the Control Panel!')
    instruction.grid(row=0,columnspan=3,sticky=W)
    
    MSR = Label(Panel,'Maximum Sensor Rate').grid(row=1,column=0,sticky=E)

"""
@brief: Sign up a new user

@object: roots -> The Signup Screen
         instrution -> Display the text
         nameL -> Display "New Username"
         nameE -> New User's username
         pwordE -> New User's password
         pwordL -> Display "New Password"
         nameE -> Entry to input the New username
         pwordE -> Entry to input the password
         signupButton -> Button to execute the signup command
"""
    
 
def Signup(): 
    global pwordE 
    global nameE
    global roots
    
    if os.path.isfile(creds): # The existence of the file shows we are access the Signup Screen by Login Screen. So, we need to destroy the Login Screen
        rootA.destroy()
    roots = Tk() 
    roots.title('Signup')
    intruction = Label(roots, text='Please Enter new Credidentials\n') 
    intruction.grid(row=0, column=0, sticky=E) 
 
    nameL = Label(roots, text='New Username: ') 
    pwordL = Label(roots, text='New Password: ') 
    nameL.grid(row=1, column=0, sticky=W) 
    pwordL.grid(row=2, column=0, sticky=W) 
 
    nameE = Entry(roots) 
    pwordE = Entry(roots, show='*') 
    nameE.grid(row=1, column=1) 
    pwordE.grid(row=2, column=1) 
 
    signupButton = Button(roots, text='Signup', command=FSSignup) 
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop()


    

"""
@brief:Sent the New User's information to the information file

@Objects:f -> The information file
"""



 
def FSSignup():
    if os.path.isfile(creds): #Check the existence of the file. If file exists, we need to append the file with new user's information, else we create a new user information file
        f=open(creds, 'a')
        f.write('\n')
        f.write(nameE.get()) 
        f.write('\n')
        f.write(pwordE.get()) 
        f.close()
    else:
        f=open(creds, 'w')
        f.write(nameE.get()) 
        f.write('\n')
        f.write(pwordE.get()) 
        f.close() 
    roots.destroy() # After transmittion is finished, destroy the Signup Screen 
    Login()

    
"""
@brief: Login Screen

@Object:rootA -> Login Screen
        nameEL -> Username
        pwordEL -> password
        nameL -> Display the text "Username"
        pwordL -> Display the text "Password"
        loginB -> Button to execute Login command
        NewUser -> Button to execute Signup command
"""



def Login():
    global nameEL
    global pwordEL 
    global rootA
 
    rootA = Tk() 
    rootA.title('Login') 
 
    intruction = Label(rootA, text='Please Login\n') 
    intruction.grid(sticky=E)
 
    nameL = Label(rootA, text='Username: ')
    pwordL = Label(rootA, text='Password: ') 
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin)
    loginB.grid(columnspan=2, sticky=W)

    NewUser = Button(rootA, text='New User',command=Signup)
    NewUser.grid(columnspan=2, sticky = W)


"""
@brief: Check Correctness of User's Information 

@para:Check -> Whether the input is match to the account information or not
      data -> the content in UIF
      num -> Number of lines of the User Information File(UIF)
      uname -> Username in UIF
      pword -> password in UIF

@Object:r -> System Message Screen (Shows the result of login)
        f -> User information file
        instruction -> the Message form the system
        r2b2 -> Button to go to the Control Panel Screen
        r1b2 -> Button to go back to the Login Screen
"""


 
def CheckLogin():
    global r
    Check = 0
    with open(creds,'r') as f:
        data = f.readlines() 
        num = len(data)
        for i in range(int(num/2)):
            uname = data[i*2].rstrip() 
            pword = data[i*2+1].rstrip() 
            if nameEL.get() == uname and pwordEL.get() == pword:
                Check = 1
                break
    if Check == True: 
        r = Tk() 
        r.title('System Message')
        instruction = Label(r, text='\n Logged In')
        instruction.grid(row=0,columnspan=3)
        r2b2 = Button(r,text='Next',command=ControlPanel)
        r2b2.grid(row=1,columnspan=3)
    else:
        r = Tk()
        r.title('System Message')
        instruction = Label(r, text='\n[!] Invalid Login')
        instruction.grid(row=0,sticky=W)
        r1b2 = Button(r, text='back',command = destroy_r)
        r1b2.grid(row=1,sticky=W)

"""
@brief:Destroy the System Message Screen
"""

def destroy_r():
    r.destroy()

"""
@brief: Check which screen to go after the Welcome Screen (If No user information, go to Signup Screen first)
"""

def Enter():
    wel.destroy()
    if os.path.isfile(creds):
        Login()
    else: 
        Signup()



Welcome() # The System goes to Welcome Screen everytime the program is executed
