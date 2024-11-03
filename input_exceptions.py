class MoreThanTwoValues(Exception):
    def __str__(self):
        return 'Границ должно быть только две!'

class FirstBiggerThanSecond(Exception):
    def __str__(self):
        return 'Первое число должно быть меньше второго!'
    
class AccuracyValueTooBig(Exception):
    def __str__(self):
        return 'Слишком большое значение точности'