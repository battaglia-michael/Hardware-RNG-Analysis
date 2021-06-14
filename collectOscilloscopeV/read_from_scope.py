import visa
import numpy as np
import time

#rm = visa.ResourceManager()

class Scope:
    def __init__(self,address,rm = visa.ResourceManager()): 
        self.device = rm.open_resource(address,timeout=5000)
        # self.device.query_delay = 0.1    # ms
        self.id = self.device.query("*idn?")
        self.device.write(":WAV:FORM ASC")
        self.device.write('DATA:WIDTH 1')
        self.device.write('DATA:STOP 2500')
        self.device.write('ACQUIRE:MODE:SAMPLE')        
        self.device.write('DATA:ENCDG RIBINARY')


    def get_trace(self,channelNumber=1,verbose=False):
        self.device.write('DATA:SOURCE CH' + `channelNumber`)
        ymult = float(self.device.query("WFMPRE:CH"+`channelNumber`+":YMULT?"))
        yoff = float(self.device.query("WFMPRE:CH"+`channelNumber`+":YOFF?"))
        yzero = float(self.device.query("WFMPRE:CH"+`channelNumber`+":YZERO?"))
        
        if verbose: 
            print "y offset = ", yoff, "y multiplication factor = ", ymult
        
        
        values = self.device.query_binary_values('CURVE?',datatype='b', is_big_endian=False)
        voltages = [(float(v)-yoff)*ymult + yzero for v in values]
        t0 = float(self.device.query('WFMPRE:Xzero?'))
        dt = float(self.device.query('WFMPRE:XINCR?'))
        t = [t0 + i*dt for i in range(len(voltages))]
        
        return t, voltages

    
    def close(self):
        self.device.write("SAVE:SETUP")
        self.device.close()

if __name__ == '__main__':
    scope = Scope('COM5')
    print scope.device.query("*idn?")
    
    print "Press Ctrl+C to exit"
    print
    
    try:		
        while True:
            channel = raw_input("Enter channel number: ")
            file_number = raw_input("Enter file number: ")
            comments = raw_input("Enter comments for header: ")	
        
            #time.sleep(2)
            #print scope.get_trace()
            #time.sleep(2)
            
            filename = "C:\\Users\\student\\Desktop\\trace" + file_number + ".txt"
            f = open(filename,'w')
            f.write("# " + comments + "\n")
            f.write("# time [s]	\t	voltage [V] \n")
            f.close()
            
            f = open(filename,'a')
            np.savetxt(f,np.transpose(scope.get_trace(channelNumber=int(channel))))
            f.close()	
            print "File saved as", filename
            print
            print
    
    except KeyboardInterrupt:
        print
        print "Closing connection to scope ..", 		
        scope.close()
        time.sleep(2)
        print ". done. Bye"


##### Example of usage in another program  ######

## (first download scope_serial.py from the course webpage and put it in the same directory as your program)

#import scope_serial
#scope = scope.Scope('COM5')
#print 'Aquiring Trace...'
#(times, voltages) = scope.get_trace(1)
#print 'Done.'
