class Backpack:
    """ Рюкзак """

    def __init__(self, gift=None):
        self.content = []
        if gift is not None:
            self.content.append(gift)

    def add(self, item):
        """ Положить в рюкзак """
        self.content.append(item)
        print("В рюкзак положили:", item)

    def inspect(self, ):
        """ Проверить содержимое """
        print("В рюкзак лежит:")
        for item in self.content:
            print('    ', item)


my_backpack = Backpack(gift='флешка')
my_backpack.add(item='ноутбук')
my_backpack.add(item='зарядка для ноутбука')
my_backpack.inspect()