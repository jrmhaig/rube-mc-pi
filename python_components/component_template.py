#!/usr/bin/python
#
# Python component for a Rube Goldberb machine.

from random import randrange
from time import sleep

def wait_for_input_trigger():
    """ Input trigger

    This function must wait until an input signal is triggered.
    For the example here, the trigger is pressing the enter key.

    """
    x = raw_input("Press enter:")

def trigger_output():
    """ Output trigger

    This function must carry out the work of this step and trigger the output.
    For this example, the 'work' is choosing random numbers until the correct
    value if chosen. The output trigger is the message "Continue!"

    """
    target = 5
    while randrange(10) != target:
        print "."
        sleep(0.3)
    print "Continue!"

def reset():
    """ Reset

    This function resets the step.
    For this example, the step is reset by answering y or Y to the question.

    """
    yn = raw_input("Reset?")
    return yn == 'y' or yn == 'Y'

go = True
while go:
    wait_for_input_trigger()
    trigger_output()
    go = reset()
