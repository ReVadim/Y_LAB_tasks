from .places import Kostroma, Tokyo, Kirigua
from abc import ABCMeta, abstractmethod


class Place(metaclass=ABCMeta):
    @abstractmethod
    def get_antagonist(self, place):
        pass


class AntagonistFinder(Place):

    def get_antagonist(self, place):
        if isinstance(place, Kostroma):
            place.get_orcs()
        elif isinstance(place, Tokyo):
            place.get_godzilla()
        elif isinstance(place, Kirigua):
            place.get_aliens()


# TODO: Проблема: Класс, отвечающий за вызов верного метода у классов разного типа добавляет излишнюю сложность.
#  Несоблюден: Принцип инверсии зависимостей.
#  По SOLID: Создать абстрактный класс Place, обязывающий реализовать метод для поиска злодея.
#  Когда возникнут трудности: Когда ваш проект обретет мировую славу
