from random import sample
from random import shuffle


def generate_random_numbers(range_size, nums_amount):
    return sample(range(1, range_size + 1), k=nums_amount)


class LottoCard:
    __rows = 3
    __cols = 9
    __nums_in_row = 5

    def __init__(self, kegs_amount):
        self.__lotto_card = generate_random_numbers(kegs_amount, self.__nums_in_row * self.__rows)
        self.__lotto_card.extend([' '] * ((self.__cols - self.__nums_in_row) * self.__rows))
        shuffle(self.__lotto_card)
        self.__nums_indexes = {val: index for index, val in enumerate(self.__lotto_card) if isinstance(val, int)}

    def __str__(self):
        return '\n'.join([''.join(f'{val:<4}' for val in self.__lotto_card[index:index + self.__cols])
                          for index in range(0, self.__rows * self.__cols, self.__cols)])

    def __contains__(self, number):
        return number in self.__nums_indexes

    def __bool__(self):
        return bool(self.__nums_indexes)

    def cross_out_number(self, number):
        if number in self.__nums_indexes:
            self.__lotto_card[self.__nums_indexes[number]] = '-'
            self.__nums_indexes.pop(number)


class LottoGame:
    __kegs_amount = 90

    def __init__(self):
        self.__user_card = LottoCard(self.__kegs_amount)
        self.__comp_card = LottoCard(self.__kegs_amount)
        self.__keg_bag = reversed(list(enumerate(generate_random_numbers(self.__kegs_amount, self.__kegs_amount))))

    def start(self):
        for left, keg in self.__keg_bag:
            print(f'Новый бочонок: {keg} (осталось {left})')
            print(f'{"-" * 10} Ваша карточка {"-" * 10}', self.__user_card, '-' * 35, sep='\n')
            print(f'{"-" * 7} Карточка компьютера {"-" * 7}', self.__comp_card, '-' * 35, sep='\n')

            answer = str()
            while answer not in {'y', 'n'}:
                answer = input('Зачеркнуть цифру? (y/n) ').lower()
            if answer == 'y' and keg not in self.__user_card \
                    or answer == 'n' and keg in self.__user_card:
                raise ValueError('Вы допустили ошибку! Игра окончена.')
            self.__user_card.cross_out_number(keg)
            self.__comp_card.cross_out_number(keg)

            if not self.__comp_card or not self.__user_card:
                self.__determine_winner()

    def __determine_winner(self):
        if not self.__comp_card and not self.__user_card:
            raise StopIteration('Победила дружба!')
        elif not self.__user_card:
            raise StopIteration('Вы победили!')
        elif not self.__comp_card:
            raise StopIteration('Победил компуктер!')


try:
    LottoGame().start()
except ValueError as error:
    print(error)
except StopIteration as error:
    print(error)
