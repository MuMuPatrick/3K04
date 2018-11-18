from tkinter import *

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

   
"""
@brief:Store the value of the parameter in a specific file. This object will be used in further assignment
"""
         
def Store_Data():
    print("Successful Stored!")


