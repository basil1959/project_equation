class EquationSolver:

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __str__(self):
        return (' + '.join((f'{coeff}*x**{i}' for i, coeff
                            in enumerate(self.coeffs))))

    def set_borders(self, borders):
        self.borders = borders
        self.border_1, self.border_2 = self.borders

    @property
    def border_values(self):
        return (self.calculate_polynomial(self.border_1),
                self.calculate_polynomial(self.border_2))

    def calculate_polynomial(self, value):
        return sum((coeff * value ** i for i, coeff in enumerate(self.coeffs)))

    def no_solution(self):
        self.k1 = 1 if self.border_values[0] > 0 else -1
        self.k2 = 1 if self.border_values[1] > 0 else -1

        return True if self.k1 * self.k2 > 0 else False

    def border_is_solution(self):
        if self.border_values[0] == 0 and self.border_values[1] == 0:
            self.x = f'x1 = {self.border_1}, x2 = {self.border_2}'
            return True
        elif self.border_values[0] == 0:
            self.x = f'x = {self.border_1}'
            return True
        elif self.border_values[1] == 0:
            self.x = f'x = {self.border_2}'
            return True

    def find_x(self, accuracy):
        x1, x2 = self.borders
        while abs(x1 - x2) > accuracy:
            self.x = (x1 + x2) / 2
            if self.calculate_polynomial(self.x) * self.k1 > 0:
                x1 = self.x
            else:
                x2 = self.x
    
        self.f_x = self.calculate_polynomial(self.x)

    def solve(self, accuracy):
        if self.border_is_solution():

            print(f'Одно (или оба) из граничных значений отрезка '
                  f'[{self.border_1}; {self.border_2}] '
                  f'является решением уравнения "{str(self)} = 0": {self.x}')

        elif self.no_solution():

            print(f'Решения в данной области нет. На концах отрезка '
                  f'[{self.border_1}; {self.border_2}] '
                  f'функция {str(self)} принимает значения '
                  f'одного знака соответственно {self.border_values[0]:.2f} '
                  f'и {self.border_values[1]:.2f}')

        else:

            self.find_x(accuracy)
            print(f'Корень уравнения "{str(self)} = 0" на отрезке '
                  f'[{self.border_1}; {self.border_2}] с точностью до '
                  f'{accuracy} равен {self.x:.4f}')
            print(f'Значение функции при x = {self.x:.4f} равно '
                  f'{self.f_x:.4f}. Заданная точность = {accuracy}')
