#McMaster University Course 3K04 Final Project
#The Device Controller-Monitor (DCM) for pacemacker
#Last Revision: 


from tkinter import *

from Modifier import *

import os

global LRL_Input
global URL_Input
global AtrAmp_Input
global APW_Input


global LRL_Input
global URL_Input
global VtrAmp_Input
global VPW_Input

global AtrSen_Input
global ARP_Input
global PVARP_Input
global Hysteresis_Input
global RateSmoothing_Input

creds = 'UserInfo.txt' # text file to store the User information
creds2 = 'Parameter List' # text file to store the Parameter List   



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
    global pwordE 
    global nameE
    global roots
    
    if os.path.isfile(creds): # The existence of the file shows we are access the Signup Screen by Login Screen. So, we need to destroy the Login Screen
        rootA.destroy()
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
    if os.path.isfile(creds): #Check the existence of the file. If file exists, we need to append the file with new user's information, else we create a new user information file
        f=open(creds, 'r')
        data = f.readlines() 
        num = len(data)
      
        f.close
        if (num >= 20):
            nk = Tk()
            instruction = Label(nk,text = "Maximum Number of Users !!!!")
            instruction.grid(row=0)
        else:
            file2=open(creds,'a')
            file2.write(nameE.get()) 
            file2.write('\n')
            file2.write(pwordE.get())
            file2.write('\n')
            file2.close()
            Login()
    else:
        f=open(creds, 'w')
        f.write(nameE.get()) 
        f.write('\n')
        f.write(pwordE.get())
        f.write('\n')
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
        r2b2 = Button(r,text='Next',command=ModesControlPanel)
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

"""
@brief: Display all the Mode available to choose after the User successfully login to the system
@object: mcp -> the ModeControlPanel Screen
         Mode_Button -> The Button that lead User to the Mode Modifier after User presses it.
"""

def ModesControlPanel():
    global mcp
    rootA.destroy();
    destroy_r();
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
    AAI_Button = Button(mcp, text='AAI', command=OFF_Mode_Modifier) 
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
    cc_Button = Button(mcp, text='Check\nConnection',command=checkConnection) 
    cc_Button.grid(row=9,column=2)
    sp2L = Label(mcp, text = "")
    sp2L.grid(row=10,columnspan=1,column=2)
    di_Button = Button(mcp, text='Check\nDevice Info',command=checkDeviceInfo) 
    di_Button.grid(row=11,column=2)

       
"""
@brief: Check the connection of the pacemaker. This function will be used in further assignments
"""

def checkConnection():
    connected=True
    if(connected):
        con = Tk();
        con.title("Connection Status")
        con.geometry("220x30")
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
