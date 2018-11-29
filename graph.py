import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from struct import *
import serial

ser=serial.Serial(port='COM5', baudrate = 115200, bytesize=8, timeout= None)
#style.use('fivethirtyeight')
style.use('ggplot')

fig = plt.figure()
fig.set_size_inches(11,6)
ax1 = fig.add_subplot(1,1,1)
#ax2 = fig.add_subplot(2,1,2)

x_ax = [] #time
y1_ax = [] #amplitude
y2_ax = []

def animate(i):
    graph_data = ser.read(16)
    y=unpack('dd',graph_data)
    x_ax.append(i*0.002)
    y1_ax.append(y[0])
    y2_ax.append(y[1])
    if len(x_ax)>50:
        del(x_ax[0])
        del(y1_ax[0])
        del(y2_ax[0])

    ax1.clear()
    ax1.plot(x_ax,y1_ax,label='Atrl_Signal')
    ax1.plot(x_ax,y2_ax,label='Vent_Signal')
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Amplitude (mV)')
    ax1.set_ylim(bottom=-2,top=2)
    ax1.set_title('Egram Data Visiualization')
    ax1.legend(loc='upper right')
    print('/n')
    print(y[0])
    print(y[1])


#fig, ax1 = plt.subplots(constrained_layout=True)
ani = animation.FuncAnimation(fig, animate,interval=2)
plt.show()
