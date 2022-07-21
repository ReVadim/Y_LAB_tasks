from .antagonist_finder import AntagonistFinder
from .weapon_mixins import GunFireMixin, LaserIncinerateMixin


class NewsPaper:
    """ the class that deals with the output of information
    """
    def create_news(self: 'SuperHero', place):
        place_name = getattr(place, 'city_name', 'place')
        print(f'{self.name} saved the {place_name}!')

    def planets_notify(self: 'SuperHero', place):
        coordinates = getattr(place, 'coordinates', '')
        place_name = getattr(place, 'city_name', 'place')
        if coordinates:
            [print(f'Planet {coordinate}! {self.name} save the {place_name}') for coordinate in coordinates]


class SuperHero(NewsPaper, GunFireMixin):

    def __init__(self, name, can_use_ultimate_attack=True):
        self.name = name
        self.can_use_ultimate_attack = can_use_ultimate_attack
        self.finder = AntagonistFinder()

    def find(self, place):
        self.finder.get_antagonist(place)

    def attack(self):
        self.fire_a_gun()

    def ultimate(self):
        pass


class Superman(LaserIncinerateMixin, SuperHero):

    def __init__(self):
        super(Superman, self).__init__('Clark Kent', True)

    def ultimate(self):
        self.incinerate_with_lasers()


# TODO: class SuperHero
#  Проблема: Герой не должен заниматься оповещениями о своей победе, это задача масс-медиа.
#  Несоблюден: Принцип единой ответственности.
#  По SOLID: Вынести оповещение в отдельный класс, занимающийся выводом информации.
#  Когда возникнут трудности? Добавьте оповещение о победе героя через газеты или через TV (на выбор)
#  а также попробуйте оповестить планеты (у которых вместо атрибута name:str используется coordinates:List[float]).

# TODO: class SuperHero
#  Проблема: Для каждого супергероя реализованы все методы обращения с оружием.
#  Несоблюден: Принцип разделения интерфейса.
#  По SOLID: Создать классы-миксины для каждого оружия.
#  Когда возникнут трудности? Попробуйте запретить Чаку норрису пользоваться лазерами из глаз!

# TODO: class Superman
#  Проблема: Сигнатура метода изменилась. Если мэр города обратится к супермену как к супергерою у
#  Кларка возникнут проблемы с атакой.
#  Несоблюден: Принцип подстановки Барбары Лисков
#  По SOLID: Не допускать таких вольностей
#  Когда возникнут трудности? При первой же битве
