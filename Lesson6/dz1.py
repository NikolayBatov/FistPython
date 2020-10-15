from time import sleep


class TrafficLight:
    RESET = "\033[0m"
    RED = "\033[31m"
    YELLOW = "\033[33m"
    GREEN = "\033[32m"
    SQUARE = chr(9632)

    def __init__(self):
        self.__color = TrafficLight.RED

    def running(self, repeat):
        for i in range(repeat):
            if i > 1:
                self.__reset_output()
            self.__print_light()
            self.__color = TrafficLight.YELLOW
            sleep(7)
            self.__reset_output()
            self.__print_light()
            self.__color = TrafficLight.GREEN
            sleep(2)
            self.__reset_output()
            self.__print_light()
            self.__color = TrafficLight.RED
            sleep(7)

    def __reset_output(self):
        print(f"\r{TrafficLight.RESET}", end="")

    def __print_light(self):
        print(f"{self.__color}{TrafficLight.SQUARE}", end="")


light = TrafficLight()
light.running(1)
