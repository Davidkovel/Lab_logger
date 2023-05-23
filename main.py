# task 1

import logging


class Calculator:
    def __init__(self):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.StreamHandler())

    def add(self, a, b):
        result = a + b
        self.logger.info(f" {a} + {b} = {result}")
        return result

    def minus(self, a, b):
        result = a - b
        self.logger.info(f" {a} - {b} = {result}")
        return result

    def mupltiply(self, a, b):
        result = a * b
        self.logger.info(f" {a} * {b} = {result}")
        return result

    def devide(self, a, b):
        try:
            result = a // b
            self.logger.info(f" {a} // {b} = {result}")
            return result
        except ZeroDivisionError as ex:
            print("error", ex)


c = Calculator()
print(c.mupltiply(15, 3))
print(c.add(15, 3))
print(c.minus(15, 3))
print(c.devide(15, 0))
