from pynput import keyboard
import car

from auto.camera import global_camera
from car.motors import set_throttle, set_steering
from auto.frame_streamer import stream

import music
import threading

key_to_speed = {'w': 20, 's': -20}
key_to_speed_caps = {'w': 30, 's': -30}
key_to_steer = {'a': +45, 'd': -45}
throttle_speed = 0
steering_value = 0

speedy = False
streaming = False

def twitch_tv():
    global streaming
    camera = global_camera()
    print(streaming)
    for frame in camera.stream():
        stream(frame)
        #print(streaming)
        if not streaming:
            print("logged off time to kick a dog")
            stream(None)
            return 

        
def run():
    global throttle_speed, steering_value
    while True:
        set_steering(steering_value)
        set_throttle(throttle_speed)
        
        
x = threading.Thread(target=run)
x.start()     
    

def on_press(key):
    global speedy
    global streaming
    global throttle_speed, steering_value
    
    if key == keyboard.Key.caps_lock:
        speedy = not speedy
    try:
        key_char = key.char.lower()
    except:
        return
    if key_char == 'm':
        x = threading.Thread(target=music.coconut_mall)
        x.start()
    if key_char == 'i':
        x = threading.Thread(target=music.ice_cream_man)
        x.start()
    if key_char == 'c':
        if not streaming:
            streaming = True
            z = threading.Thread(target=twitch_tv)
            z.start()
            #print(streaming)
        else:
            streaming = False
            #print(streaming) 
    speed_dict = key_to_speed
    if speedy:
        speed_dict = key_to_speed_caps
    if key_char in key_to_speed:
        throttle_speed = speed_dict[key_char]
    elif key_char in key_to_steer:
        steering_value = key_to_steer[key_char]
    elif key_char == 't':
        car.print(input())

        
def on_release(key):
    global throttle_speed, steering_value
    try:
        key_char = key.char.lower()
    except:
        return
    
        
    if key_char in key_to_speed:
        throttle_speed = 0
    if key_char in key_to_steer:
        steering_value = 0
    if key == keyboard.Key.esc:
        # Stop listener
        return False

    
# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
