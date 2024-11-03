from equation_solver_class import EquationSolver
from input_exceptions import UserInputError


COEFF_MESSAGE = ('Введите коэффициенты a0, a1, ..., aN для уравнения вида: '
                 '"a0*x**0 + a1*x**1 + ... + aN*x**N" через пробел:\n')
BORDER_MESSAGE = 'Введите границы области поиска через пробел:\n'
POSITIVE_RESPONSES = ('y', 'yes', 'д', 'да')


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
                raise UserInputError
            if borders[0] >= borders[1]:
                raise UserInputError
        except ValueError:
            print('Введите только числовые значения!')
            continue
        except UserInputError:
            print('Границ должно быть только две, причём')
            print('первое число должно быть меньше второго!')
            continue
        else:
            break
    return borders


def get_accuracy(borders):
    while True:
        try:
            accuracy = float(input('Введите желаемую точность '
                                   '(например, "0.001"):\n').strip())
            if accuracy <= 0:
                raise UserInputError
            if accuracy/(borders[1] - borders[0]) > 0.1:
                raise UserInputError
        except ValueError:
            print('Введите значение типа "float" (например, "0.001")!')
            continue
        except UserInputError:
            print('Неправильно задана точность!')
        else:
            break
    return accuracy


def solve_equation(equation):
    borders = get_borders()
    equation.set_borders(borders)
    accuracy = get_accuracy(borders)
    equation.solve(accuracy)


def run_equation_solver():
    coeffs = get_coeffs()
    equation = EquationSolver(coeffs)
    print(f'Ваше уравнение: {equation} = 0')
    while True:
        solve_equation(equation)
        response = input('Переопределить границы и точность? (y/n) ')
        if response.strip().lower() not in POSITIVE_RESPONSES:
            break


if __name__ == '__main__':
    run_equation_solver()
