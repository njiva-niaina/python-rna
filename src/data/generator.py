import numpy as np


class FunctionValues:
    @staticmethod
    def __calculate_x(a: int, x: float):
        return float(a * x * (1 - x))

    @staticmethod
    def generate_values(count: int, a: int):
        xn = np.array([0.1])
        for i in range(count - 1):
            xi = FunctionValues.__calculate_x(a, xn[i])
            xn = np.append(xn, xi)
        return xn
