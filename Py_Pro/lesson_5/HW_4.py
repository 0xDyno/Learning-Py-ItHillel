"""
Implement a digital counter class. Implement methods in the class:

1. initialization of the counter (provide for setting the counter with
    default values 0-100) (method __init__())
2. increase counter by 1 (increase() method)
3. returning the current counter value (method get_current_value())

The class structure is given below:

class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        pass

    def increase(self):
        pass

    def get_current_value(self):
        pass
"""


class DigitalCounter:
    def __init__(self, start=0, end=100, current=None):
        self.__start = start
        self.__end = end
        self.__current = current if current is not None else self.__start

    def increase(self):
        """Increases the counter by 1 if it's not finished"""
        if self.__current < self.__end:
            self.__current += 1
        # else:
        #     raise ValueError("Finished")      # depends on the conditions

    def get_current_value(self):
        return self.__current