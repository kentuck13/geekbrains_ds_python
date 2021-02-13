class Car:
    current_speed = 0

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return self.current_speed

    def go(self):
        self.current_speed = self.speed

    def stop(self):
        self.current_speed = 0

    def turn(self, direction):
        self.current_speed = (self.speed / 100) * 30


class TownCar(Car):
    def show_speed(self):
        if self.current_speed > 60:
            print('Over speed')
        return self.current_speed


class WorkCar(Car):
    def show_speed(self):
        if self.current_speed > 40:
            print('Over speed')
        return self.current_speed
