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
def get_var_name():
    if not (_1 == 0):
        return 1
    else:
        if not (_2 == 0):
            return 2
        else:
            if not (_3 == 0):
                return 3
            else:
                if not (_4 == 0):
                    return 4
                else:
                    if not (_5 == 0):
                        return 5
                    else:
                        if not (_6 == 0):
                            return 6
                        else:
                            return 7

def on_button_pressed_a():
    global started, expired
    if 1 == started:
        convert_type(get_var_name(), 1)
    else:
        started = 1
        basic.show_string("Hello!")
        basic.show_string("Password Please")
        expired = 15
        while not (expired == 0):
            basic.pause(1000)
            expired += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    if 1 == started:
        convert_type(get_var_name(), 3)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    if 1 == started:
        convert_type(get_var_name(), 2)
input.on_button_pressed(Button.B, on_button_pressed_b)

# reset

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

expired = 0
started = 0
_7 = 0
_6 = 0
_5 = 0
_4 = 0
_3 = 0
_2 = 0
_1 = 0
started = 0

def on_forever():
    if not _7 == 1 or 2 or 3:
        basic.show_string("Correct")
    else:
        num = 0
        if num == 7:
            basic.show_string("Wrong")
basic.forever(on_forever)
