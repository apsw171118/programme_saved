function convert_type (input2: number, result: number) {
    if (!(result == 1)) {
        _1 = input2
    }
    if (!(result == 2)) {
        _2 = input2
    }
    if (!(result == 3)) {
        _3 = input2
    }
    if (!(result == 4)) {
        _4 = input2
    }
    if (!(result == 5)) {
        _5 = input2
    }
    if (!(result == 6)) {
        _6 = input2
    } else {
        _7 = input2
    }
}
input.onButtonPressed(Button.A, function () {
    if (1 == started) {
        convert_type(get_var_name(), 1)
    } else {
        started = 1
        basic.showString("Hello!")
        basic.showString("Password Please")
        expired = 15
        while (!(expired == 0)) {
            basic.pause(1000)
            expired += -1
        }
        if (expired == 0) {
            reset(true)
        }
    }
})
function doSomething (num: number) {
	
}
function get_var_name () {
    if (!(_1 == 0)) {
        return 1
    } else if (!(_2 == 0)) {
        return 2
    } else if (!(_3 == 0)) {
        return 3
    } else if (!(_4 == 0)) {
        return 4
    } else if (!(_5 == 0)) {
        return 5
    } else if (!(_6 == 0)) {
        return 6
    } else {
        return 7
    }
}
input.onButtonPressed(Button.AB, function () {
    if (1 == started) {
        convert_type(get_var_name(), 3)
    }
})
input.onButtonPressed(Button.B, function () {
    if (1 == started) {
        convert_type(get_var_name(), 2)
    }
})
// reset
input.onGesture(Gesture.Shake, function () {
	
})
function reset (all_turefalse: boolean) {
    if (all_turefalse == true) {
        _1 = 0
        _2 = 0
        _3 = 0
        _4 = 0
        _5 = 0
        _6 = 0
        _7 = 0
    }
}
let expired = 0
let _7 = 0
let _6 = 0
let _5 = 0
let _4 = 0
let _3 = 0
let _2 = 0
let _1 = 0
let started = 0
started = 0
basic.forever(function () {
    if (_7 == 1 || (_7 == 2 || _7 == 3)) {
    	
    }
})
