from equation_solver_class import EquationSolver
from input_exceptions import *


COEFF_MESSAGE = ('Введите коэффициенты a0, a1 ... aN для уравнения вида: '
                 '"a0*x**0 + a1*x**1 + ... + aN*x**N" через пробел:\n')
BORDER_MESSAGE = 'Введите границы области поиска через пробел:\n'

def get_input(message):
    values_string = input(message).strip()
    values = [float(value) for value in values_string.split(' ')]
    return values

def get_coeffs():
    while True:
        try:
            coeffs = get_input(COEFF_MESSAGE)
        except ValueError: 
            print('Введите только числовые значения!')
            continue
        else:
            break
    return coeffs

def get_borders():
    while True:
        try:
            borders = get_input(BORDER_MESSAGE)
            if len(borders) != 2:
                raise MoreThanTwoValues
            if borders[0] >= borders[1]:
                raise FirstBiggerThanSecond
        except ValueError: 
            print('Введите только числовые значения!')
            continue
        except MoreThanTwoValues:
            print('Границ должно быть только две!')
            continue
        except FirstBiggerThanSecond:
            print('Первое число должно быть меньше второго!')
            continue
        else:
            break
    return borders

def get_accuracy(borders):
    while True:
        try:
            accuracy = float(input('Введите желаемую точность (например, "0.001"):\n').strip())
            if accuracy/(borders[1] - borders[0]) > 0.1:
                raise AccuracyValueTooBig
        except ValueError:
            print('Введите значение типа "float" (например, "0.001")!')
            continue
        except AccuracyValueTooBig:
            print('Слишком грубая точность!')
        else:
            break
    return accuracy

def solve_equation():
    borders = get_borders()
    equation.set_borders(*borders)
    accuracy = get_accuracy(borders)
    equation.solve(accuracy)

def keep_going():
    POSITIVE_RESPONSES = ('y', 'yes', 'д', 'да')
    while True:
        response = input('Переопределить границы и точность? (y/n) ').strip()
        if response.lower() in POSITIVE_RESPONSES:
            solve_equation()
        else:
            break


if __name__ == '__main__':
    coeffs = get_coeffs()
    equation = EquationSolver(*coeffs)
    print(f'Ваше уравнение: {equation} = 0')
    solve_equation()
    keep_going()


