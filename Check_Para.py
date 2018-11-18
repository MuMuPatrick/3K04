"""
@brief: Check the correctness of the value of LRL. If this is a invaild input, system will change the value into the nearest vaild value.
@para: LRL -> the value of LRL read from the User's input
@Note: The system will find out which region the value is in and change the value based on the increments given in the manual
       If the input in not in these three regions, a -1 will be returned.
"""

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

"""
@brief: Check the correctness of the value of URL. If this is a invaild input, system will change the value into the nearest vaild value.
@para: URL -> the value of URL read from the User's input
       LRL -> the value of LRL read from the User's input
@Note: The system will find out which region the value is in and change the value based on the increments given in the manual
       If the input in not in the regions, a -1 will be returned.
       If URL is small than the LRL (It cannot happen in real life), a -1 will also be returned
"""

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

"""
@brief: Check the correctness of the value of amplitude. If this is a invaild input, system will change the value into the biggest vaild value that smaller than the input
@para: Amp -> the value of amplitude read from the User's input
@Note: The system will find out which region the value is in and change the value based on the increments given in the manual
       If the input in not in these regions, a -1 will be returned.
"""

def Check_Change_VA_Amp(Amp):
    if (Amp == 0): return Amp
    if (Amp >= 0.5) & (Amp<=3.2):
        temp = round((Amp-3.5)/0.1)
        return round(3.5+temp*0.1,1)
    elif (Amp>=3.5) & (Amp<=7.0):
        temp = round((Amp-3.5)/0.5)
        return round(3.5+temp*0.5,1)
    else:
        return -1

"""
@brief: Check the correctness of the value of pulse width. If this is a invaild input, system will change the value into the biggest vaild value that smaller than the input
@para: PW -> the value of pulse width read from the User's input
@Note: The system will find out which region the value is in and change the value based on the increments given in the manual
       If the input in not in these regions, a -1 will be returned.
"""


def Check_Change_PW(PW):
    if (PW == 0.05): return PW
    elif (PW>=0.1) & (PW<=1.9) :
        temp = round((PW-0.1)/0.1)
        return round(0.1+temp*0.1,1)
    else:
        return -1

def Check_Change_AVSen(S):
    if (S == 0.25): return S
    if (S == 0.5): return S
    if (S == 0.75): return S
    elif (S>=1.0) & (S<=10.0):
        temp = round((S-1.0)/0.5)
        return round(1.0+temp*0.5,1)
    else:
        return -1

def Check_Change_AVRP(RP):
    if (RP>=150) & (RP<=500):
        temp = round((RP-150)/10)
        return round(150+temp*10,1)
    else:
        return -1

def Check_Change_RS(RS):
    if (RS==3):return RS
    if (RS==6):return RS
    if (RS==9):return RS
    if (RS==12):return RS
    if (RS==15):return RS
    if (RS==18):return RS
    if (RS==21):return RS
    if (RS==25):return RS
    else:
        return -1
