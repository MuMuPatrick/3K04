import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from struct import *
import serial
import time,threading



ser=serial.Serial(port='COM6', baudrate = 115200, bytesize=8, timeout= None)
style.use('ggplot')


fig = plt.figure()
fig.set_size_inches(11,6)
ax1 = fig.add_subplot(1,1,1)
#ax2 = fig.add_subplot(2,1,2)

x_ax = [] #time
y1_ax = [] #amplitude
y2_ax = []
xtime=0

def grab_data():
    global xtime
    graph_data = ser.read(24)
    y=unpack('ddd',graph_data)    
    if( abs(y[2])-31 < (1e-6)):
        x_ax.append(xtime*0.005)
        y1_ax.append(y[0])
        y2_ax.append(y[1])
        xtime=xtime+1
        if len(x_ax)>100:
            del(x_ax[0])
            del(y1_ax[0])
            del(y2_ax[0])
    threading.Timer(0.005,grab_data).start() #Timer to call grab_data function every 0.005s



def animate(i):
    ax1.clear()
    ax1.plot(x_ax,y1_ax,label='Atrl_Signal')
    ax1.plot(x_ax,y2_ax,label='Vent_Signal')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Amplitude (mV)')
    ax1.set_ylim(bottom=-2,top=2)
    ax1.set_title('Egram Data Visiualization')
    ax1.legend(loc='upper right')



grab_data()
ani = animation.FuncAnimation(fig, animate,interval=200)
plt.show()

    
    
