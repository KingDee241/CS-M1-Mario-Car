from pynput import keyboard
import car
from car.motors import set_throttle, set_steering

key_to_speed = {'w': 20, 's': -20}
key_to_speed_caps = {'w': 40, 's': -40}
key_to_steer = {'a': +45, 'd': -45}

def on_press(key):
    try:
        key_char = key.char.lower()
    except:
        return
    speed_dict = key_to_speed
    if keyboard.Controller.shift_pressed:
        speed_dict = key_to_speed_caps
    
    if key_char in key_to_speed:
        set_throttle(speed_dict[key_char])
    elif key_char in key_to_steer:
        set_steering(key_to_steer[key_char])
    elif key_char == 't':
        car.print(input())
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    try:
        key.char
    except:
        return
    if key.char in key_to_speed:
        set_throttle(0)
    if key.char in key_to_steer:
        set_steering(0)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
   
