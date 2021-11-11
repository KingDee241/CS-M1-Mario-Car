import input
from car.motors import set_steering

steering = 0

while True:
    steering+=input.get_horizontal()
    set_steering(steering)
    print(steering)
    speed = input.get_vertical()
    print(speed)