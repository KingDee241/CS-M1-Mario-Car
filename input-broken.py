import keyboard
# import car
# from car.motors import set_steering

def get_vertical():
    input = keyboard.read_key()
    if input == "W":
        return 20
    elif input == "S":
        return -20
    else:
        return 0

def get_horizontal():
    input = keyboard.read_key()
    if input == "A":
        return -0.1
    elif input == "D":
        return 0.1
    else:
        return 0
