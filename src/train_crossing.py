#!/usr/bin/env python3
from buildhat import PassiveMotor,MotionSensor,Hat
import sys
from enum import Enum
import time
time.sleep(2)
class CrossingState(Enum):
    LOWERING=1
    LOWERED=2
    RAISING=3
    RAISED=4
counter = 0
started = False
while(counter < 10):
    if started == True:
        break
    try:
        hat = Hat()
        print(hat.get())
        started = True
    except Exception as e:
        print(e)
    counter = counter + 1
    time.sleep(1)
if started == False:
    print("Couldn't Start.  Exiting")
    sys.exit()

motion = MotionSensor('A')
motor1 = PassiveMotor('B')
motor2 = PassiveMotor('C')
DISTANCE_THRESHOLD = 5
LOWERING_TIME = 2.0
RAISING_TIME = 2.0
LOWERED_TIME = 5.0
RAISE_SPEED = 50
LOWER_SPEED = -50
dT = 0.1
timer = 0.0
state = CrossingState.RAISED

motor1.start(RAISE_SPEED)
motor2.start(RAISE_SPEED)
time.sleep(RAISING_TIME)
motor1.stop()
motor2.stop()
while(True):
    time.sleep(dT)
    print(state)
    if(state == CrossingState.RAISED):
        dist = motion.get_distance()
        if(dist <= DISTANCE_THRESHOLD):
            state = CrossingState.LOWERING
            motor1.start(LOWER_SPEED)
            motor2.start(LOWER_SPEED)
    elif(state == CrossingState.LOWERING):
        timer += dT
        if(timer >= LOWERING_TIME):
            timer = 0.0
            motor1.stop()
            motor2.stop()
            state = CrossingState.LOWERED
    elif(state == CrossingState.LOWERED):
        timer += dT
        if(timer >= LOWERED_TIME):
            timer = 0.0
            motor1.start(RAISE_SPEED)
            motor2.start(RAISE_SPEED)
            state = CrossingState.RAISING
    elif(state == CrossingState.RAISING):
        timer += dT
        if(timer >= RAISING_TIME):
            timer = 0.0
            motor1.stop()
            motor2.stop()
            state = CrossingState.RAISED