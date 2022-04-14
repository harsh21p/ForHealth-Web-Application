from gpiozero import RotaryEncoder
from gpiozero import PWMLED
from gpiozero import LED
from time import sleep



brake= LED(23)
for_rv = LED(18)
motor_brake = LED(11)
vi_pwm = LED(15)
encoder = RotaryEncoder(13, 19, max_steps=0)


BRAKESTATE = True

brake.off()
BRAKESTATE = False
REPITIONS = 0


def Angle(angle1):
    motor_brake.off()
    brake.off()
    BRAKESTATE = False

    #Go to Z (Home
    #Go to angle1
    a1steps =  angle1 * (1024/360)
    i=0
    vi_pwm.on()

    if a1steps>0:
        #clockwise
        for_rv.on()
    else:
        for_rv.off()
   
    encoder.steps=0
   
    while(i==0):
       
        esteps = encoder.steps
        print(esteps)
        if abs(esteps)>=abs(a1steps):
            #find range
            i=1
    vi_pwm.off()


def Repitions(angle1,angle2,rep):
    REPITIONS = rep
    motor_brake.off()
    sleep(1)
    brake.off()
    sleep(0.5)
    BRAKESTATE = False

    Angle(angle1)
   
    Range = angle2 - angle1
    rep= rep*2
    while(rep>0):
        Angle(Range)
        rep=rep-1
        Range=Range * (-1)
        REPITIONS = rep


def Encoder_Angle():
    return(encoder.steps*360/1024)

def Stop_Now():
    vi_pwm.off()
    brake.on()
    BRAKESTATE = True
