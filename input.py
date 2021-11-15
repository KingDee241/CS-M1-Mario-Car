from pynput import keyboard
# import car
# from car.motors import set_steering


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# def get_vertical():
#     input = keyboard.read_key()
#     if input == "W":
#         return 20
#     elif input == "S":
#         return -20
#     else:
#         return 0
#
# def get_horizontal():
#     input = keyboard.read_key()
#     if input == "A":
#         return -0.1
#     elif input == "D":
#         return 0.1
#     else:
#         return 0
