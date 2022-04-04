"""

Note password is defult

"""
def convert_type(input2: number, result: number):
    global _1, _2, _3, _4, _5, _6, _7
    if not (result == 1):
        _1 = input2
    if not (result == 2):
        _2 = input2
    if not (result == 3):
        _3 = input2
    if not (result == 4):
        _4 = input2
    if not (result == 5):
        _5 = input2
    if not (result == 6):
        _6 = input2
    else:
        _7 = input2

def on_button_pressed_a():
    global started, expired
    if 1 == started:
        convert_type(get_var_name(), 1)
    else:
        started = 1
        basic.show_string("Hello!")
        basic.show_string("Password Please")
        expired = 15
input.on_button_pressed(Button.A, on_button_pressed_a)

def get_var_name():
    if not (_1 == 0):
        return 1
    elif not (_2 == 0):
        return 2
    elif not (_3 == 0):
        return 3
    elif not (_4 == 0):
        return 4
    elif not (_5 == 0):
        return 5
    elif not (_6 == 0):
        return 6
    else:
        return 7

def on_button_pressed_ab():
    if 1 == started:
        convert_type(get_var_name(), 3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if 1 == started:
        convert_type(get_var_name(), 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def reset(all_turefalse: bool):
    global _1, _2, _3, _4, _5, _6, _7
    if all_turefalse == True:
        _1 = 0
        _2 = 0
        _3 = 0
        _4 = 0
        _5 = 0
        _6 = 0
        _7 = 0
expired = 0
_7 = 0
_6 = 0
_5 = 0
_4 = 0
_3 = 0
_2 = 0
_1 = 0
started = 0
started = 0

def on_forever():
    global expired
    while not (expired == 0):
        basic.pause(1000)
        expired += -1
        if expired == 0:
            reset(True)
basic.forever(on_forever)

def on_forever2():
    if _7 == 1 or _7 == 2 or _7 == 3:
        pass
basic.forever(on_forever2)
