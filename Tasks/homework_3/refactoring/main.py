from typing import Union
from Tasks.homework_3.refactoring.heroes import Superman, SuperHero
from Tasks.homework_3.refactoring.places import Kostroma, Tokyo, Kirigua


def save_the_place(hero: SuperHero, place: Union[Kostroma, Tokyo, Kirigua]):
    hero.find(place)
    hero.attack()
    if hero.can_use_ultimate_attack:
        hero.ultimate()
    hero.create_news(place)
    hero.planets_notify(place)


if __name__ == '__main__':
    save_the_place(Superman(), Kostroma())
    print('-' * 20)
    save_the_place(SuperHero('Chack Norris', False), Tokyo())
    print('-' * 20)
    save_the_place(SuperHero('Bruce Willis', False), Kirigua())
