class OrgTechnics:
    def __init__(self, kind, name, serial, year):
        self.__kind = kind
        self.__name = name
        self.__serial = serial
        self.__year = year

    @property
    def kind(self):
        return self.__kind

    @property
    def name(self):
        return self.__name

    @property
    def serial(self):
        return self.__serial

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f'тип: {self.kind}, название: {self.name}, серийник: {self.serial}, год: {self.year}'


class Printer(OrgTechnics):
    def __init__(self, name, serial, year, cartridges):
        super().__init__(self.__class__.__name__, name, serial, year)
        self.__cartriges = cartridges

    @property
    def cartridges(self):
        return self.__cartriges

    def __str__(self):
        return f'{super().__str__()}, картриджи: {self.cartridges}'


class Scanner(OrgTechnics):
    def __init__(self, name, serial, year, resolution):
        super().__init__(self.__class__.__name__, name, serial, year)
        self.__resolution = resolution

    @property
    def resolution(self):
        return self.__resolution

    def __str__(self):
        return f'{super().__str__()}, разрешение: {self.resolution}'


class Xerox(Scanner):
    def __init__(self, name, serial, year, resolution, speed):
        super().__init__(name, serial, year, resolution)
        self.__speed = speed

    @property
    def speed(self):
        return self.__speed

    def __str__(self):
        return f'{super().__str__()}, скорость: {self.speed}'


class Stock:
    def __init__(self):
        self.__stock = {}

    @property
    def stock(self):
        return self.__stock

    def add(self, item):
        self.stock.setdefault(item.kind, {})
        self.stock[item.kind].update({item.serial: item})

    def get(self, serial):
        for key in self.stock:
            if serial in self.stock[key]:
                return self.stock[key][serial]
        raise ValueError(f'{serial} нет на складе')


class StockCommandsParser:
    def __init__(self, stock):
        self.__stock = stock

    def parse_command(self, command):
        if command == 'get':
            serials = input('Введите серийные номера через пробел:\n').split()
            return self.__get_command(*serials)
        elif command == 'add':
            amount = int(input('Введите количество объектов: '))
            self.__add_command(*self.__generate_items(amount))
        elif command == 'info':
            serials = input('Введите серийные номера через пробел:\n').split()
            self.__info_command(*serials)
        else:
            raise ValueError('Неверная команда')

    def __add_command(self, *args):
        for item in args:
            self.__stock.add(item)
            print(item.serial, 'добавлен на склад')

    def __get_command(self, *args):
        items, item = [], None
        for serial in args:
            try:
                items.append(self.__stock.get(serial))
            except ValueError as error:
                print(error)
        return items

    def __info_command(self, *args):
        for serial in args:
            try:
                print(f'Информация о {serial}:\n{self.__stock.get(serial)}')
            except ValueError as error:
                print(error)

    def __generate_items(self, amount):
        items = []
        for index in range(amount):
            print(f'Добавление {index + 1} объекта:')
            try:
                item = self.__generate_item(input('Введите тип объекта: ').capitalize())
                items.append(item)
            except ValueError as error:
                print(error)
        return items

    def __generate_item(self, kind):
        if kind not in {'Принтер', 'Ксерокс', 'Сканнер'}:
            raise ValueError('Неизвестный объект')
        name, year, serial = input('Введите название: '), input('Введите серийник: '), int(input('Введите год: '))
        if kind == 'Принтер':
            item = Printer(name, year, serial, int(input('Введите количество катриджей: ')))
        elif kind == 'Ксерокс':
            item = Xerox(name, year, serial, input('Введите разрешение: '), input('Введите скорость: '))
        else:
            item = Scanner(name, year, serial, input('Введите разрешение: '))
        return item


stock = Stock()
stock_commands_parser = StockCommandsParser(stock)
while True:
    print(f'{"-" * 25} Склад {"-" * 25}')
    print('Чтобы добавить объекты на склад введите: add')
    print('Чтобы посмотреть информацию об объекте на складу введите: info')
    print('Чтобы получить объекты со склада введите: get')
    print('Чтобы выйти введите: stop', "-" * 56, sep='\n')
    command = input('Введите команду: ')
    if command == 'stop':
        break
    try:
        stock_commands_parser.parse_command(command)
    except ValueError as error:
        print(error)
