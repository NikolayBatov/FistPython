class Car:

    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self) -> str:
        return f"Car {self.name} is go"

    def stop(self) -> str:
        return f"Car {self.name} is stop"

    def turn(self, direction: str) -> str:
        return f"Car {self.name} turn on {direction}"

    def show_speed(self) -> int:
        return self.speed


class TownCar(Car):

    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, "TownCar", False)

    def show_speed(self):
        if self.speed < 60:
            return super().show_speed()
        return "Превышение скорости"


class SportCar(Car):

    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, "SportCar", False)


class WorkCar(Car):

    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, "WorkCar", False)

    def show_speed(self):
        if self.speed < 40:
            return super().show_speed()
        return "Превышение скорости"


class PoliceCar(Car):

    def __init__(self, speed: int, color: str):
        super().__init__(speed, color, "PoliceCar", True)


car1 = TownCar(61, "Red")
print(car1.show_speed())
car1 = TownCar(43, "Blue")
print(car1.show_speed())