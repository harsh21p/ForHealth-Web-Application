from gpiozero import RotaryEncoder
from gpiozero import PWMLED
from gpiozero import LED
from time import sleep

brake= LED(23)
for_rv = LED(18)
motor_brake = LED(11)
vi_pwm = LED(15)
encoder = RotaryEncoder(13, 19, max_steps=0)

def Angle(angle1):

    #Go to Z (Home)

    motor_brake.off()
    brake.on()
    sleep(2)
    brake.off()
    sleep(2)


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

    Angle(angle1)
   
    Range = angle2 - angle1
    rep= rep*2
    while(rep>0):
        Angle(Range)
        rep=rep-1
        Range=Range * (-1)