from tkinter import *
from tkinter import messagebox
from Check_Para import *
import os
import serial
from serial.tools import List_ports

global ParaList
creds2 = 'Parameter List.txt' # text file to store the Parameter List  

#Value that will sent to the Pacemaker
global LRL_Val
global URL_Val
global AtrAmp_Val
global APW_Val
global VtrAmp_Val
global VPW_Val
global VtrSen_Val
global AtrSen_Val
global ARP_Val
global VRP_Val
global PVARP_Val
global Hysteresis_Val
global RateSmoothing_Val



def connect():
    port = list_ports.comports()
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = port[0]
    ser.timeout = None
    ser.open()
    if ser.is_open:
        messagebox.showinfo("System Message", "The Device is connected")
    else:
        messagebox.showerror("System Message", "The Device is not connected")

"""
@brief: System Message Screen shows this Mode is currently not accessible.
@objectL OMM -> OFF_Mode_Modifier Screen
         instruction -> System Message Display
"""

def OFF_Mode_Modifier():
    OMM = Tk()
    OMM.title("System Message");
    instruction  = Label(OMM,text = "\n This Mode is currently not accessible.")
    instruction.pack()


# Initialize the ParaList
def List_Init():
    global ParaList
    ParaList = [0] * 11

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
    global LRL_Val
    global URL_Val
    global AtrAmp_Val
    global APW_Val
    global ParaList
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
        List_Init()
        ParaList[0]=16
        ParaList[1]=55
        Set_Button = Button(AOO_Check, text = "Store", command = Store_AOO)
        Set_Button.grid(row=5,column=0)
        Pass = Button(AOO_Check, text = "Pass to Pacemaker", command = Pass_Val)
        Pass.grid(row=5,column=1)

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
    global LRL_Val
    global URL_Val
    global VtrAmp_Val
    global VPW_Val
    
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
        Set_Button = Button(VOO_Check, text = "Store", command = Store_VOO)
        Set_Button.grid(row=5,column=0)

         
def AAI_Mode_Modifier():
    global LRL_Input
    global URL_Input
    global AtrAmp_Input
    global APW_Input
    global AtrSen_Input
    global ARP_Input
    global PVARP_Input
    global Hysteresis_Input
    global RateSmoothing_Input
    
    AAIModeWindow = Tk()
    AAIModeWindow.title("AAI Mode Modifier")
    AAIModeWindow.geometry("600x500")

    pvL = Label(AAIModeWindow, text = "Programable Variables", fg = 'blue')
    pvL.grid(row=1,column=0)
    vL = Label(AAIModeWindow, text = "Value",fg='blue')
    vL.grid(row=1,column=1)
    rtL = Label(AAIModeWindow, text = "Tolerance",fg='blue')
    rtL.grid(row=1,column=2)

    LRL = Label(AAIModeWindow, text = "Lower Rate Limit")
    LRL.grid(row=2,column=0)
    LRL_Input = Entry(AAIModeWindow)
    LRL_Input.grid(row=2,column=1)
    LRL_T = Label(AAIModeWindow, text = "+/- 8 ms")
    LRL_T.grid(row=2,column=2)
    
    URL = Label(AAIModeWindow, text = "Upper Rate Limit")
    URL.grid(row=3,column=0)
    URL_Input = Entry(AAIModeWindow)
    URL_Input.grid(row=3,column=1)
    URL_T =Label(AAIModeWindow, text = "+/- 8 ms")
    URL_T.grid(row=3,column=2)

    AtrAmp = Label(AAIModeWindow, text = "Atrial Amplitude")
    AtrAmp.grid(row=4,column=0)
    AtrAmp_Input = Entry(AAIModeWindow)
    AtrAmp_Input.grid(row=4,column=1)
    AtrAmp_T = Label(AAIModeWindow, text = "+/- 12%")
    AtrAmp_T.grid(row=4,column=2)

    APW = Label(AAIModeWindow, text = "Atrial Pulse Width")
    APW.grid(row=5,column=0)
    APW_Input = Entry(AAIModeWindow)
    APW_Input.grid(row=5,column=1)
    APW_T = Label(AAIModeWindow, text = "0.2 ms")
    APW_T.grid(row=5,column=2)

    AtrSen = Label(AAIModeWindow, text = "Atrial Sensitivity")
    AtrSen.grid(row=6,column=0)
    AtrSen_Input = Entry(AAIModeWindow)
    AtrSen_Input.grid(row=6,column=1)
    AtrSen_T = Label(AAIModeWindow, text = "+/- 2%")
    AtrSen_T.grid(row=6,column=2)

    ARP = Label(AAIModeWindow, text = "Atrial Refractory Period")
    ARP.grid(row=7,column=0)
    ARP_Input = Entry(AAIModeWindow)
    ARP_Input.grid(row=7,column=1)
    ARP_T = Label(AAIModeWindow, text = "+/- 8 ms")
    ARP_T.grid(row=7,column=2)

    PVARP = Label(AAIModeWindow, text = "PVARP")
    PVARP.grid(row=8,column=0)
    PVARP_Input = Entry(AAIModeWindow)
    PVARP_Input.grid(row=8,column=1)
    PVARP_T = Label(AAIModeWindow, text = "+/- 8 ms")
    PVARP_T.grid(row=8,column=2)

    Hysteresis = Label(AAIModeWindow, text = "Hysteresis")
    Hysteresis.grid(row=9,column=0)
    Hysteresis_Input = Entry(AAIModeWindow)
    Hysteresis_Input.grid(row=9,column=1)
    Hysteresis_T = Label(AAIModeWindow, text = "+/- 8 ms")
    Hysteresis_T.grid(row=9,column=2)

    RateSmoothing = Label(AAIModeWindow, text = "Rate Smoothing(%)")
    RateSmoothing.grid(row=10,column=0)
    RateSmoothing_Input = Entry(AAIModeWindow)
    RateSmoothing_Input.grid(row=10,column=1)
    RateSmoothing_T = Label(AAIModeWindow, text = "+/- 1%")
    RateSmoothing_T.grid(row=10,column=2)

    Set_button = Button(AAIModeWindow, text = "Set Mode", command=Check_Set_AAI)
    Set_button.grid(row=16,column=1)

def Check_Set_AAI():
    global LRL_Val
    global URL_Val
    global AtrAmp_Val
    global APW_Val
    global AtrSen_Val
    global ARP_Val
    global PVARP_Val
    global Hysteresis_Val
    global RateSmoothing_Val
    
    AAI_Check = Tk()
    AAI_Check.title("System Message")
    
    Display = Label(AAI_Check, text = "The Parameter List")
    Display.grid(row=0,column=0)

    LRL_Val = Check_Change_LRL(int(LRL_Input.get()))
    URL_Val = Check_Change_URL(int(URL_Input.get()),int(LRL_Input.get()))
    AtrAmp_Val = Check_Change_VA_Amp(float(AtrAmp_Input.get()))
    APW_Val = Check_Change_PW(float(APW_Input.get()))
    AtrSen_Val = Check_Change_AVSen(float(AtrSen_Input.get()))
    ARP_Val = Check_Change_AVRP(int(ARP_Input.get()))
    PVARP_Val = Check_Change_AVRP(int(PVARP_Input.get()))
    Hysteresis_Val = Check_Change_LRL(int(Hysteresis_Input.get()))
    RateSmoothing_Val = Check_Change_RS(int(RateSmoothing_Input.get()))
    
    LRL = Label(AAI_Check, text = "Lower Rate Limit: ")
    LRL.grid(row=1,column=0)
    LRL_Ouput = Label(AAI_Check, text=LRL_Val)
    LRL_Ouput.grid(row=1,column=1)

    URL = Label(AAI_Check, text = "Upper Rate Limit: ")
    URL.grid(row=2,column=0)
    URL_Ouput = Label(AAI_Check, text=URL_Val)
    URL_Ouput.grid(row=2,column=1)

    AtrAmp = Label(AAI_Check, text = "Atrial Amplitude: ")
    AtrAmp.grid(row=3,column=0)
    AtrAmp_Ouput = Label(AAI_Check, text=AtrAmp_Val)
    AtrAmp_Ouput.grid(row=3,column=1)

    APW = Label(AAI_Check, text = "Atrial Pulse Width: ")
    APW.grid(row=4,column=0)
    APW_Ouput = Label(AAI_Check, text=APW_Val)
    APW_Ouput.grid(row=4,column=1)

    AtrSen = Label(AAI_Check, text = "Atrial Sensitivity: ")
    AtrSen.grid(row=5,column=0)
    AtrSen_Output = Label(AAI_Check, text=AtrSen_Val)
    AtrSen_Output.grid(row=5,column=1)

    ARP = Label(AAI_Check, text = "Atrial Refractory Period: ")
    ARP.grid(row=6,column=0)
    ARP_Output = Label(AAI_Check, text=ARP_Val)
    ARP_Output.grid(row=6,column=1)

    PVARP = Label(AAI_Check, text = "PVARP: ")
    PVARP.grid(row=7,column=0)
    PVARP_Output = Label(AAI_Check, text=PVARP_Val)
    PVARP_Output.grid(row=7,column=1)
    
    Hys = Label(AAI_Check, text = "Hysteresis: ")
    Hys.grid(row=8,column=0)
    Hys_Output = Label(AAI_Check, text=Hysteresis_Val)
    Hys_Output.grid(row=8,column=1)
    
    RS = Label(AAI_Check, text = "Rate Smoothing(%): ")
    RS.grid(row=9,column=0)
    RS_Output = Label(AAI_Check, text=RateSmoothing_Val)
    RS_Output.grid(row=9,column=1)
         
    if (LRL_Val==-1) | (URL_Val==-1) | (AtrAmp_Val==-1) | (APW_Val==-1) | (AtrSen_Val==-1) | (ARP_Val==-1) | (PVARP_Val==-1) | (Hysteresis_Val==-1) | (RateSmoothing_Val==-1) :
        Set_Button = Button(AAI_Check, text = "Go Back", command = AAI_Mode_Modifier)
        Set_Button.grid(row=10,column=0)
    else:
        Set_Button = Button(AAI_Check, text = "Store", command = Store_AAI)
        Set_Button.grid(row=10,column=0)

def VVI_Mode_Modifier():
    global LRL_Input
    global URL_Input
    global VtrAmp_Input
    global VPW_Input
    global VtrSen_Input
    global VRP_Input
    global Hysteresis_Input
    global RateSmoothing_Input

    VVIModeWindow = Tk()
    VVIModeWindow.title("VVI Mode Modifier")
    VVIModeWindow.geometry("600x500")

    pvL = Label(VVIModeWindow, text = "Programable Variables", fg = 'blue')
    pvL.grid(row=1,column=0)

    vL = Label(VVIModeWindow, text = "Value",fg='blue')
    vL.grid(row=1,column=1)

    rtL = Label(VVIModeWindow, text = "Tolerance",fg='blue')
    rtL.grid(row=1,column=2)

    LRL = Label(VVIModeWindow, text = "Lower Rate Limit")
    LRL.grid(row=2,column=0)
    LRL_Input = Entry(VVIModeWindow)
    LRL_Input.grid(row=2,column=1)
    LRL_T = Label(VVIModeWindow, text = "+/-8 ms")
    LRL_T.grid(row=2,column=2)
    
    URL = Label(VVIModeWindow, text = "Upper Rate Limit")
    URL.grid(row=3,column=0)
    URL_Input = Entry(VVIModeWindow)
    URL_Input.grid(row=3,column=1)
    URL_T =Label(VVIModeWindow, text = "+/-8 ms")
    URL_T.grid(row=3,column=2)

    VtrAmp = Label(VVIModeWindow, text = "Ventricular Amplitude")
    VtrAmp.grid(row=4,column=0)
    VtrAmp_Input = Entry(VVIModeWindow)
    VtrAmp_Input.grid(row=4,column=1)
    VtrAmp_T = Label(VVIModeWindow, text = "+/-12%")
    VtrAmp_T.grid(row=4,column=2)

    VPW = Label(VVIModeWindow, text = "Ventricular Pulse Width")
    VPW.grid(row=5,column=0)
    VPW_Input = Entry(VVIModeWindow)
    VPW_Input.grid(row=5,column=1)
    VPW_T = Label(VVIModeWindow, text = "0.2 ms")
    VPW_T.grid(row=5,column=2)

    VtrSen = Label(VVIModeWindow, text = "Ventricular Sensitivity")
    VtrSen.grid(row=6,column=0)
    VtrSen_Input = Entry(VVIModeWindow)
    VtrSen_Input.grid(row=6,column=1)
    VtrSen_T = Label(VVIModeWindow, text = "+/-20%")
    VtrSen_T.grid(row=6,column=2)

    VRP = Label(VVIModeWindow, text = "Ventricular Refractory Period")
    VRP.grid(row=7,column=0)
    VRP_Input = Entry(VVIModeWindow)
    VRP_Input.grid(row=7,column=1)
    VRP_T = Label(VVIModeWindow, text = "+/-8 ms")
    VRP_T.grid(row=7,column=2)

    HYS= Label(VVIModeWindow, text = "Hysteresis Rate Limit")
    HYS.grid(row=8,column=0)
    Hysteresis_Input = Entry(VVIModeWindow)
    Hysteresis_Input.grid(row=8,column=1)
    HYS_T = Label(VVIModeWindow, text = "+/-8 ms")
    HYS_T.grid(row=8,column=2)

    RSM = Label(VVIModeWindow, text = "Rate Smoothing")
    RSM.grid(row=9,column=0)
    RateSmoothing_Input = Entry(VVIModeWindow)
    RateSmoothing_Input.grid(row=9,column=1)
    RSM_T = Label(VVIModeWindow, text = "+/-1%")
    RSM_T.grid(row=9,column=2)

    Set_button = Button(VVIModeWindow, text = "Set Mode", command=Check_Set_VVI)
    Set_button.grid(row=11,column=1)

def Check_Set_VVI():
    global LRL_Val
    global URL_Val
    global VtrAmp_Val
    global VPW_Val
    global VtrSen_Val
    global VRP_Val
    global Hysteresis_Val
    global RateSmoothing_Val
    VVI_Check=Tk()
    VVI_Check.title("System Message")

    Display = Label(VVI_Check, text = "The Parameter List")
    Display.grid(row=0,column=0)

    LRL_Val = Check_Change_LRL(int(LRL_Input.get()))
    URL_Val = Check_Change_URL(int(URL_Input.get()),int(LRL_Input.get()))
    VtrAmp_Val = Check_Change_VA_Amp(float(VtrAmp_Input.get()))
    VPW_Val = Check_Change_PW(float(VPW_Input.get()))
    VtrSen_Val = Check_Change_AVSen(float(VtrSen_Input.get()))
    VRP_Val = Check_Change_AVRP(int(VRP_Input.get()))
    Hysteresis_Val = Check_Change_LRL(int(Hysteresis_Input.get())) #same choices as LRL
    RateSmoothing_Val = Check_Change_RS(int(RateSmoothing_Input.get()))
    
    LRL = Label(VVI_Check, text = "Lower Rate Limit: ")
    LRL.grid(row=1,column=0)
    LRL_Ouput = Label(VVI_Check, text=LRL_Val)
    LRL_Ouput.grid(row=1,column=1)

    URL = Label(VVI_Check, text = "Upper Rate Limit: ")
    URL.grid(row=2,column=0)
    URL_Ouput = Label(VVI_Check, text=URL_Val)
    URL_Ouput.grid(row=2,column=1)

    VEN = Label(VVI_Check, text = "Ventricular Amplitude Limit: ")
    VEN.grid(row=3,column=0)
    VEN_Output = Label(VVI_Check, text=VtrAmp_Val)
    VEN_Output.grid(row=3,column=1)

    VPW = Label(VVI_Check, text = "Ventricular Pulse Width Limit: ")
    VPW.grid(row=4,column=0)
    VPW_Output = Label(VVI_Check, text=VPW_Val)
    VPW_Output.grid(row=4,column=1)

    VSEN = Label(VVI_Check, text = "Ventricular Sensitivity Limit: ")
    VSEN.grid(row=5,column=0)
    VSEN_Output = Label(VVI_Check, text=VtrSen_Val)
    VSEN_Output.grid(row=5,column=1)
    
    VRP = Label(VVI_Check, text = "Ventricular Refractory Period Limit: ")
    VRP.grid(row=6,column=0)
    VRP_Output = Label(VVI_Check, text=VRP_Val)
    VRP_Output.grid(row=6,column=1)

    HYS = Label(VVI_Check, text = "Hysteresis Rate Limit: ")
    HYS.grid(row=7,column=0)
    HYS_Output = Label(VVI_Check, text=Hysteresis_Val)
    HYS_Output.grid(row=7,column=1)

    RSM = Label(VVI_Check, text = "Ventricular Amplitude Limit: ")
    RSM.grid(row=8,column=0)
    RSM_Output = Label(VVI_Check, text=RateSmoothing_Val)
    RSM_Output.grid(row=8,column=1)

    if (LRL_Val == -1) | (URL_Val == -1) | (VtrAmp_Val == -1) | (VPW_Val == -1) | (VtrSen_Val == -1) | (VRP_Val == -1) | (Hysteresis_Val == -1) | (RateSmoothing_Val == -1):
        Set_Button = Button(VVI_Check, text = "Go Back", command = VVI_Mode_Modifier)
        Set_Button.grid(row=9,column=0)
    else:
        Set_Button = Button(VVI_Check, text = "Store", command = Store_VVI)
        Set_Button.grid(row=9,column=0)  
   
"""
@brief:Store the value of the parameter in a specific file. This object will be used in further assignment
"""
         
def Store_AOO():
    global LRL_Val
    global URL_Val
    global AtrAmp_Val
    global APW_Val
    global ParaList
    ParaList[2] = LRL_Val
    ParaList[3] = URL_Val
    ParaList[4] = int (AtrAmp_Val*20)
    ParaList[5] = int (APW_Val*10)
    ParaList[6] = 21
    f = open(creds2,'w')
    for para in ParaList:
        f.write(str(para))
        f.write('\n')
    f.close()

def Store_VOO():
    global ParaList
    global LRL_Val
    global URL_Val
    global VtrAmp_Val
    global VPW_Val
    ParaList[2] = LRL_Val
    ParaList[3] = URL_Val
    ParaList[4] = VtrAmp_Val
    ParaList[5] = VPW_Val
    f = open(creds2,'w')
    for para in ParaList:
        f.write(str(para))
        f.write('\n')
    f.close()

def Store_AAI():
    global LRL_Val
    global URL_Val
    global AtrAmp_Val
    global APW_Val
    global AtrSen_Val
    global ARP_Val
    global PVARP_Val
    global Hysteresis_Val
    global RateSmoothing_Val
    ParaList[0] = LRL_Val
    ParaList[1] = URL_Val
    ParaList[7] = AtrAmp_Val
    ParaList[9] = APW_Val
    ParaList[10] = AtrSen_Val
    ParaList[12] = ARP_Val
    ParaList[13] = PVARP_Val
    ParaList[15] = Hysteresis_Val
    ParaList[16] = RateSmoothing_Val
    f = open(creds2,'w')
    for para in ParaList:
        f.write(str(para))
        f.write('\n')
    f.close()

def Store_VVI():
    global LRL_Val
    global URL_Val
    global VtrAmp_Val
    global VPW_Val
    global VtrSen_Val
    global VRP_Val
    global Hysteresis_Val
    global RateSmoothing_Val
    ParaList[0] = LRL_Val
    ParaList[1] = URL_Val
    ParaList[7] = VtrAmp_Val
    ParaList[9] = VPW_Val
    ParaList[10] = VtrSen_Val
    ParaList[11] = VRP_Val
    ParaList[15] = Hysteresis_Val
    ParaList[16] = RateSmoothing_Val
    f = open(creds2,'w')
    for para in ParaList:
        f.write(str(para))
        f.write('\n')
    f.close()
    
def Pass_Val:
    global ParaList
    s.write(ParaList)
