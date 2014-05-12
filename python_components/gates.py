import turtle as t
from time import sleep

class Logic:
    """ Base class for all logic gates and components """
    def __init__(self, x, y, size):
        self.outputs = []
        self.inputs = []
        self.value = 2 # = unknown
        self.x = x
        self.y = y
        self.exit_x = x + 2 * size
        self.exit_y = y + size
        self.size = size
        self.COLOURS = ['red','blue', 'black']

    def go_to_start(self):
        """ Move the turtle to the start point for drawing the gate """
        t.penup()
        t.setpos(self.x, self.y)
        t.pendown()

    def go_to_exit(self):
        """ Move to the exit point for the gate """
        t.penup()
        t.setpos(self.exit_x, self.exit_y)
        t.pendown()

    def go_to_input(self, inpt):
        """ Move to the input point for the gate from the given input """
        t.penup()
        self.draw_to_input(inpt)
        t.pendown()

    def get_input_index(self, inpt):
        """ Get the index of the given input """
        return self.inputs.index(inpt)

    def get_n_inputs(self):
        """ Get the number of inputs to the gate """
        return len(self.inputs)

    def draw_to_input(self, inpt):
        """ Draw to the input point for the gate from the given input """
        n = self.get_input_index(inpt)
        t.setpos(self.x, self.y + 2 * self.size * (n+1)/(self.get_n_inputs()+1))

    def add_input(self, inpt):
        """ Add a new input to the gate """
        self.inputs.append(inpt)

    def add_output(self, outpt):
        """ Add a new output to the gate """
        self.outputs.append(outpt)
        outpt.add_input(self)

    def draw_outputs(self):
        """ Draw all outputs from the gate """
        t.color(self.COLOURS[self.calculate_value()])
        for out in self.outputs:
            self.go_to_exit()
            out.draw_to_input(self)
            t.dot(3)

    def print_value(self):
        """ Print the value in the gate """
        if self.value != 2:
            t.color(self.COLOURS[self.value])
            self.go_to_start()
            t.penup()
            t.forward(self.size)
            t.left(90)
            t.forward(self.size)
            t.pendown()
            t.write(self.value)
            t.penup()
            t.backward(self.size)
            t.right(90)

    def get_value(self):
        """ Return the value of the gate.
            Note, this does not attempt to calculate the value so it may be
            2=unknown even if all the inputs are present. 

        """
        return self.value

class Starter(Logic):
    """ Input value """

    def add_input(self, n):
        """ The starting point can only have one 'input', which should be
            and integer: 0 = false, 1 = true, 2 = undefined

        """
        self.inputs = n

    def calculate_value(self):
        """ Even though there is only one input, the value of the starting
            point is only set when it is 'calculated'

        """
        self.value = self.inputs
        self.print_value()
        return self.value

    def get_input_index(self, inpt):
        """ There is only one 'input' so the index is always 0 """
        return 0

    def get_n_inputs(self):
        """ There is only ever one input for a starting point """
        return 1

    def draw(self):
        """ An input is represented as a circle """
        self.go_to_start()
        t.penup()
        t.forward(self.size)
        t.pendown()
        t.circle(self.size, 360)
        t.penup()
        t.backward(self.size)
        t.pendown()

class Finish(Logic):
    """ Output values """

    def add_input(self, inpt):
        """ An end point can only have one input """
        self.inputs = inpt 

    def add_output(self, n):
        """ An end point does not have any outputs """
        pass

    def calculate_value(self):
        """ The value of an endpoint is the output value of the only input """
        if self.inputs != []:
            self.value = self.inputs.get_value()
            self.print_value()
            return self.value

    def get_input_index(self, inpt):
        """ There is only one 'input' so the index is always 0 """
        return 0

    def get_n_inputs(self):
        """ There is only ever one output for a starting point """
        return 1

    def draw(self):
        """ An input is represented as a box """
        self.go_to_start()
        for i in range(4):
            t.forward(2*self.size)
            t.left(90)

class LAnd(Logic):
    def draw(self):
        self.go_to_start()
        t.forward(self.size)
        t.circle(self.size, 180)
        t.forward(self.size)
        t.left(90)
        t.forward(2*self.size)
        t.left(90)

    def calculate_value(self):
        """ Calculate the output of an AND gate """
        self.value = 1
        for i in self.inputs:
            if i.get_value() == 0:  # A single false makes the output false
                self.value = 0
                break
            elif i.get_value() == 2:
                # A single unknown means the output cannot be true but it
                # may be false (hence no 'break')
                self.value = 2
        self.print_value()
        return self.value

# Four inputs
s1 = Starter(-200,100,30)
s1.add_input(1)

s2 = Starter(-200,30,30)
s2.add_input(0)

s3 = Starter(-200,-30,30)
s3.add_input(1)

s4 = Starter(-200,-100,30)
s4.add_input(1)

# Input 1 AND Input 2
a = LAnd(0,50,30)
s2.add_output(a)
s1.add_output(a)

# Input 3 AND Input 4
b = LAnd(0,-50,30)
s4.add_output(b)
s3.add_output(b)

c = LAnd(100, 0, 30)
b.add_output(c)
a.add_output(c)

d = Finish(250, 0, 30)
c.add_output(d)


bits = [ d, c, b, a, s1, s2, s3, s4 ]

for bit in bits:
    bit.draw()

while True:
    for bit in bits:
        if bit.value == 2:
            bit.draw_outputs()
