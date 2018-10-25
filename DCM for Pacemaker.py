#McMaster University Course 3K04 Final Project
#The Device Controller-Monitor (DCM) for pacemacker
#Last Revision: 


from tkinter import *
import os




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
    mcp.geometry("180x290")
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
         
"""
@brief: AOO Mode Control Panel, user can change the value of the parameter for the AOO mode
@object: AOOModeWindow -> The AOO Mode Modifier Screen
         pvl,vl,cvl,rtl -> The Colume Label, stand for Programmable Variable, Value, Tolerance respectively
         LRL,URL,AtrAmp,APW -> The row label, stand for Lower Rate Limit, Upper Rate Limit, Atrial Amplitude, Atrial Pulse Width respectively
         (LRL,URL,AtrAmp,APW)_Input -> The Entry box for Lower Rate Limit, Upper Rate Limit, Atrial Amplitude, Atrial Pulse Width respectively
         (LRL,URL,AtrAmp,APW)_T -> The Tolerance for Lower Rate Limit, Upper Rate Limit, Atrial Amplitude, Atrial Pulse Width respectively
         Set_button -> Set the parameter
@parameter: (LRL,URL,AtrAmp,APW)_Input -> The Result (in String) for Lower Rate Limit, Upper Rate Limit, Atrial Amplitude, Atrial Pulse Width respectively
"""

def AOO_Mode_Modifier():
    global LRL_Input
    global URL_Input
    global AtrAmp_Input
    global APW_Input
    global AOOModeWindow
    
    AOOModeWindow = Tk()
    AOOModeWindow.title("AOO Mode Modifier")
    AOOModeWindow.geometry("600x500")

    pvL = Label(AOOModeWindow, text = "Programable Variables", fg = 'blue')
    pvL.grid(row=1,column=0)

    vL = Label(AOOModeWindow, text = "Value",fg='blue')
    vL.grid(row=1,column=1)

    rtL = Label(AOOModeWindow, text = "Tolerance",fg='blue')
    rtL.grid(row=1,column=2)

    LRL = Label(AOOModeWindow, text = "Lower Rate Limit")
    LRL.grid(row=2,column=0)
    LRL_Input = Entry(AOOModeWindow)
    LRL_Input.grid(row=2,column=1)
    LRL_T = Label(AOOModeWindow, text = "+/-8 ms")
    LRL_T.grid(row=2,column=2)
    
    URL = Label(AOOModeWindow, text = "Upper Rate Limit")
    URL.grid(row=3,column=0)
    URL_Input = Entry(AOOModeWindow)
    URL_Input.grid(row=3,column=1)
    URL_T =Label(AOOModeWindow, text = "+/-8 ms")
    URL_T.grid(row=3,column=2)

    AtrAmp = Label(AOOModeWindow, text = "Atrial Amplitude")
    AtrAmp.grid(row=4,column=0)
    AtrAmp_Input = Entry(AOOModeWindow)
    AtrAmp_Input.grid(row=4,column=1)
    AtrAmp_T = Label(AOOModeWindow, text = "+/-12%")
    AtrAmp_T.grid(row=4,column=2)

    APW = Label(AOOModeWindow, text = "Atrial Pulse Width")
    APW.grid(row=5,column=0)
    APW_Input = Entry(AOOModeWindow)
    APW_Input.grid(row=5,column=1)
    APW_T = Label(AOOModeWindow, text = "0.2 ms")
    APW_T.grid(row=5,column=2)

    Set_button = Button(AOOModeWindow, text = "Set Mode", command=Check_Set_AOO)
    Set_button.grid(row=11,column=1)
         
"""
@Brief: Check the Value of the paramater in AOO Mode that set by User and give out the right result of the parameters
@Object: AOO_Check -> The Screen that display the value of parameter that will sent to the pacemaker
         Display -> "The Parameter List" Label
         (LRL,URL,AtrAmp,APW)_Val -> The values of the parameter check and revised by the system, stand for Lower Rate Limit, Upper Rate Limit, Atrial Amplitude, Atrial Pulse Width respectively
         LRL,URL,AtrAmp,APW -> The Labels for variables, stand for Lower Rate Limit, Upper Rate Limit, Atrial Amplitude, Atrial Pulse Width respectively
         (LRL,URL,AtrAmp,APW)_Output -> Display the result of the variables, stand for Lower Rate Limit, Upper Rate Limit, Atrial Amplitude, Atrial Pulse Width respectively
         Set_button -> Button that lead the User to further procedure
"""

def Check_Set_AOO():
    AOO_Check = Tk()
    AOO_Check.title("System Message")
    
    Display = Label(AOO_Check, text = "The Parameter List")
    Display.grid(row=0,column=0)

    LRL_Val = Check_Change_LRL(int(LRL_Input.get()))
    URL_Val = Check_Change_URL(int(URL_Input.get()),int(LRL_Input.get()))
    AtrAmp_Val = Check_Change_VA_Amp(float(AtrAmp_Input.get()))
    APW_Val = Check_Change_PW(float(APW_Input.get()))

    LRL = Label(AOO_Check, text = "Lower Rate Limit: ")
    LRL.grid(row=1,column=0)
    LRL_Ouput = Label(AOO_Check, text=LRL_Val)
    LRL_Ouput.grid(row=1,column=1)

    URL = Label(AOO_Check, text = "Upper Rate Limit: ")
    URL.grid(row=2,column=0)
    URL_Ouput = Label(AOO_Check, text=URL_Val)
    URL_Ouput.grid(row=2,column=1)

    AtrAmp = Label(AOO_Check, text = "Atrial Amplitude: ")
    AtrAmp.grid(row=3,column=0)
    AtrAmp_Ouput = Label(AOO_Check, text=AtrAmp_Val)
    AtrAmp_Ouput.grid(row=3,column=1)

    APW = Label(AOO_Check, text = "Atrial Pulse Width")
    APW.grid(row=4,column=0)
    APW_Ouput = Label(AOO_Check, text=APW_Val)
    APW_Ouput.grid(row=4,column=1)

    # If one of these parameters is invalid (Checked by Check_Change functions), the Button will lead the User to Modifier Screen. Else, it will lead the user to store the results
    if (LRL_Val == -1) | (URL_Val == -1) | (AtrAmp_Val == -1) | (APW_Val == -1):
        Set_Button = Button(AOO_Check, text = "Go Back", command = AOO_Mode_Modifier)
        Set_Button.grid(row=5,column=0)
    else:
        Set_Button = Button(AOO_Check, text = "Store", command = Store_Data)
        Set_Button.grid(row=5,column=0)

"""
@brief: VOO Mode Control Panel, user can change the value of the parameter for the VOO mode
@object: AOOModeWindow -> The VOO Mode Modifier Screen
         pvl,vl,cvl,rtl -> The Colume Label, stand for Programmable Variable, Value, Tolerance respectively
         LRL,URL,VtrAmp,VPW -> The row label, stand for Lower Rate Limit, Upper Rate Limit, Ventricular Amplitude, Ventricular Pulse Width respectively
         (LRL,URL,VtrAmp,VPW)_Input -> The Entry box for Lower Rate Limit, Upper Rate Limit, Ventricular Amplitude, Ventricular Pulse Width respectively
         (LRL,URL,VtrAmp,VPW)_T -> The Tolerance for Lower Rate Limit, Upper Rate Limit, Ventricular Amplitude, Ventricular Pulse Width respectively
         Set_button -> Set the parameter
@parameter: (LRL,URL,VtrAmp,VPW)_Input -> The Result (in String) for Lower Rate Limit, Upper Rate Limit, Ventricular Amplitude, Ventricular Pulse Width respectively
"""
         
def VOO_Mode_Modifier():
    global LRL_Input
    global URL_Input
    global VtrAmp_Input
    global VPW_Input
    global VOOModeWindow
    VOOModeWindow = Tk()
    VOOModeWindow.title("VOO Mode Modifier")
    VOOModeWindow.geometry("600x500")
    pvL = Label(VOOModeWindow, text = "Programable Variables", fg = 'blue')
    pvL.grid(row=1,column=0)

    vL = Label(VOOModeWindow, text = "Value",fg='blue')
    vL.grid(row=1,column=1)

    rtL = Label(VOOModeWindow, text = "Tolerance",fg='blue')
    rtL.grid(row=1,column=2)

    LRL = Label(VOOModeWindow, text = "Lower Rate Limit")
    LRL.grid(row=2,column=0)
    LRL_Input = Entry(VOOModeWindow)
    LRL_Input.grid(row=2,column=1)
    LRL_T = Label(VOOModeWindow, text = "+/-8 ms")
    LRL_T.grid(row=2,column=2)
    
    URL = Label(VOOModeWindow, text = "Upper Rate Limit")
    URL.grid(row=3,column=0)
    URL_Input = Entry(VOOModeWindow)
    URL_Input.grid(row=3,column=1)
    URL_T =Label(VOOModeWindow, text = "+/-8 ms")
    URL_T.grid(row=3,column=2)

    VtrAmp = Label(VOOModeWindow, text = "Ventricular Amplitude")
    VtrAmp.grid(row=4,column=0)
    VtrAmp_Input = Entry(VOOModeWindow)
    VtrAmp_Input.grid(row=4,column=1)
    VtrAmp_T = Label(VOOModeWindow, text = "+/-12%")
    VtrAmp_T.grid(row=4,column=2)

    VPW = Label(VOOModeWindow, text = "Ventricular Pulse Width")
    VPW.grid(row=5,column=0)
    VPW_Input = Entry(VOOModeWindow)
    VPW_Input.grid(row=5,column=1)
    VPW_T = Label(VOOModeWindow, text = "0.2 ms")
    VPW_T.grid(row=5,column=2)

    Set_button = Button(VOOModeWindow, text = "Set Mode", command=Check_Set_VOO)
    Set_button.grid(row=11,column=1)

"""
@Brief: Check the Value of the paramater in VOO Mode that set by User and give out the right result of the parameters
@Object: VOO_Check -> The Screen that display the value of parameter that will sent to the pacemaker
         Display -> "The Parameter List" Label
         (LRL,URL,VtrAmp,VPW)_Val -> The values of the parameter check and revised by the system, stand for Lower Rate Limit, Upper Rate Limit, Ventricular Amplitude, Ventricular Pulse Width respectively
         LRL,URL,VtrAmp,VPW -> The Labels for variables, stand for Lower Rate Limit, Upper Rate Limit, Ventricular Amplitude, Ventricular Pulse Width respectively
         (LRL,URL,VtrAmp,VPW)_Output -> Display the result of the variables, stand for Lower Rate Limit, Upper Rate Limit, Ventricular Amplitude, Ventricular Pulse Width respectively
         Set_button -> Button that lead the User to further procedure
"""

def Check_Set_VOO():
    
    VOO_Check = Tk()
    VOO_Check.title("System Message")
    
    Display = Label(VOO_Check, text = "The Parameter List")
    Display.grid(row=0,column=0)

    LRL_Val = Check_Change_LRL(int(LRL_Input.get()))
    URL_Val = Check_Change_URL(int(URL_Input.get()),int(LRL_Input.get()))
    VtrAmp_Val = Check_Change_VA_Amp(float(VtrAmp_Input.get()))
    VPW_Val = Check_Change_PW(float(VPW_Input.get()))

    LRL = Label(VOO_Check, text = "Lower Rate Limit: ")
    LRL.grid(row=1,column=0)
    LRL_Ouput = Label(VOO_Check, text=LRL_Val)
    LRL_Ouput.grid(row=1,column=1)

    URL = Label(VOO_Check, text = "Upper Rate Limit: ")
    URL.grid(row=2,column=0)
    URL_Ouput = Label(VOO_Check, text=URL_Val)
    URL_Ouput.grid(row=2,column=1)

    VtrAmp = Label(VOO_Check, text = "Ventricular Amplitude: ")
    VtrAmp.grid(row=3,column=0)
    VtrAmp_Ouput = Label(VOO_Check, text=VtrAmp_Val)
    VtrAmp_Ouput.grid(row=3,column=1)

    VPW = Label(VOO_Check, text = "Ventricular Pulse Width")
    VPW.grid(row=4,column=0)
    VPW_Ouput = Label(VOO_Check, text=VPW_Val)
    VPW_Ouput.grid(row=4,column=1)

     # If one of these parameters is invalid (Checked by Check_Change functions), the Button will lead the User to Modifier Screen. Else, it will lead the user to store the results
         
    if (LRL_Val == -1) | (URL_Val == -1) | (VtrAmp_Val == -1) | (VPW_Val == -1):
        Set_Button = Button(VOO_Check, text = "Go Back", command = VOO_Mode_Modifier)
        Set_Button.grid(row=5,column=0)
    else:
        Set_Button = Button(VOO_Check, text = "Store", command = Store_Data)
        Set_Button.grid(row=5,column=0)
         
         
         
def Store_Data():
    print("Successful Stored!")

def Check_Change_LRL(LRL):
    print(LRL)
    if (LRL>=30) & (LRL<50) :
        if ((LRL-30)%5) ==0 :
            return LRL
        elif ((LRL-30)%5) <3 :
            return LRL-(LRL-30)%5
        else :
            return LRL+(5-(LRL-30)%5)
    elif (LRL>=50) & (LRL<90) :
        return LRL
    elif (LRL>=90) & (LRL<=175) :
        if ((LRL-90)%5) ==0 :
            return LRL
        elif ((LRL-90)%5) <3 :
            return LRL-(LRL-90)%5
        else :
            return LRL+(5-(LRL-90)%5)
    else :
        return -1

def Check_Change_URL(URL,LRL):
    if (URL < LRL):
        return -1
    if (URL>=50) & (URL<=175):
        if (URL-50)%5 ==0 :
            return URL
        elif (URL-50)%5 <3 :
            return URL-(URL-50)%5
        else :
            return URL+(5-(URL-50)%5)
    else:
        return -1

def Check_Change_VA_Amp(Amp):
    if (Amp == 0): return Amp
    if (Amp>=0.5) & (Amp<=3.2):
        temp = round((Amp-3.5)/0.1)
        return round(3.5+temp*0.1,1)
    elif (Amp>=3.5) & (Amp<=7.0):
        temp = round((Amp-3.5)/0.5)
        return round(3.5+temp*0.5,1)
    else:
        return -1

def Check_Change_PW(PW):
    if (PW == 0.05): return PW
    elif (PW>=0.1) & (PW<=1.9) :
        temp = round((Amp-0.1)/0.1)
        return round(0.1+temp*0.1,1)
    else:
        return -1


#def VOO_Mode_Modifier():


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
