#!/usr/bin/python3
#
# Python component for a Rube Goldberb machine.

from random import randrange
from time import sleep
import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital()

def wait_for_input_trigger():
    """ Input trigger

    This function must wait until an input signal is triggered.
    Here the trigger is pressing any of the PiFace Digital buttons.

    """
    button = 0
    while button == 0:
        button = pfd.input_port.value

def pin_reverse(val):
    """ Reverse the order of the binary representation """

    out = 0
    for i in range(7, -1, -1):
        if 2**i <= val:
            val = val - 2**i
            out = out + 2**(7-i)
    return int(out)

def trigger_output():
    """ Output trigger

    This function must carry out the work of this step and trigger the output.
    For this example, the 'work' is choosing random numbers until the correct
    value if chosen. The output trigger is the message "Continue!"

    """
    target = 128
    val = 0
    while val < target:
        if randrange(100) >= 51:
            if val > 0:
                val = val - 1
        else:
            val = val + 1
        print(val)
        pfd.output_port.value = pin_reverse(val)
        #sleep(0.02)
    print("Continue!")

def reset():
    """ Reset

    This function resets the step.
    In this example reset by pressing one of the buttons

    """
    button = 0
    while button == 0:
        button = pfd.input_port.value
    pfd.output_port.value = 0
    while button > 0:
        button = pfd.input_port.value
    return True

go = True
while go:
    wait_for_input_trigger()
    trigger_output()
    go = reset()
