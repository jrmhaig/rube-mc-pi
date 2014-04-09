"""
Adaptor for Raspberry Pi GPIO plugs.

The JSON config looks like this:

    { "source": {
        "type": "gpio",
        "pin": 18,
        "low_state_block": [0, 0],
        "high_state_block": [45, 0]
        },
        
      "target":  {
        "type": "gpio",
        "pin": 12
        }
    }
"""

from mcpi.block import Block
import rube

class GpioSource(rube.Source): #pylint: disable=R0903
    """
        Use the input from the raspberry pi GPIO pin 
    """
    def __init__(self, attribs):
        super(GpioSource, self).__init__()
        self.pin = attribs["pin"]
        self.low_state_block = Block(attribs["low_state_block"][0], attribs["low_state_block"][1])
        self.high_state_block = Block(attribs["high_state_block"][0], attribs["high_state_block"][1])

        def poll_state(self):
            pass
