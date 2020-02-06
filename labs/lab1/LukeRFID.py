import time, threading, Queue
import RPi.GPIO as GPIO
from time import sleep

D0 = 8
D1 = 10
output = 18
doorSwitch = 16
t = 15
timeout = t
pwm = ''
delay_period = 0.01
idArray = [1415070, 1414970, 9803944]
bits = ''
currentDoorState, pastDoorState, currentLockState, isLock, result = True, False, False, True, ''

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(doorSwitch,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(D0, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(D1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(output, GPIO.OUT)

def set_procname(newname):
    from ctypes import cdll, byref, create_string_buffer
    libc = cdll.LoadLibrary('libc.so.6')    #Loading a 3rd party library C
    buff = create_string_buffer(len(newname)+1) #Note: One larger than the name (man prctl says that)
    buff.value = newname                 #Null terminated string as it should be
    libc.prctl(15, byref(buff), 0, 0, 0) #Refer to "#define" of "/usr/include/linux/prctl.h" for the misterious value 16 & arg[3..5] are zero as the man page says.
    
def one(channel):
    global bits
    global timeout
    bits = bits + '1'
    timeout = t
    
def zero(channel):
    global bits
    global timeout
    bits = bits + '0'
    timeout = t

def setAngle(angle):
    global pwm
    setupServoGPIO()
    duty = angle
    GPIO.output(18, True)
    pwm.ChangeDutyCycle(duty)
    sleep(.5)
    pwm.stop()
    GPIO.output(18, False)
    pwm.stop()
    print('Servo has moved to: %s', angle)
    sleep(3)
    return True

            
def checkDoor():
    isDoorOpen = GPIO.input(doorSwitch)
    return isDoorOpen

def unlockDoor():
    if(setAngle(3))
        return True

def lockDoor():
    if(setAngle(3))
        return True

def RFIDReader():
    set_procname("Wiegand Reader")
    GPIO.add_event_detect(D0, GPIO.FALLING, callback=zero)
    GPIO.add_event_detect(D1, GPIO.FALLING, callback=one)
    global bits, timeout, result
    while 1:
        try:
            if bits:
                timeout = timeout -1
                time.sleep(0.001)
                if len(bits) > 1 and timeout == 0:
                    print (bits)
                    result = int(bits[0:25],2)
                    #resultStr = str(bits[0:25,2])
                    
                    rfid_read = result
                    print (result)
                    
                    if(result in idArray)
                        isLock = False
                        sleep(5)
                        isLock = True
                    
                    bits = '0'
            else:
                time.sleep(0.001)
    
    except KeyboardInterrupt:
        thread.exit()


def main():
#Setting up RFID daemon thread
    RFIDThread = threading.thread(target = RFIDReader, args = ())
    RFIDThread.setDaemon()
    RFIDReader.start()

#State Checker
    while 1:
        global currentDoorState, pastDoorState, currentLockState, isLock
        
        
        currentDoorState = doorCheck() #True means open
        if(currentDoorState): #Door is open
            if(unlockDoor()):
                while doorCheck():
                    sleep(.1)
                currentDoorState = doorCheck()
                currentLockState = False
    
    
        if(!currentDoorState and isLock and !currentLockState): #Door is closed
            if(lockDoor()):
                currentLockState = True
        






        
        







    
    
    

if __name__ == '__main__':
    main()
