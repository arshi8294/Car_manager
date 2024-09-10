from abc import ABC, abstractmethod
from random import choice


class Car(ABC):
    @abstractmethod
    def coupe(self):
        pass

    @abstractmethod
    def suv(self):
        pass


class Benz(Car):
    def coupe(self):
        return BenzCoupe()

    def suv(self):
        return BenzSuv()


class Bmw(Car):
    def coupe(self):
        return BmwCoupe()

    def suv(self):
        return BmwSuv()


class Coupe(ABC):
    @abstractmethod
    def coupe_car(self):
        pass


class Suv(ABC):
    @abstractmethod
    def suv_car(self):
        pass


class BenzCoupe(Coupe):
    CARS = ['E-class', 'C-class', 'AMG GT', 'S-class']

    def coupe_car(self):
        return f'Your COUPE car is "Benz {choice(self.CARS)}"'


class BenzSuv(Suv):
    CARS = ['GLS', 'GLA', 'GLC', 'G-CLASS', 'GLE']

    def suv_car(self):
        return f'Your SUV car is "Benz {choice(self.CARS)}'


class BmwCoupe(Coupe):
    CARS = ['M240i Coupe', '230i Coupe', '430i xDrive Coupe']

    def coupe_car(self):
        return f'Your COUPE car is "Bmw {choice(self.CARS)}"'


class BmwSuv(Suv):
    CARS = ['X1 xDrive28i', 'X1 M35i', 'X3 xDrive30']

    def suv_car(self):
        return f'Your SUV car is "BMW {choice(self.CARS)}'


class Handler:
    COMPANIES = {
        'benz': Benz,
        'bmw': Bmw
    }

    @classmethod
    def handle(cls):
        car_company = input("Enter your car company: ").lower()
        model = input("Enter your car type(suv/coupe): ").lower()
        car = cls.COMPANIES[car_company]()
        result = None
        if model == 'coupe':
            result = car.coupe().coupe_car()
        elif model == 'suv':
            result = car.suv().suv_car()
        return result


if __name__ == '__main__':
    handler = Handler()
    res = handler.handle()
    print(res)

