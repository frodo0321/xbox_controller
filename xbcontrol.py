import usb
import struct


class XBoxController():
    
    def __init__(self, controller_num=0):
        self.c=None

        controllers=usb.core.find(idVendor=0x045e, idProduct=0x028e)

        if(isinstance(controllers, type(None))):
            print "No controllers found!"
            quit()
        elif(isinstance(controllers, usb.core.Device)):
            print "1 controller found!"
            self.c=controllers
        elif(isinstance(controllers, list)):
            print "%i controllers found!" % (len(controllers))
            self.c=controllers[controller_num]


        try:
            if(self.c.is_kernel_driver_active(0)):
                self.c.detach_kernel_driver(0)
            self.c.set_configuration()
        except:
            
            print "Access is denied.  Please run $ "
            quit()


        self.state=self.c.read(0x81, 32)
        
        self.A=False
        self.B=False
        self.X=False
        self.Y=False
        self.LB=False
        self.RB=False
        self.Guide=False
        self.Back=False
        self.Start=False
        self.LStick=False
        self.RStick=False
        self.DUp=False
        self.DDown=False
        self.DRight=False
        self.DLeft=False

        self.LAnalogX=0
        self.LAnalogY=0
        self.RAnalogX=0
        self.RAnalogY=0

        self.LT=0
        self.RT=0

    def update(self):
        try:
            self.state=self.c.read(0x81, 32)
        except:
            pass
               
        if len(self.state)>4:
            
            self.LT=self.state[4]
            self.RT=self.state[5]

            self.LAnalogX=struct.unpack('h', struct.pack('I', int(format(self.state[7], '#010b') + format(self.state[6], '#010b')[2:], base=2))[0:2])[0]
            self.LAnalogY=struct.unpack('h', struct.pack('I', int(format(self.state[9], '#010b') + format(self.state[8], '#010b')[2:], base=2))[0:2])[0]
            self.RAnalogX=struct.unpack('h', struct.pack('I', int(format(self.state[11], '#010b') + format(self.state[10], '#010b')[2:], base=2))[0:2])[0]
            self.RAnalogY=struct.unpack('h', struct.pack('I', int(format(self.state[13], '#010b') + format(self.state[12], '#010b')[2:], base=2))[0:2])[0]

            self.A=bool(int(format(self.state[3], '#010b')[2:][7-4]))
            self.B=bool(int(format(self.state[3], '#010b')[2:][7-5]))
            self.X=bool(int(format(self.state[3], '#010b')[2:][7-6]))
            self.Y=bool(int(format(self.state[3], '#010b')[2:][7-7]))
            self.LB=bool(int(format(self.state[3], '#010b')[2:][7-0]))
            self.RB=bool(int(format(self.state[3], '#010b')[2:][7-1]))
            self.Guide=bool(int(format(self.state[3], '#010b')[2:][7-2]))
            self.Back=bool(int(format(self.state[2], '#010b')[2:][7-5]))
            self.Start=bool(int(format(self.state[2], '#010b')[2:][7-4]))
            self.LStick=bool(int(format(self.state[2], '#010b')[2:][7-6]))
            self.RStick=bool(int(format(self.state[2], '#010b')[2:][7-7]))
            self.DUp=bool(int(format(self.state[2], '#010b')[2:][7-0]))
            self.DDown=bool(int(format(self.state[2], '#010b')[2:][7-1]))
            self.DRight=bool(int(format(self.state[2], '#010b')[2:][7-3]))
            self.DLeft=bool(int(format(self.state[2], '#010b')[2:][7-2]))

             

    def read_raw(self):
        self.update()
        return self.state

if __name__=='__main__':
    c=XBoxController()
    while(True):
        c.update()
        print c.LT
        print c.RAnalogX


#experimental data:
#
#data[3]
#lbumper = 0
#rbumper = 1
#Guide = 2
#? = 3
#A = 4
#B = 5
#X = 6
#Y = 7
#
#data[2]
#dup = 0
#ddown = 1
#dleft = 2
#dright = 3
#start = 4
#back = 5
#lanalog = 6
#ranalog = 7
#
#data[4] = lt
#data[5] = rt
#data[6] = lanalog x-axis bits 0-3
#data[7] = lanalog x-axis bits 4-7 signed
#data[8] = ranalog y-axis bits 0-3
#data[9] = ranalog y-axis bits 4-7 signed
