# Задание 3.
# Создайте класс для перевода из метрической системы в английскую и наоборот.
# Функциональность необходимо реализовать в виде статических методов.
# Обязательно реализуйте перевод мер длины.
class Measures_of_length:
    num_length = 0

    @staticmethod
    def inch_to_millimeter(length):
        Measures_of_length.num_length += 1
        return length * 25.4

    @staticmethod
    def inch_to_centimeter(length):
        Measures_of_length.num_length += 1
        return length * 2.54

    @staticmethod
    def inch_to_decimeter(length):
        Measures_of_length.num_length += 1
        return length * 0.254

    @staticmethod
    def inch_to_meter(length):
        Measures_of_length.num_length += 1
        return length * 0.0254

    @staticmethod
    def inch_to_kilometer(length):
        Measures_of_length.num_length += 1
        return length * 0.0000254

    @staticmethod
    def millimeter_to_inch(length):
        Measures_of_length.num_length += 1
        return length / 25.4

    @staticmethod
    def centimeter_to_inch(length):
        Measures_of_length.num_length += 1
        return length / 2.54

    @staticmethod
    def decimeter_to_inch(length):
        Measures_of_length.num_length += 1
        return length / 0.254

    @staticmethod
    def meter_to_inch(length):
        Measures_of_length.num_length += 1
        return length / 0.0254

    @staticmethod
    def kilometer_to_inch(length):
        Measures_of_length.num_length += 1
        return length / 0.0000254

    @staticmethod
    def foot_to_millimeter(length):
        Measures_of_length.num_length += 1
        return length * 304.8

    @staticmethod
    def foot_to_centimeter(length):
        Measures_of_length.num_length += 1
        return length * 30.48

    @staticmethod
    def foot_to_decimeter(length):
        Measures_of_length.num_length += 1
        return length * 3.048

    @staticmethod
    def foot_to_meter(length):
        Measures_of_length.num_length += 1
        return length * 0.3048

    @staticmethod
    def foot_to_kilometer(length):
        Measures_of_length.num_length += 1
        return length * 0.0003048

    @staticmethod
    def millimeter_to_foot(length):
        Measures_of_length.num_length += 1
        return length / 304.8

    @staticmethod
    def centimeter_to_foot(length):
        Measures_of_length.num_length += 1
        return length / 30.48

    @staticmethod
    def decimeter_to_foot(length):
        Measures_of_length.num_length += 1
        return length / 3.048

    @staticmethod
    def meter_to_foot(length):
        Measures_of_length.num_length += 1
        return length / 0.3048

    @staticmethod
    def kilometer_to_foot(length):
        Measures_of_length.num_length += 1
        return length / 0.0003048

    @staticmethod
    def yard_to_millimeter(length):
        Measures_of_length.num_length += 1
        return length * 914.4

    @staticmethod
    def yard_to_centimeter(length):
        Measures_of_length.num_length += 1
        return length * 91.44

    @staticmethod
    def yard_to_decimeter(length):
        Measures_of_length.num_length += 1
        return length * 9.144

    @staticmethod
    def yard_to_meter(length):
        Measures_of_length.num_length += 1
        return length * 0.9144

    @staticmethod
    def yard_to_kilometer(length):
        Measures_of_length.num_length += 1
        return length * 0.0009144

    @staticmethod
    def millimeter_to_yard(length):
        Measures_of_length.num_length += 1
        return length / 914.4

    @staticmethod
    def centimeter_to_yard(length):
        Measures_of_length.num_length += 1
        return length / 91.44

    @staticmethod
    def decimeter_to_yard(length):
        Measures_of_length.num_length += 1
        return length / 9.144

    @staticmethod
    def meter_to_yard(length):
        Measures_of_length.num_length += 1
        return length / 0.9144

    @staticmethod
    def kilometer_to_yard(length):
        Measures_of_length.num_length += 1
        return length / 0.0009144

    @staticmethod
    def get_num_length():
        return Measures_of_length.num_length


print('дюйм (inch):')
print(f'10 inch = {Measures_of_length.inch_to_millimeter(10)} mm')
print(f'10 inch = {Measures_of_length.inch_to_centimeter(10)} sm')
print(f'10 inch = {Measures_of_length.inch_to_decimeter(10)} dm')
print(f'10 inch = {Measures_of_length.inch_to_meter(10)} m')
print(f'10 inch = {Measures_of_length.inch_to_kilometer(10)} km')
print(f'5 mm = {Measures_of_length.millimeter_to_inch(5)} inch')
print(f'5 sm = {Measures_of_length.centimeter_to_inch(5)} inch')
print(f'5 dm = {Measures_of_length.decimeter_to_inch(5)} inch')
print(f'5 m = {Measures_of_length.meter_to_inch(5)} inch')
print(f'5 km = {Measures_of_length.kilometer_to_inch(5)} inch')
print('фут (foot):')
print(f'3 foot = {Measures_of_length.foot_to_millimeter(3)} mm')
print(f'3 foot = {Measures_of_length.foot_to_centimeter(3)} sm')
print(f'3 foot = {Measures_of_length.foot_to_decimeter(3)} dm')
print(f'3 foot = {Measures_of_length.foot_to_meter(3)} m')
print(f'3 foot = {Measures_of_length.foot_to_kilometer(3)} km')
print(f'2 mm = {Measures_of_length.millimeter_to_foot(2)} foot')
print(f'2 sm = {Measures_of_length.centimeter_to_foot(2)} foot')
print(f'2 dm = {Measures_of_length.decimeter_to_foot(2)} foot')
print(f'2 m = {Measures_of_length.meter_to_foot(2)} foot')
print(f'2 km = {Measures_of_length.kilometer_to_foot(2)} foot')
print('ярд (yard):')
print(f'7 yard = {Measures_of_length.yard_to_millimeter(7)} mm')
print(f'7 yard = {Measures_of_length.yard_to_centimeter(7)} sm')
print(f'7 yard = {Measures_of_length.yard_to_decimeter(7)} dm')
print(f'7 yard = {Measures_of_length.yard_to_meter(7)} m')
print(f'7 yard = {Measures_of_length.yard_to_kilometer(7)} km')
print(f'12 mm = {Measures_of_length.millimeter_to_yard(12)} yard')
print(f'12 sm = {Measures_of_length.centimeter_to_yard(12)} yard')
print(f'12 dm = {Measures_of_length.decimeter_to_yard(12)} yard')
print(f'12 m = {Measures_of_length.meter_to_yard(12)} yard')
print(f'12 km = {Measures_of_length.kilometer_to_yard(12)} yard')
print(f'Количество подсчетов длины: {Measures_of_length.get_num_length()}')