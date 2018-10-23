#McMaster University Course 3K04 Final Project
#The Device Controller-Monitor (DCM) for pacemacker
#Last Revision: 


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
        f=open(creds, 'a')
        f.write('\n')
        f.write(nameE.get()) 
        f.write('\n')
        f.write(pwordE.get())
        f.write('\n\n')
        f.close()
    else:
        f=open(creds, 'w')
        f.write(nameE.get()) 
        f.write('\n')
        f.write(pwordE.get())
        f.write('\n\n')
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
    rootA.destroy();
    destroy_r();
    mcp = Tk() 
    mcp.title('Modes')
    mcp.geometry("150x200")
    OFF_Button = Button(mcp, text='OFF', command=OFF_Mode_Modifier) 
    OFF_Button.grid(row=1,column=1)
    DDD_Button = Button(mcp, text='DDD', command=OFF_Mode_Modifier) 
    DDD_Button.grid(row=1,column=2)
    VDD_Button = Button(mcp, text='VDD', command=OFF_Mode_Modifier) 
    VDD_Button.grid(row=1,column=3)
    DDI_Button = Button(mcp, text='DDI', command=OFF_Mode_Modifier) 
    DDI_Button.grid(row=2,column=1)
    DOO_Button = Button(mcp, text='DOO', command=OFF_Mode_Modifier) 
    DOO_Button.grid(row=2,column=2)
    AOO_Button = Button(mcp, text='AOO', command=AOO_Mode_Modifier) 
    AOO_Button.grid(row=2,column=3)
    AAI_Button = Button(mcp, text='AAI', command=OFF_Mode_Modifier) 
    AAI_Button.grid(row=3,column=1)
    VOO_Button = Button(mcp, text='VOO', command=VOO_Mode_Modifier) 
    VOO_Button.grid(row=3,column=2)
    VVI_Button = Button(mcp, text='VVI', command=VVI_Mode_Modifier) 
    VVI_Button.grid(row=3,column=3)
    AAT_Button = Button(mcp, text='AAT', command=OFF_Mode_Modifier) 
    AAT_Button.grid(row=4,column=1)
    VVT_Button = Button(mcp, text='VVT', command=OFF_Mode_Modifier) 
    VVT_Button.grid(row=4,column=2)
    DDDR_Button = Button(mcp, text='DDDR', command=OFF_Mode_Modifier) 
    DDDR_Button.grid(row=4,column=3)
    AAT_Button = Button(mcp, text='VDDR', command=OFF_Mode_Modifier) 
    AAT_Button.grid(row=5,column=1)
    VVT_Button = Button(mcp, text='DDIR', command=OFF_Mode_Modifier) 
    VVT_Button.grid(row=5,column=2)
    DDDR_Button = Button(mcp, text='DOOR', command=OFF_Mode_Modifier) 
    DDDR_Button.grid(row=5,column=3)
    AOOR_Button = Button(mcp, text='AOOR', command=OFF_Mode_Modifier) 
    AOOR_Button.grid(row=6,column=1)
    AAIR_Button = Button(mcp, text='AAIR', command=OFF_Mode_Modifier) 
    AAIR_Button.grid(row=6,column=2)
    VOOR_Button = Button(mcp, text='VOOR', command=OFF_Mode_Modifier) 
    VOOR_Button.grid(row=6,column=3)
    VVIR_Button = Button(mcp, text='VVIR', command=OFF_Mode_Modifier) 
    VVIR_Button.grid(row=7,column=1)

"""
@brief: System Message Screen shows this Mode is currently not accessible.
@objectL OMM -> OFF_Mode_Modifier Screen
         instruction -> System Message Display
"""

def OFF_Mode_Modifier():
    OMM = Tk();
    OMM.title("System Message");
    instruction  = Label(OMM,text = "\n This Mode is currently not accessible.")
    instruction.pack();

def AOO_Mode_Modifier():


def VOO_Mode_Modifier():


def VVI_Mode_Modifier():
    global p_pacingState
    p_pacingState = 'Permanent'
    global p_pacingMode
    p_pacingMode = 'VVI'
    global p_hysteresis
    p_hysteresis = False
    global p_hysteresisInterval
    p_hysteresisInterval = 300
    global p_lowrateInterval
    p_lowrateInterval = 1000
    global p_vPaceAmp
    p_vPaceAmp = 3500
    global p_vPaceWidth
    p_vPaceWidth = 0.4
    global p_VRP
    p_VRP = 320
    global pp
    VVIModeWindow = Tk()
    VVIModeWindow.title("VVI Mode Modifier")
    VVIModeWindow.geometry("600x500")
    pvL = Label(VVIModeWindow, text = "Programable Variables",fg='blue')
    pvL.grid(row=1,column=0)
    vL = Label(VVIModeWindow, text = "Value",fg='blue')
    vL.grid(row=1,column=1)
    cvL = Label(VVIModeWindow, text = "Current Value",fg='blue')
    cvL.grid(row=1,column=2)
    rtL = Label(VVIModeWindow, text = "Range/Tolerance",fg='blue')
    rtL.grid(row=1,column=3)
    psL = Label(VVIModeWindow, text = "Pacing State")
    psL.grid(row=2,column=0)
    psE = Entry(VVIModeWindow)
    psE.grid(row=2,column=1)
    cvpsL = Label(VVIModeWindow, text = str(p_pacingState))
    cvpsL.grid(row=2,column=2)
    rtpsL = Label(VVIModeWindow, text = "NA")
    rtpsL.grid(row=2,column=3)
    pmL = Label(VVIModeWindow, text = "Pacing Mode")
    pmL.grid(row=3,column=0)
    pmE = Entry(VVIModeWindow)
    pmE.grid(row=3,column=1)
    cvpmL = Label(VVIModeWindow, text = str(p_pacingMode))
    cvpmL.grid(row=3,column=2)
    rtpmL = Label(VVIModeWindow, text = "NA")
    rtpmL.grid(row=3,column=3)
    hsL = Label(VVIModeWindow, text = "Hysteresis Status")
    hsL.grid(row=4,column=0)
    hsE = Entry(VVIModeWindow)
    hsE.grid(row=4,column=1)
    cvhsL = Label(VVIModeWindow, text = "NA")
    cvhsL.grid(row=4,column=2)
    rthsL= Label(VVIModeWindow, text = "True / False")
    rthsL.grid(row=4,column=3)
    hiL = Label(VVIModeWindow, text = "Hysteresis Interval")
    hiL.grid(row=5,column=0)
    hiE = Entry(VVIModeWindow)
    hiE.grid(row=5,column=1)
    cvhiL = Label(VVIModeWindow, text = str(p_hysteresisInterval))
    cvhiL.grid(row=5,column=2)
    rthiL = Label(VVIModeWindow, text = "200~500, +-4")
    rthiL.grid(row=5,column=3)
    lriL = Label(VVIModeWindow, text = "Low Rate Interval")
    lriL.grid(row=6,column=0)
    lriE = Entry(VVIModeWindow)
    lriE.grid(row=6,column=1)
    cvlriL = Label(VVIModeWindow, text = str(p_lowrateInterval))
    cvlriL.grid(row=6,column=2)
    rtlriL = Label(VVIModeWindow, text = "343~2000, +-8")
    rtlriL.grid(row=6,column=3)
    vpaL = Label(VVIModeWindow, text = "Ventricular Pace Amp")
    vpaL.grid(row=7,column=0)
    vpaE = Entry(VVIModeWindow)
    vpaE.grid(row=7,column=1)
    cvvpaL = vpaL = Label(VVIModeWindow, text = str(p_vPaceAmp))
    cvvpaL.grid(row=7,column=2)
    rtvpaL = Label(VVIModeWindow, text = "500~7000, +-12%")
    rtvpaL.grid(row=7,column=3)
    vpwL = Label(VVIModeWindow, text = "Ventricular Pace Width")
    vpwL.grid(row=8,column=0)
    vpwE = Entry(VVIModeWindow)
    vpwE.grid(row=8,column=1)
    cvvpwL = vpwL = Label(VVIModeWindow, text = str(p_vPaceWidth))
    cvvpwL.grid(row=8,column=2)
    rtvpwL = Label(VVIModeWindow, text = "0.1~1.9, 0.2")
    rtvpwL.grid(row=8,column=3)
    vrpL = Label(VVIModeWindow, text = "Ventricular Refrac Period")
    vrpL.grid(row=9,column=0)
    vrpE = Entry(VVIModeWindow)
    vrpE.grid(row=9,column=1)
    cvvrpL = Label(VVIModeWindow, text = str(p_VRP))
    cvvrpL.grid(row=9,column=2)
    rtvvrpL = Label(VVIModeWindow, text = "150~500, +-8")
    rtvvrpL.grid(row=9,column=3)
    spL = Label(VVIModeWindow)
    spL.grid(row=10,columnspan=2)
    Set_Button = Button(VVIModeWindow, text='Set Mode', command=Set_VVI_Values)
    Set_Button.grid(row=11,column=1)

def Set_VVI_Values():
     
    #do it in the future
    
    return 1

Welcome() # The System goes to Welcome Screen everytime the program is executed
