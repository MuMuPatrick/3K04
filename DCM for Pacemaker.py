#McMaster University Course 3K04 Final Project
#The Device Controller-Monitor (DCM) for pacemacker
#Last Revision: 


from tkinter import *
from tkinter import messagebox

from Modifier import *

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
    global roots
    global nameE
    global pwordE
    
    if os.access("Users",os.F_OK): # The existence of the file shows we are access the Signup Screen by Login Screen. So, we need to destroy the Login Screen
        rootA.destroy()
    else:
        os.mkdir('Users')
    roots = Tk() 
    roots.title('Signup')
    instruction = Label(roots, text='Please Enter new Credidentials\n') 
    instruction.grid(row=0, column=0, sticky=E) 
 
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
    
    os.chdir('./Users')
    readfiles = os.listdir(os.getcwd())
    num = len(readfiles)
    User = nameE.get()
    Password = pwordE.get()
    
    if num >= 20:
        messagebox.showerror("System Message", "Maximun Number of Users !!!")
    elif os.access(User,os.F_OK):
        messagebox.showerror("System Message", "User has already existed !!!")
    else:
        os.mkdir(User)
        os.chdir('./'+ User)
        f=open(creds, 'w')
        f.write(User) 
        f.write('\n')
        f.write(Password)
        f.write('\n')
        f.close()
        os.chdir('..')
    
    roots.destroy() # After transmittion is finished, destroy the Signup Screen
    os.chdir('..')
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
    global rootA
    global nameEL
    global pwordEL
    
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
    os.chdir('./Users')
    User = nameEL.get()
    Password = pwordEL.get()
    if os.access(User,os.F_OK) == FALSE :
        messagebox.showerror('System Message', 'Invalid Username')
    else:
        os.chdir('./' + User)
        with open(creds,'r') as f:
            data = f.readlines()
            TruePword = data[1]
            f.close()
        os.chdir('..')
        os.chdir('..')
        if TruePword != Password+'\n':
            messagebox.showerror('System Message', 'Invalid Password')
        else:
            ModesControlPanel()

"""
@brief: Check which screen to go after the Welcome Screen (If No user information, go to Signup Screen first)
"""

def Enter():
    wel.destroy()
    if os.access('Users',os.F_OK):
        Login()
    else:
        Signup()

"""
@brief: Display all the Mode available to choose after the User successfully login to the system
@object: mcp -> the ModeControlPanel Screen
         Mode_Button -> The Button that lead User to the Mode Modifier after User presses it.
"""

def ModesControlPanel():
    global mcp
    rootA.destroy();
    mcp = Tk() 
    mcp.title('Modes')
    mcp.geometry("200x350")

    OFF_Button = Button(mcp, text='OFF', command=OFF_Mode_Modifier) 
    OFF_Button.grid(row=1,column=1)
    
    AOO_Button = Button(mcp, text='AOO', command=AOO_Mode_Modifier) 
    AOO_Button.grid(row=1,column=2)
    
    VOO_Button = Button(mcp, text='VOO', command=VOO_Mode_Modifier) 
    VOO_Button.grid(row=1,column=3)
    
    DDI_Button = Button(mcp, text='DDI', command=OFF_Mode_Modifier) 
    DDI_Button.grid(row=2,column=1)
    
    DOO_Button = Button(mcp, text='DOO', command=OFF_Mode_Modifier) 
    DOO_Button.grid(row=2,column=2)
    
    DDD_Button = Button(mcp, text='DDD', command=OFF_Mode_Modifier) 
    DDD_Button.grid(row=2,column=3)
    
    AAI_Button = Button(mcp, text='AAI', command=AAI_Mode_Modifier) 
    AAI_Button.grid(row=3,column=1)
    
    VDD_Button = Button(mcp, text='VDD', command=OFF_Mode_Modifier) 
    VDD_Button.grid(row=3,column=2)
    
    VVI_Button = Button(mcp, text='VVI', command=VVI_Mode_Modifier) 
    VVI_Button.grid(row=3,column=3)
    
    AAT_Button = Button(mcp, text='AAT', command=OFF_Mode_Modifier) 
    AAT_Button.grid(row=4,column=1)
    
    VVT_Button = Button(mcp, text='VVT', command=OFF_Mode_Modifier) 
    VVT_Button.grid(row=4,column=2)
    
    DDDR_Button = Button(mcp, text='DDDR', command=OFF_Mode_Modifier) 
    DDDR_Button.grid(row=4,column=3)
    
    VDDR_Button = Button(mcp, text='VDDR', command=OFF_Mode_Modifier) 
    VDDR_Button.grid(row=5,column=1)
    
    DDIR_Button = Button(mcp, text='DDIR', command=OFF_Mode_Modifier) 
    DDIR_Button.grid(row=5,column=2)
    
    DOOR_Button = Button(mcp, text='DOOR', command=OFF_Mode_Modifier) 
    DOOR_Button.grid(row=5,column=3)
    
    AOOR_Button = Button(mcp, text='AOOR', command=OFF_Mode_Modifier) 
    AOOR_Button.grid(row=6,column=1)
    
    AAIR_Button = Button(mcp, text='AAIR', command=OFF_Mode_Modifier) 
    AAIR_Button.grid(row=6,column=2)
    
    VOOR_Button = Button(mcp, text='VOOR', command=OFF_Mode_Modifier) 
    VOOR_Button.grid(row=6,column=3)
    
    VVIR_Button = Button(mcp, text='VVIR', command=OFF_Mode_Modifier) 
    VVIR_Button.grid(row=7,column=1)
    
    spL = Label(mcp, text = "")
    spL.grid(row=8,columnspan=1,column=2)
    cc_Button = Button(mcp, text='Connect',command=connect)
    cc_Button.grid(row=9,column=2)
    sp2L = Label(mcp, text = "")
    sp2L.grid(row=10,columnspan=1,column=2)
    di_Button = Button(mcp, text='Check\nDevice Info',command=checkDeviceInfo) 
    di_Button.grid(row=11,column=2)

       
"""
@brief: Check the connection of the pacemaker. This function will be used in further assignments
"""

def connect():
    connected=True
    if(connected):
        con = Tk();
        con.title("Connection Status")
        con.geometry("220x30")
        #######################################
        #put our serial configuration codes here
        
        #######################################
        connectedL = Label(con, text="             device connected",fg='blue',anchor='center')
        connectedL.grid(row=1,columnspan=1)


"""
@brief: Check the Device Code. This  function will be used in further assignments
"""

def checkDeviceInfo():
    connected=True
    if(connected):
        di = Tk();
        di.title("Device")
        di.geometry("100x30")
        diL = Label(di, text="      device 1",fg='blue',anchor='center')
        diL.grid(row=1,columnspan=1)


Welcome() # The System goes to Welcome Screen everytime the program is executed
