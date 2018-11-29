import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from struct import *
import serial

ser=serial.Serial(port='COM5', baudrate = 115200, bytesize=8, timeout= None)
style.use('fivethirtyeight')

fig = plt.figure()
fig.set_size_inches(11,6)
#ax1 = fig.add_subplot(1,1,1)
#ax2 = fig.add_subplot(2,1,2)

x_ax = [] #time
y1_ax = [] #amplitude
y2_ax = []
i=1

while(True):
    graph_data = ser.read(16)
    y=unpack('dd',graph_data)
    x_ax.append(i*0.01)
    y1_ax.append(y[0])
    y2_ax.append(y[1])
    if len(x_ax)>50:
        del(x_ax[0])
        del(y1_ax[0])
        del(y2_ax[0])

    plt.close()
    plt.plot(x_ax,y1_ax,label='Atrl_Signal')
    plt.plot(x_ax,y2_ax,label='Vent_Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (mV)')
    plt.ylim(bottom=-7,top=7)
    plt.title('Egram Data Visiualization')
    plt.legend(loc='upper right')
    print('/n')
    print(y[0])
    print(y[1])

    plt.pause(0.01)
    plt.show()    
    i=i+1
    
#fig, ax1 = plt.subplots(constrained_layout=True)
#ani = animation.FuncAnimation(fig, animate, interval=200)

