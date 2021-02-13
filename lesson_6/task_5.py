class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        super().draw()
        print(self.title)


class Pencil(Stationery):
    def draw(self):
        super().draw()
        print(self.title)


class Handle(Stationery):
    def draw(self):
        super().draw()
        print(self.title)
