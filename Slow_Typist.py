from math import *


class SlowTypist:

    def __init__(self):
        self.last_location = []

        self.distance_traveled = 0

        self.keypad = []
        self.keypad.append(["1", "2", "3"])
        self.keypad.append(["4", "5", "6"])
        self.keypad.append(["7", "8", "9"])
        self.keypad.append([".", "0"])

    def calculate_motion(self, input_string):
        for digit in input_string:
            for row_ind, line in enumerate(self.keypad):
                if digit in line:
                    location = (row_ind, line.index(digit))
                    if not self.last_location:
                        self.last_location = location
                        continue
                    self.distance_traveled += sqrt(abs(pow(abs(location[0]-self.last_location[0]), 2) +
                                                       pow(abs(location[1]-self.last_location[1]), 2)))
                    self.last_location = location

        print(self.distance_traveled)


myTypist = SlowTypist()
myTypist.calculate_motion("219.45.143.143")
