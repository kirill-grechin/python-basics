from random import sample
from random import shuffle


class KegBag:
    __kegs_amount = 90

    @classmethod
    @property
    def kegs_amount(cls):
        return cls.__kegs_amount

    @staticmethod
    def generate_random_numbers(range_size, nums_amount):
        return sample(range(1, range_size + 1), k=nums_amount)

    def __init__(self):
        self.__keg_bag = self.generate_random_numbers(self.kegs_amount, self.kegs_amount)

    @property
    def keg_bag(self):
        return self.__keg_bag


class LottoCard:
    __rows = 3
    __cols = 9
    __nums_in_row = 5

    def __init__(self):
        values = KegBag.generate_random_numbers(KegBag.kegs_amount, self.__nums_in_row * self.__rows)
        values.extend([' '] * ((self.__cols - self.__nums_in_row) * self.__rows))
        shuffle(values)
        self.__lotto_card = values
        self.__nums_indexes = {val: index for index, val in enumerate(values) if isinstance(val, int)}

    def __str__(self):
        return '\n'.join([''.join(f'{val:<4}'
                                  for val in self.__lotto_card[index:index + self.__cols])
                          for index in range(0, self.__rows * self.__cols, self.__cols)])

    def cross_out_number(self, number):
        if number in self.__nums_indexes:
            self.__lotto_card[self.__nums_indexes[number]] = '-'
            self.__nums_indexes.pop(number)

    def is_number_in_card(self, number):
        return number in self.__nums_indexes

    def is_card_empty(self):
        return not bool(self.__nums_indexes)


class LottoGame:
    def __init__(self):
        self.__human_card = LottoCard()
        self.__computer_card = LottoCard()
        self.__keg_bag = KegBag().keg_bag

    def start(self, auto_mode=False):
        for index, keg in reversed(list(enumerate(self.__keg_bag))):
            print(f'Новый бочонок: {keg} (осталось {index})')
            print(f'{"-" * 10} Ваша карточка {"-" * 10}', self.__human_card, '-' * 35, sep='\n')
            print(f'{"-" * 7} Карточка компьютера {"-" * 7}', self.__computer_card, '-' * 35, sep='\n')

            if auto_mode:
                self.__human_card.cross_out_number(keg)
                self.__computer_card.cross_out_number(keg)
            else:
                data = str()
                while data not in ('y', 'n'):
                    data = input('Зачеркнуть цифру? (y/n) ').lower()
                if data == 'y' and not self.__human_card.is_number_in_card(keg) \
                        or data == 'n' and self.__human_card.is_number_in_card(keg):
                    raise ValueError('Вы допустили ошибку! Игра окончена.')
                if data == 'y':
                    self.__human_card.cross_out_number(keg)
                self.__computer_card.cross_out_number(keg)

            if self.__computer_card.is_card_empty() and self.__human_card.is_card_empty():
                raise StopIteration('Победила дружба!')
            elif self.__human_card.is_card_empty():
                raise StopIteration('Вы победили!')
            elif self.__computer_card.is_card_empty():
                raise StopIteration('Победил компуктер!')


try:
    LottoGame().start()
except ValueError as ve:
    print(ve)
except StopIteration as si:
    print(si)
