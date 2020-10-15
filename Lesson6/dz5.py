class Stationery:

    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):

    def __init__(self):
        super().__init__("Ручка")

    def draw(self):
        super().draw()
        print(self.title)


class Pencil(Stationery):

    def __init__(self):
        super().__init__("Карандаш")

    def draw(self):
        super().draw()
        print(self.title)


class Handle(Stationery):

    def __init__(self):
        super().__init__("Маркер")

    def draw(self):
        super().draw()
        print(self.title)


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
