from pynput import keyboard
import car
from car.motors import set_throttle, set_steering

key_to_speed = {'w': 20, 's': 20}
key_to_steer = {'a': 45, 'd': -45}

def on_press(key):
    if key.char in key_to_speed:
        car.set_throttle(key_to_speed[key.char])
    if key.char in key_to_steer:
        car.set_steering(key_to_steer[key.char])
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key.char in key_to_speed:
        car.set_throttle(0)
    if key.char in key_to_steer:
        car.set_steering(0)
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
   
